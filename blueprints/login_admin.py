from flask import Blueprint, render_template, request, redirect, flash, url_for
from models.user_admin import User 
from werkzeug.utils import secure_filename
import os
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from extensions import db , login_manager

regis_blueprint = Blueprint('regis_blueprint', __name__)

@login_manager.user_loader 
def load_user(user_id):
    return User.query.get(int(user_id))  

@regis_blueprint.route('/login_admin')
def login():
    return render_template('login.html')

@regis_blueprint.route('/login', methods=['POST'])
def login_post():
    # login code goes here
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login')) # if the user doesn't exist or password is wrong, reload the page
    login_user(user, remember=remember)
    # if the above check passes, then we know the user has the right credentials
    return redirect(url_for('admin_blueprint.admin'))

@regis_blueprint.route('/logout_admin')
@login_required
def logout():
    logout_user()
    return redirect(url_for('regis_blueprint.login'))

@regis_blueprint.route('/signup_admin')
def signup():
    return render_template('signup.html')

@regis_blueprint.route('/signup', methods=['POST'])
def signup_post():
    # code to validate and add user to database goes here

    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database

    if user: # if a user is found, we want to redirect back to signup page so user can try again
         flash('     address already exists')

    # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for('regis_blueprint.profile'))


@regis_blueprint.route('/profile_admin')
def profile():
    return render_template('profile.html')

@regis_blueprint.route('/Admin')
def index():
    return render_template('index_admin.html')