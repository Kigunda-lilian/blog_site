# from pyexpat import model
# from unicodedata import category
from app.forms import LogInForm,SignupForm,PitchesForm,CommentsForm,UpdateProfileForm
from flask import redirect, render_template ,request, url_for
from app import app,db
# from app.model.model import User,Pitches
from app.forms import LogInForm,SignupForm
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import login_required,logout_user,login_user,current_user



@app.route("/")
#view function
def home():
   db.create_all()
   return render_template('index.html')


#login
@app.route('/login',methods = ["GET","POST"])
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
            return redirect(next_page) if next_page else redirect(url_for('home'))  
              
        print("Invalid username or password")
        print("Invalid username or password")
       
    return render_template("login.html",registration_form=form)


#signup
@app.route('/signup',methods = ["GET","POST"])
def signup():
    
    form = SignupForm()
    
    if form.validate_on_submit():
        user=User(firstname = form.firstname.data,
        lastname = form.lastname.data,
        username = form.username.data,
        email= form.email.data,
        password =generate_password_hash(form.password.data))
        # confirm_password = form.confirm_password.data
        # remember_me = form.remember_me.data
        # submit = form.submit.data
        
        # Hash password
        # hashed_password = generate_password_hash(password,method="sha256")
        
        # new_user=models.User(first_name = first_name,last_name=last_name,username=username,email=email,password=password)
        
        #send data to db
        db.session.add(user)
        db.session.commit()
        print("User has been added successfully")
        print(user.username)
        print(user.password)
        
        return redirect (url_for('login'))
    
    return render_template("signup.html",registerform=form)


#logout
@app.route('/logout')
def logout():
    return redirect (url_for('home'))

# #comments
@app.route('/comments',methods = ["GET","POST"])
@login_required
def comments():
    
    form = CommentsForm()
    
    return render_template("comments.html",feedbackform=form,name=current_user.username)


# # #pitches
# @app.route('/pitches',methods = ["GET","POST"])
# @login_required
# def pitches():
    
#     form = PitchesForm()
#     if form.validate_on_submit():
#         pitc=Pitches(
#             title=form.title.data,
#             category=form.category.data,
#             post=form.post.data
#             )
#         db.session.add(pitc)
#         db.session.commit()
        
#         print(pitc.post)
#         return redirect (url_for('home'))
    
    
#     return render_template("pitch.html",pitchform=form,name=current_user.username)