from unicodedata import category
from app import db
from datetime import datetime
from flask_login import UserMixin
from flask_login import login_manager
from app import login_manager


@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))

class User(db.Model,UserMixin,):
    ___tablename__='user'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    firstname = db.Column(db.String(),nullable=False)
    lastname = db.Column(db.String(),nullable=False)
    username = db.Column(db.String(),nullable=False)
    email = db.Column(db.String(),nullable=False)
    password = db.Column(db.String(),nullable=False)

class Comments(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.Text, nullable=False,)

class Quote(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(),nullable=False)
    post = db.Column (db.String(),default=0, nullable=False)
    created_at = db.Column (db.DateTime(),default=datetime.utcnow,nullable=False)
    comments = db.relationship('Comments', backref='comment_Quote', lazy=True)

