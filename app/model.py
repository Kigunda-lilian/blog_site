from unicodedata import category
from . import db, login_manager
from datetime import datetime
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))

class User(db.Model,UserMixin):
    ___tablename__='user'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    firstname = db.Column(db.String(),nullable=False)
    lastname = db.Column(db.String(),nullable=False)
    username = db.Column(db.String(),nullable=False)
    email = db.Column(db.String(),nullable=False)
    password = db.Column(db.String(),nullable=False)
    posts = db.relationship('Post', backref='user', lazy='dynamic')
    comments = db.relationship('Comments', backref='post', lazy='dynamic')


class Comments(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.Text, nullable=False,)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))

class Quotes(db.Model):
    __tablename__ = 'quotes'

    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(),nullable=False)
    quote = db.Column(db.String(),nullable=False)
    
    
class Post(db.Model):
    ___tablename__='posts'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(),nullable=False)
    post = db.Column (db.String(),default=0, nullable=False)
    created_at = db.Column (db.DateTime(),default=datetime.utcnow,nullable=False)
    category= db.Column (db.String(),default=0, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    comments = db.relationship('Comments', backref='post', lazy='dynamic')
    def save_post(self):
        db.session.add(self)
        db.session.commit()
    

       

