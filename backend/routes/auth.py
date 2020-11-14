from flask import Flask, session, redirect, url_for, request, jsonify
from markupsafe import escape
import bcrypt
from app import app, User, db

@app.route('/auth')
def index():
  if 'user_id' in session:
    return 'Logged in as %s' % escape(session['user_id'])
  return 'You are not logged in'

# User Registration
@app.route('/auth/register', methods=['POST'])
def register():
  if request.json == None or not all([x in request.json for x in ['name','college','department','email','year','phone_number','gender','pronouns','description','password']]):
    return jsonify({'error': 'missing info'})
  
  # if already registered
  user = User.query.filter_by(email=request.json['email']).first()
  if user != None:
    return jsonify({'error': 'this email has already been registered'})

  u = User(
    name=request.json['name'],
    college=request.json['college'],
    department=request.json['department'],
    email=request.json['email'],
    year=request.json['year'],
    phone_number=request.json['phone_number'],
    gender=request.json['gender'],
    pronouns=request.json['pronouns'],
    description=request.json['description'],
    password=request.json['password']
    # password=bcrypt.hashpw(request.json['password'].encode('utf8'), bcrypt.gensalt()).decode('utf8'),
  )

  db.session.add(u)
  db.session.commit()

  print("new user:", u.id)

  session['user_id'] = u.id

  return jsonify({'status': 'success'})

# User Login
@app.route('/auth/login', methods=['POST'])
def login():
  if request.json == None or not all([x in request.json for x in ['email', 'password']]):
    return jsonify({'error': 'missing info'})

  email = request.json['email']
  password = request.json['password']

  user = User.query.filter_by(email=email).first()
  if not user:
    return jsonify({'error': 'no user found'})
    
  
  # if not bcrypt.checkpw(password.encode('utf8'), user.password.encode('utf8')):
  if password != user.password:
    return jsonify({'error': 'wrong password'})
  
  session['user_id'] = user.id
  return jsonify({'status': 'success'})

@app.route('/auth/logout')
def logout():
  session.pop('user_id', None)
  return redirect("/")


#get all (available/matched/finalized/finished) hangouts I posted
@app.route('/auth/my_hangouts')
def my_hangouts():
  if session['user_id'] == None:
    return jsonify({'error': 'not logged in'})

  if request.json == None or not all([x in request.json for x in ['hangout_type']]):
    return jsonify({'error': 'missing info'})

  hangout_type = request.json['hangout_type']
  uid = session['user_id']
  hangouts = Hangouts.query.filter_by(author_id = uid, status = hangout_type).all() + Hangouts.query.filter_by(participant_id = uid, status = hangout_type).all()
  return jsonify({'hangouts': hangouts})

#get all available hangouts that fit me
@app.route('/auth/my_feed')
def my_feed():
  if session['user_id'] == None:
    return jsonify({'error': 'not logged in'})

  #retrive key user info
  uid = session['user_id']
  user = User.query.filter_by(id=uid).first()
  name = user.name
  college = user.college
  department = user.department
  year = user.year
  gender = user.gender

  #filter all hangouts
  hangouts = Hangouts.query.all()
  feeds = []
  for hangout in hangouts:
    if hangout.status == 'available':
      if (name == hangout.cond_name or hangout.cond_name == '*') and \
         (college == hangout.cond_college or hangout.cond_college == '*') and \
         (department == hangout.department or hangout.cond_department == '*') and \
         (year == hangout.year or houngout.cond_year == 0) and \
         (gender == hangout.gender or hangout.cond_gender == '*'):
        feeds.append(hangout)

  return jsonify({'feeds': feeds})


#1. publish hangout
@app.route('/auth/publish', methods=['POST'])
def publish():
  if request.json == None or not all([x in request.json for x in ['time','location','activity','cond_name','cond_college','cond_department','cond_gender','cond_year']]):
    return jsonify({'error': 'missing info'})
  
  uid = session['user_id']
  h = Hangout(
    time=request.json['time'],
    location=request.json['location'],
    activity=request.json['activity'],
    cond_name=request.json['cond_name'],
    cond_college=request.json['cond_college'],
    cond_department=request.json['cond_department'],
    cond_gender=request.json['cond_gender'],
    cond_year=request.json['cond_year'],
    status='available',
    author_id=uid,
    participant_id=0
  )
  db.session.add(h)
  db.session.commit()

  print('create hangout:', h.id)
  return jsonify({'status': 'succeed'})

# 2. take a hangout
@app.route('/auth/take')
def take():
  if request.json == None or not all([x in request.json for x in ['hid']]):
    return jsonify({'error': 'missing info'})

  uid = session['user_id']
  hid = request.json['hid']
  h = Hangouts.query.filter_by(id = hid).first()

  if h == None:
    return jsonify({'error': 'no hangout found'})

  if h.status != 'available':
    return jsonify({'error': 'hangout not available'})

  # WILL THIS CHANGE THE DATABASE?
  h.participant_id = uid
  h.status = 'matched'
  db.session.commit()

  print('match hangout:', h.id)
  return jsonify({'status': 'succeed'})

# 3.1 the author accepts a matched handout
@app.route('/auth/accept')
def accept():
  if request.json == None or not all([x in request.json for x in ['hid']]):
    return jsonify({'error': 'missing info'})

  uid = session['user_id']
  hid = request.json['hid']
  h = Hangouts.query.filter_by(id = hid).first()

  if h == None:
    return jsonify({'error': 'no hangout found'})

  if h.status != 'matched' or h.author_id != uid:
    return jsonify({'error': 'this hangout cannot be accepted'})

  h.status = 'finalized'
  db.session.commit()
  print('accepted hangout:', h.id)
  return jsonify({'status': 'succeed'})

# 3.2 the author declines a matched handout
@app.route('/auth/decline')
def decline():
  if request.json == None or not all([x in request.json for x in ['hid']]):
    return jsonify({'error': 'missing info'})

  uid = session['user_id']
  hid = request.json['hid']
  h = Hangouts.query.filter_by(id = hid).first()

  if h == None:
    return jsonify({'error': 'no hangout found'})

  if h.status != 'matched' or h.author_id != uid:
    return jsonify({'error': 'this hangout cannot be declined'})

  #put the hangout back into available stage
  h.status = 'available'
  db.session.commit()
  print('declined hangout:', h.id)
  return jsonify({'status': 'succeed'})

# 4 refresh the whole hangout database by a time, changing some 'finalized' to 'finished'
# @app.route('/auth/finish')
# def finish():

