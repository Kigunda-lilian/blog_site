from . import db, login_manager
from datetime import datetime
from flask_login import UserMixin


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

class Quotes(db.Model):
    __tablename__ = 'quotes'

    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(),nullable=False)
    quote = db.Column(db.String(),nullable=False)

       

