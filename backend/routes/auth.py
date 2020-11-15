from flask import Flask, session, redirect, url_for, request, jsonify
from markupsafe import escape
import bcrypt
from app import app, User, db, Hangout


@app.route('/auth')
def index():
    if 'user_id' in session:
        return 'Logged in as %s' % escape(session['user_id'])
    return 'You are not logged in'

# User Registration


@app.route('/auth/register', methods=['POST'])
def register():
    if request.json == None or not all([x in request.json for x in ['name', 'college', 'department', 'email', 'year', 'phone_number', 'gender', 'pronouns', 'description', 'password']]):
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

    return jsonify({'status': 'register success', 'user_id': u.id})

# User Login


@app.route('/auth/user_info', methods=['GET'])
def info():
    if 'user_id' not in session:
        return jsonify({'error': 'not logged in'})

    user = User.query.filter_by(id=session['user_id']).first()

    return jsonify({'user': {
        'id': user.id,
        'name': user.name,
        'college': user.college,
        'department': user.department,
        'email': user.email,
        'year': user.year,
        'phone_number': user.phone_number,
        'gender': user.gender,
        'pronouns': user.pronouns,
        'description': user.description,
    }})


@app.route('/auth/user_update', methods=['POST'])
def update():
    if 'user_id' not in session:
        return jsonify({'error': 'not logged in'})
    if request.json == None or not all([x in request.json for x in ['name', 'college', 'department', 'email', 'year', 'phone_number', 'gender', 'pronouns', 'description']]):
        return jsonify({'error': 'missing info'})
    user = User.query.filter_by(id=session['user_id']).first()

    user.name = request.json['name']
    user.college = request.json['college']
    user.department = request.json['department']
    user.email = request.json['email']
    user.year = request.json['year']
    user.phone_number = request.json['phone_number']
    user.gender = request.json['gender']
    user.pronouns = request.json['pronouns']
    user.description = request.json['description']
    db.session.commit()
    return jsonify({'status': 'update success'})


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

    return jsonify({'status': 'login success', 'uid': user.id})


@app.route('/auth/logout', methods=['GET'])
def logout():
    session.pop('user_id', None)
    return jsonify({'status': 'logout success'})


# get all (available/matched/finalized/finished) hangouts I posted
@app.route('/auth/my_hangouts', methods=['POST'])
def my_hangouts():
    if 'user_id' not in session:
        return jsonify({'error': 'not logged in'})

    if request.json == None or not all([x in request.json for x in ['hangout_type']]):
        return jsonify({'error': 'missing info'})

    hangout_type = request.json['hangout_type']
    uid = session['user_id']
    hangouts = Hangout.query.filter_by(author_id=uid, status=hangout_type).all(
    ) + Hangout.query.filter_by(participant_id=uid, status=hangout_type).all()

    output = []
    for h in hangouts:
        uid = h.author_id
        if uid == session['user_id']:
            uid = h.participant_id
        u = User.query.filter_by(id=uid).first()
        o = {
            'hangout_id': h.id,
            'cond_name': h.cond_name,
            'cond_college': h.cond_college,
            'cond_department': h.cond_department,
            'cond_year': h.cond_year,
            'cond_gender': h.cond_gender,
            'activity': h.activity,
            'time': h.time,
            'location': h.location,
            'status': h.status,
            'author_id': h.author_id,
            'participant_id': h.participant_id,
        }
        if u != None:
            o['peer'] = {
                'id': u.id,
                'name': u.name,
                'college': u.college,
                'department': u.department,
                'email': u.email,
                'year': u.year,
                'phone_number': u.phone_number,
                'gender': u.gender,
                'pronouns': u.pronouns,
                'description': u.description,
            }
        output.append(o)
    return jsonify({'hangouts': output})

# get all available hangouts that fit me


