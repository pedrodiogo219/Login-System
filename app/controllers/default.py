from flask import render_template, flash, redirect, url_for
from flask_login import login_user, logout_user
from app import app, db, lm

from app.models.tables import User, Post
from app.models.forms import LoginForm, SignupForm



@lm.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first()


@app.route("/index")
@app.route("/")
def index():
    post = Post.query.all()
    #select a.content, b.username
    #from posts a
    #inner join users b on b.id = a.user_id
    return render_template('index.html', post=post)


@app.route("/teste/", defaults={'info': "Jorge"})
@app.route("/teste/<info>")
def teste(info):
    r = User.query.filter_by(username="outronomeaí").first()
    db.session.delete(r)
    db.session.commit()
    return "Ok"

@app.route("/signup", methods=["GET", "POST"])
def signup():
    form_signup = SignupForm()
    if form_signup.validate_on_submit():

        existing_user = User.query.filter_by(username=form_signup.username.data).first()
        existing_email = User.query.filter_by(email=form_signup.email.data).first()

        if existing_user or existing_email:
            if existing_user:
                flash("This username already exists")
            if existing_email:
                flash("This email address is already registered")
        else:
            new_user = User(form_signup.username.data, form_signup.password.data, form_signup.email.data, form_signup.name.data)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            flash("Logged in.")
            return redirect(url_for("index"))
    else:
        print(form_signup.errors)
    return render_template('signup.html', form_signup=form_signup)

@app.route("/login", methods=["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            flash("Logged in.")
            return redirect(url_for("index"))

        else:
            flash("Invalid login.")

    return render_template('login.html', form=form)

@app.route("/logout")
def logout():
    logout_user()
    flash("Logged out.")
    return redirect(url_for("index"))
