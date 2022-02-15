from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import scoped_session, sessionmaker
from flask_login import LoginManager,login_user,login_required,logout_user,current_user
from werkzeug.security import check_password_hash,generate_password_hash
from flask_bootstrap import Bootstrap
from app.config import  DevConfig
from flask_migrate import Migrate



#create an instance of my app
app= Flask(__name__)
db =SQLAlchemy(app)
bootstrap = Bootstrap(app)
migrate= Migrate(app,db)


login_manager=LoginManager(app)
login_manager.login_view = "login"


#specify my db environment

app.config['SECRET_KEY']='LILIAN'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI']

# create my sqlAlchemy instance
app.config.from_object(DevConfig)

#create auth instance

from app import views









