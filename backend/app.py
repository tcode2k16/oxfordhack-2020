from flask import Flask, request, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from config import CONFIG

app = Flask(__name__, static_url_path='', static_folder='../static',)
app.config['SQLALCHEMY_DATABASE_URI'] = CONFIG['db_url']
app.secret_key = CONFIG['secret']
db = SQLAlchemy(app)


class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable=False)
  college = db.Column(db.String(100), nullable=False)
  department = db.Column(db.String(100), nullable=False)
  email = db.Column(db.String(100), nullable=False)
  year = db.Column(db.Integer, nullable=False)
  phone_number = db.Column(db.String(100), nullable=False)
  gender = db.Column(db.String(100), nullable=False)
  pronouns = db.Column(db.String(100), nullable=False)
  description = db.Column(db.String(500), nullable=False)
  password = db.Column(db.String(500), nullable=False)

  def __repr__(self):
    return '<User %r>' % self.name

class Task(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  time = db.Column(db.String(100), nullable=False)
  activity = db.Column(db.String(100), nullable=False)
  location = db.Column(db.String(100), nullable=False)
  
  author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
  author = db.relationship('User', backref=db.backref('tasks', lazy=True))
  
  def __repr__(self):
    return '<Task %r %r %r>' % (self.time, self.activity, self.location)


db.create_all()

@app.route('/')
def entry():
  return send_from_directory('../static', './index.html')


# @app.route('/<path:path>')
# def send_files(path):
#   return send_from_directory('../static', path)

import routes.auth

if __name__ == "__main__":
  app.run(debug=True)
