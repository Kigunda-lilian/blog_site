from .forms import LogInForm,SignupForm,PostForm,CommentsForm
from flask import redirect, render_template ,request, url_for
from .. import db
from ..model import Comments, User,Post
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import login_required,logout_user,login_user,current_user
from . import main
from ..request import fetch_quotes

@main.route('/post/<id>', methods=['GET', 'POST'])
@login_required
def post(id):

    post_form = PostForm()
    if post_form.validate_on_submit():
        title = post_form.title.data
        category = post_form.category.data
        post = post_form.post.data

        new_pitch = Post(title=title, category=category, post=post, user=current_user)

        new_pitch.save_post()
        return redirect(url_for('.index'))

    return render_template('post.html', post_form=post_form)

    
@main.route("/")
#view function

def index():
    
    
    Blogs=fetch_quotes()
    post=Post.query.all()
    
    return render_template ('index.html',articles=Blogs,posts=post)


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
            return redirect(next_page) if next_page else redirect(url_for('main.index'))  
              
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
@login_required
def logout():
    """Logout function"""
    logout_user()
    return redirect(url_for('main.index'))


# #comments
@main.route('/comment/<id>', methods=['GET', 'POST'])
@login_required
def comments(id):
    comment_form = CommentsForm()
    post = Post.query.get(id)
    comments = Comments.query.filter_by(post_id=id).all()
    if comment_form.validate_on_submit():
        comment = comment_form.comment.data
        post_id = id
        user_id = current_user._get_current_object().id
        new_comment = Comments(comment=comment, user_id=user_id, post_id=post_id)
        new_comment.save_comment()
        return redirect(url_for('.comment', id=post_id))
    return render_template('comments.html', comment_form=comment_form, post=post, all_comments=comments)



