from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, ValidationError
from wtforms.validators import DataRequired, EqualTo, Email

class LoginForm(FlaskForm):
	email = StringField("email", validators=[DataRequired(), Email()])
	senha = PasswordField("senha", validators=[DataRequired()])


class CadForm(FlaskForm):
	nome = StringField("nome", validators=[DataRequired()])
	telefonefixo = StringField("telefonefixo", validators=[])
	celular = StringField("celular", validators=[])
	email = StringField("email", validators=[DataRequired(), Email()])
	senha = PasswordField("senha", validators=[DataRequired(), EqualTo('confirmasenha', message='As senhas não batem')])
	confirmasenha = PasswordField("confirmasenha", validators=[DataRequired()])
	assinante = BooleanField("assinante")


class AltForm(FlaskForm):
	codpessoa = StringField("codpessoa", validators=[DataRequired()])
	nome = StringField("nome", validators=[DataRequired()])
	telefonefixo = StringField("telefonefixo", validators=[])
	telefonecel = StringField("celular", validators=[])
	email = StringField("email", validators=[DataRequired(), Email()])
	senha = PasswordField("senha", validators=[DataRequired(), EqualTo('confirmasenha', message='As senhas não batem')])
	confirmasenha = PasswordField("confirmasenha", validators=[DataRequired()])
	assinante = BooleanField("assinante")


