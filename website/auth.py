from flask import Blueprint, render_template,request
from flask.helpers import flash, url_for
from werkzeug.utils import redirect
from .models import User
from . import db
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)


@auth.route('/login',methods=['GET', 'POST'])
def login():
    reloaded_page = False
    if request.method == "POST":
        reloaded_page = True
        email =request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user == None:
            flash("User does not exist")
        else:
            if user.password == password:
                login_user(user, remember=True)
                return redirect('/notes')
            else:
                flash("Incorrect email/password")

    return render_template('login.html', user=current_user)

@auth.route('/signup' ,methods=['GET', 'POST'])
def signup():
    if request.method == "POST":
        email = request.form['email']
        fname = request.form['fname']
        lname = request.form['lname']
        password = request.form["password1"]
        con_password = request.form['password2']

        if len(email) < 3:
            flash("Email can not be less than 3 characters")
        elif len(password) < 7 or len(con_password) <7:
            flash("Password can not be less than 7 characters")
        elif password != con_password:
            flash("Password does not match")
        else:
            if User.query.filter_by(email=email).first() == None:
                new_user = User(email=email, fname=fname, lname=lname, password=password)
                db.session.add(new_user)
                db.session.commit()
                return "<h1>Account created</h1>"
            else:
                flash("Email already exits") 
    return render_template("signup.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


