from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email


class LoginForm(FlaskForm):
    username = StringField("username",validators=[DataRequired()])
    password = PasswordField("password",validators=[DataRequired()])
    remember_me = BooleanField("remember_me")


class SignupForm(FlaskForm):
    name = StringField("name", validators=[DataRequired()])
    username = StringField("username", validators=[DataRequired()])
    email = StringField("email", validators=[DataRequired(), Email()])
    password = PasswordField("password",validators=[DataRequired()])
