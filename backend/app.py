from flask import Flask, request, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from config import CONFIG

app = Flask(__name__, static_url_path='', static_folder='../build',)
app.config['SQLALCHEMY_DATABASE_URI'] = CONFIG['db_url']
app.secret_key = CONFIG['secret']
db = SQLAlchemy(app)


class User(db.Model):
  # identity info
  id = db.Column(db.Integer, primary_key=True)
  password = db.Column(db.String(500), nullable=False)
  
  # personal info
  name = db.Column(db.String(500), nullable=False)
  college = db.Column(db.String(500), nullable=False)
  department = db.Column(db.String(500), nullable=False)
  email = db.Column(db.String(500), nullable=False)
  year = db.Column(db.Integer, nullable=False)
  phone_number = db.Column(db.String(500), nullable=False)
  gender = db.Column(db.String(500), nullable=False)
  pronouns = db.Column(db.String(500), nullable=False)
  description = db.Column(db.String(500), nullable=False)

  def __repr__(self):
    return '<User %r>' % self.name

class Hangout(db.Model):
  #identity
  id = db.Column(db.Integer, primary_key=True)

  #status
  status = db.Column(db.String(500), nullable=False) #available, matched, finalized, finished

  #users
  author_id = db.Column(db.Integer, nullable=False)
  accepter_id = db.Column(db.Integer, nullable=True)


# IMPORTANT: SINGLE CHOICE
  #hard condition
  cond_name = db.Column(db.String(500), nullable=False) # *
  cond_college = db.Column(db.String(500), nullable=False) # *
  cond_department = db.Column(db.String(500), nullable=False) # *
  cond_year = db.Column(db.Integer, nullable=False) # 0
  cond_gender = db.Column(db.String(500), nullable=False) # *

  #soft condition
  activity = db.Column(db.String(500), nullable=False)
  time = db.Column(db.String(500), nullable=False)
  location = db.Column(db.String(500), nullable=False)
  
  def __repr__(self):
    return '<Hangout %r %r %r>' % (self.time, self.activity, self.location)

db.create_all()

@app.route('/')
def entry():
  return send_from_directory('../build', './index.html')

# @app.route('/<path:path>')
# def send_files(path):
#   return send_from_directory('../static', path)

import routes.auth

if __name__ == "__main__":
  app.run(port = 8000, debug=True)
