import requests
from flask import render_template, url_for, flash, redirect, request, jsonify
from . import create_app
from .forms import RegistrationForm, LoginForm
from flask_login import login_user, current_user, logout_user, login_required

app = create_app()

API_URL = "https://login-signup.p.rapidapi.com"
API_HEADERS = {
    'x-rapidapi-key': "your_rapidapi_key_here",
    'x-rapidapi-host': "login-signup.p.rapidapi.com"
}

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        payload = {
            "api_key": "your_api_key_here",
            "email": form.email.data,
            "password": form.password.data
        }
        response = requests.post(f"{API_URL}/public/v1/register.php", data=payload, headers=API_HEADERS)
        if response.status_code == 200:
            flash('Your account has been created! You are now able to log in', 'success')
            return redirect(url_for('login'))
        else:
            flash('Registration Unsuccessful. Please try again.', 'danger')
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        payload = {
            "api_key": "your_api_key_here",
            "email": form.email.data,
            "password": form.password.data
        }
        response = requests.post(f"{API_URL}/public/v1/login.php", data=payload, headers=API_HEADERS)
        if response.status_code == 200:
            data = response.json()
            # Here you should handle the login_user logic
            # Example:
            # user = User.query.filter_by(email=form.email.data).first()
            # login_user(user, remember=form.remember.data)
            flash('Login Successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))
