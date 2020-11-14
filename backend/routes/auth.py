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
    password=bcrypt.hashpw(request.json['password'].encode('utf8'), bcrypt.gensalt()).decode('utf8'),
  )

  db.session.add(u)
  db.session.commit()

  print(u.id)
  session['user_id'] = u.id

  return jsonify({'status': 'success'})

# User Login
@app.route('/auth/login', methods=['POST'])
def login():
  if request.json == None or not all([x in request.json for x in ['email', 'password']]):
    return jsonify({'error': 'missing login info'})
  email = request.json['email']
  password = request.json['password']

  user = User.query.filter_by(email=email).first()
  if not user:
    return jsonify({'error': 'no user found'})
    
  
  if not bcrypt.checkpw(password.encode('utf8'), user.password.encode('utf8')):
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
  hangout_type = request.json['hangout_type']
  author_id = session['user_id']
  #***
  hangouts = Hangouts.query.filter_by(author_id = author_id, status = 'hangout_type').all()
  return jsonify({'hangouts': hangouts})

#get all available hangouts that fit me
@app.route('/auth/my_feed')
def my_feed():
  uid = session['user_id']
  user = User.query.filter_by(id=uid).first()
  name = user.name
  college = user.college
  department = user.department
  year = user.year
  gender = user.gender

  hangouts = Hangouts.query.all()
  feeds = []
  for hangout in hangouts:
    if name == hangout.cond_name and \
       college == hangout.cond_college and \
       department == hangout.department and \
       year == hangout.year and \
       gender == hangout.gender:
       feeds.append(hangout)

  return jsonify({'feeds': feeds})


#1. publish hangout
@app.route('/auth/publish', methods=['POST'])
def publish():
  if request.json == None or not all([x in request.json for x in ['time','location','activity','cond_name','cond_college','cond_department','cond_gender','cond_year']]):
    return jsonify({'error': 'missing info'})
  
  h = Hangout(
    time=request.json['time'],
    location=request.json['location'],
    activity=request.json['activity'],
    cond_name=request.json['cond_name'],
    cond_college=request.json['cond_college'],
    cond_department=request.json['cond_department'],
    cond_gender=request.json['cond_gender'],
    cond_year=request.json['cond_year'],
    status='available'
  )
  db.session.add(h)
  db.session.commit()
  print(h.id)
  session['hangout_id'] = h.id

  return jsonify({'status': 'success'})

#2. match a hangout
# @app.route('/auth/match')
# def match():
#   uid = session['user_id']
#   user = User.query.filter_by(id=uid).first()
#   hid = request.json['hid']

  

#   hangouts = Hangouts.query.all()
#   feeds = []
#   for hangout in hangouts:
#     if name == hangout.cond_name and \
#        college == hangout.cond_college and \
#        department == hangout.department and \
#        year == hangout.year and \
#        gender = hangout.gender:
#        feeds.append(hangout)

#   session['my_feeds'] = feeds

#   return jsonify({'status': 'success'})