@app.route('/auth/my_feed', methods=['POST', 'GET'])
def my_feed():
    if 'user_id' not in session:
        return jsonify({'error': 'not logged in'})

    # retrive key user info
    uid = session['user_id']
    user = User.query.filter_by(id=uid).first()
    name = user.name
    college = user.college
    department = user.department
    year = user.year
    gender = user.gender

    # filter all hangouts
    hangouts = Hangout.query.all()
    feeds = []
    for hangout in hangouts:
        if hangout.status == 'available':
            if (uid != hangout.author_id) and \
               (name == hangout.cond_name or hangout.cond_name == '*') and \
               (college == hangout.cond_college or hangout.cond_college == '*') and \
               (department == hangout.cond_department or hangout.cond_department == '*') and \
               (year == hangout.cond_year or hangout.cond_year == 0) and \
               (gender == hangout.cond_gender or hangout.cond_gender == '*'):
                u = User.query.filter_by(id=hangout.author_id).first()
                feeds.append({
                    'hangout_id': hangout.id,
                    'cond_name': hangout.cond_name,
                    'cond_college': hangout.cond_college,
                    'cond_department': hangout.cond_department,
                    'cond_year': hangout.cond_year,
                    'cond_gender': hangout.cond_gender,
                    'activity': hangout.activity,
                    'time': hangout.time,
                    'location': hangout.location,
                    'status': hangout.status,
                    'author_id': hangout.author_id,
                    'participant_id': hangout.participant_id,
                    'author': {
                        'id': u.id,
                        'name': u.name,
                        'college': u.college,
                        'department': u.department,
                        'email': u.email,
                        'year': u.year,
                        'phone_number': u.phone_number,
                        'gender': u.gender,
                        'pronouns': u.pronouns,
                        'description': u.description,
                    },
                })
    return jsonify({'feeds': feeds})


# 1. publish hangout
@ app.route('/auth/publish', methods=['POST'])
def publish():
    print("t3 ", ('user_id' in session))
    # print("pre-publishing check", ('user_id' in session))
    if 'user_id' not in session:
        return jsonify({'error': 'not logged in'})

    if request.json == None or not all([x in request.json for x in ['time', 'location', 'activity', 'cond_name', 'cond_college', 'cond_department', 'cond_gender', 'cond_year']]):
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
        participant_id=0,
    )
    db.session.add(h)
    db.session.commit()

    print('create hangout:', h.id)
    return jsonify({'status': 'publish succeed'})

# 2. take a hangout


@ app.route('/auth/take', methods=['POST'])
def take():
    if 'user_id' not in session:
        return jsonify({'error': 'not logged in'})

    if request.json == None or not all([x in request.json for x in ['hid']]):
        return jsonify({'error': 'missing info'})

    uid = session['user_id']
    hid = request.json['hid']
    h = Hangout.query.filter_by(id=hid).first()

    if h == None:
        return jsonify({'error': 'no hangout found'})

    if h.status != 'available':
        return jsonify({'error': 'hangout not available'})

    # WILL THIS CHANGE THE DATABASE?
    h.participant_id = uid
    h.status = 'matched'
    db.session.commit()

    print(uid, ' take hangout:', h.id)
    return jsonify({'status': 'take succeed'})

# 3.1 the author accepts a matched handout


@ app.route('/auth/accept', methods=['POST'])
def accept():
    if 'user_id' not in session:
        return jsonify({'error': 'not logged in'})

    if request.json == None or not all([x in request.json for x in ['hid']]):
        return jsonify({'error': 'missing info'})

    uid = session['user_id']
    hid = request.json['hid']
    h = Hangout.query.filter_by(id=hid).first()

    if h == None:
        return jsonify({'error': 'no hangout found'})

    if h.status != 'matched' or h.author_id != uid:
        return jsonify({'error': 'this hangout cannot be accepted'})

    h.status = 'finalized'
    db.session.commit()
    print(uid, ' accept hangout:', h.id)
    return jsonify({'status': 'accept succeed'})

# 3.2 the author declines a matched handout


@ app.route('/auth/decline', methods=['POST'])
def decline():
    if 'user_id' not in session:
        return jsonify({'error': 'not logged in'})

    if request.json == None or not all([x in request.json for x in ['hid']]):
        return jsonify({'error': 'missing info'})

    uid = session['user_id']
    hid = request.json['hid']
    h = Hangout.query.filter_by(id=hid).first()

    if h == None:
        return jsonify({'error': 'no hangout found'})

    if h.status != 'matched' or h.author_id != uid:
        return jsonify({'error': 'this hangout cannot be declined'})

    h.status = 'finished'
    db.session.commit()
    print(uid, ' decline hangout:', h.id)
    return jsonify({'status': 'decline succeed'})

# 4 refresh the whole hangout database by a time, changing some 'finalized' to 'finished'
# @app.route('/auth/finish')
# def finish():
