from .forms import LogInForm,SignupForm,PostForm,CommentsForm
from flask import redirect, render_template ,request, url_for
from .. import db
from ..model import Comment, User,Post
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
        content = post_form.post.data

        new_post = Post(title=title, category=category, content=content, user=current_user)

        new_post.save_post()
        return redirect(url_for('.show'))

    return render_template('post.html', post_form=post_form)

    
@main.route("/")
#view function

def index():
    
    
    Blogs=fetch_quotes()
    post=Post.query.all()
    
    return render_template ('index.html',articles=Blogs,posts=post)

@main.route("/show")
#view function

def show():
    
    
    Blogs=fetch_quotes()
    post=Post.query.all()
    
    return render_template ('show.html',articles=Blogs,posts=post)

@main.route('/post/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):

    data = Post.query.get(id)
    if request.method == 'POST':
        data.title = request.form['title']
        data.category = request.form['category']
        data.content = request.form['content']
        db.session.commit()
        return redirect(url_for(".show"))

    return render_template("edit.html", data=data)


#login
@main.route('/login',methods = ["GET","POST"])
def login():
    login_form = LogInForm()
    if login_form.validate_on_submit():
        user=User.query.filter_by(email=login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user,login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))


    return render_template('login.html', registration_form=login_form)


#signup
@main.route('/signup',methods = ["GET","POST"])
def signup():
    reg_form = SignupForm()
    if reg_form.validate_on_submit():
        user=User(username=reg_form.username.data,email=reg_form.email.data,password=reg_form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('main.login'))

    return render_template('signup.html', registerform=reg_form)


#logout
@main.route('/logout')
@login_required
def logout():
    """Logout function"""
    logout_user()
    return redirect(url_for('main.index'))


# #commentdds
@main.route('/comment/<id>', methods=['GET', 'POST'])
@login_required
def comments(id):
    comment_form = CommentsForm()
    post = Post.query.get(id)
    comments = Comment.query.filter_by(post_id=id).all()
    if comment_form.validate_on_submit():
        comment = comment_form.comment.data
        post_id = id
        user_id = current_user._get_current_object().id
        new_comment = Comment(comment=comment, user_id=user_id, post_id=post_id)
        new_comment.save_comment()
        return redirect(url_for('.comments', id=post_id))
    return render_template('comments.html', comment_form=comment_form, post=post, all_comments=comments)


@main.route('/delete/<id>', methods=["GET", "POST"])
def delete(id):
    data = Post.query.get(id)
    db.session.delete(data)
    db.session.commit()
    return redirect(url_for(".show"))

