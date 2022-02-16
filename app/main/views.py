from .forms import LogInForm,SignupForm,QuotesForm,CommentsForm
from flask import redirect, render_template ,request, url_for
from .. import db
from ..model import User
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import login_required,logout_user,login_user,current_user
from . import main
from ..request import fetch_quotes


@main.route("/")
#view function

def index():
    
    
    Blogs=fetch_quotes()
   
    
    return render_template ('index.html',articles=Blogs)


#login
@main.route('/login',methods = ["GET","POST"])
def login():
    
    form=LogInForm()
    
    #check for validation
    if form.validate_on_submit():
        user=User.query.filter_by(username=form.username.data).first()
        
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            next_page = request.args.get('next') 
            return redirect(next_page) if next_page else redirect(url_for('main.comments'))  
              
        print("Invalid username or password")
        print("Invalid username or password")
       
    return render_template("login.html",registration_form=form)


#signup
@main.route('/signup',methods = ["GET","POST"])
def signup():
    
    form = SignupForm()
    
    if form.validate_on_submit():
        user=User(firstname = form.firstname.data,
        lastname = form.lastname.data,
        username = form.username.data,
        email= form.email.data,
        password =generate_password_hash(form.password.data))
        
        
        #send data to db
        db.session.add(user)
        db.session.commit()
        print("User has been added successfully")
        print(user.username)
        print(user.password)
        
        return redirect (url_for('main.login'))
    
    return render_template("signup.html",registerform=form)


#logout
@main.route('/logout')
def logout():
    return redirect (url_for('home'))

# #comments
@main.route('/comments',methods = ["GET","POST"])
@login_required
def comments():
    
    form = CommentsForm()
    
    return render_template("comments.html",feedbackform=form,name=current_user.username)




