from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired, EqualTo

class LoginForm(FlaskForm):
	username = StringField("username", validators=[DataRequired()])
	password = PasswordField("password", validators=[DataRequired()])
	remember_me = BooleanField("remember_me")

class CadForm(FlaskForm):
	username = StringField("username", validators=[DataRequired()])
	password = PasswordField("password", validators=[DataRequired(), EqualTo('re_password', message='Passwords must match')])
	re_password = PasswordField("re_password", validators=[DataRequired()])
