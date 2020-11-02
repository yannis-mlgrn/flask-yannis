#!/usr/bin/env python
# encoding: utf-8
from flask import *
import flask_login
from flask_login import LoginManager, login_required, logout_user, current_user,login_user
import os

login_manager = LoginManager()

app = Flask(__name__)

login_manager.init_app(app)

#user loader
@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

#index
@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('login.html')


@app.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'admin' and request.form['username'] == 'admin':
        session['logged_in'] = True
        user = current_user
        user.authenticated = True
        login_user(user)
        return render_template('dashboard.html')
    else:
        flash('wrong password!')
        return home()

@app.route("/logout")
def logout():
    logout_user()
    return redirect("/")

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(host='0.0.0.0',port='5000', debug=True)