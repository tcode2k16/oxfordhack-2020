from flask import Flask, session, redirect, url_for, request, jsonify
from markupsafe import escape
import bcrypt
from app import app, User, db


@app.route('/auth')
def index():
  if 'user_id' in session:
    return 'Logged in as %s' % escape(session['user_id'])
  return 'You are not logged in'

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




@app.route('/auth/login', methods=['POST'])
def login():
  if request.json == None:
    return jsonify({'error': 'no data'})
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
