from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField, IntegerField,SubmitField,SelectField,TextAreaField
from wtforms.validators import ValidationError, DataRequired,InputRequired,Length,Email,ValidationError,EqualTo

class LogInForm(FlaskForm):
    username = StringField('username',validators=[InputRequired(),Length(min=5,max=15)])
    password =PasswordField('password',validators=[InputRequired(),Length(min=5 , max=8)])
    submit = SubmitField('Log In')
   
    
class SignupForm(FlaskForm):
    firstname = StringField(' first name',validators=[InputRequired(),Length(min=5 , max=25)])
    lastname = StringField('last name',validators=[InputRequired(),Length(min=5 , max=25)])
    username = StringField('username',validators=[InputRequired(),Length(min=5 ,max=25)])
    email= StringField('email',validators=[InputRequired(),Email(message ='invalid email'),Length(min=8 ,max=25)])
    password =PasswordField('password',validators=[InputRequired(),Length(min=5 , max=8)])
    # confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo('password')])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Sign Up')
    
class PitchesForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired()])
    category = SelectField('Pitch Category', choices=[('',''),('Sales','Sales'),('Interview','Interview'),
    ('Elevator','Elevator'),('Promotion','Promotion'),('Personal','Personal'),
    ('Pickup-lines','Pickup-lines')],validators=[InputRequired()])
    post = TextAreaField('Pitch', validators=[InputRequired()])
    submit = SubmitField('Post Pitch')
    
class CommentsForm(FlaskForm):
    comment = TextAreaField('Comment', validators=[InputRequired()])
    submit = SubmitField('Comment')
    