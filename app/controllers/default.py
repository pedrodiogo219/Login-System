from flask import render_template, flash, redirect, url_for
#from flask_login import login_user, logout_user
from app import app, db, lm, conn

from app.models.forms import LoginForm, CadForm
#from app.models.tables import User

from sqlalchemy.sql import select, insert, and_, or_, not_



"""
@lm.user_loader
def load_user(id):
	return User.query.filter_by(id=id).first()

"""

@app.route("/index")
@app.route("/")
def index():
	return render_template('index.html')

"""
@app.route("/login", methods=["GET","POST"])
def login():
	form = LoginForm()
	if form and form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user:
			if user.password == form.password.data:
				login_user(user)
				flash("Logged in.")
				return redirect(url_for("index"))
			else:
				flash("Wrong password.")
		else:
			flash("Invalid user.")

	return render_template('login.html', form=form)

"""

"""
@app.route("/logout")
def logout():
	logout_user()
	flash("Logged out.")
	return redirect(url_for("index"))

"""


# noinspection PyInterpreter
"""
@app.route("/register", methods=["GET", "POST"])
def register():
	form = CadForm()
	if form.validate_on_submit():
		if form.password.data == form.re_password.data:
			s = select([User]).where(or_(User.username==form.username.data, User.email==form.email.data)).limit(1)
			result = conn.execute(s)

			is_unique = True
			for row in result:
				is_unique = False
				break

			if not is_unique:
				flash("This is user is already registered.")
			else:
				stmt = insert(User).values(username=form.username.data, email=form.email.data,
									   password=form.password.data, name=form.username.data)
				conn.execute(stmt)
				flash("Successfully registered! Please log in, now.")
				return redirect(url_for('login'))
		else:
			flash("The password don't match.")



	return render_template('register.html', form=form)
"""
