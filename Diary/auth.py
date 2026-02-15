from flask import Blueprint, render_template

# Creat Blueprint
auth = Blueprint('auth', __name__)

# route
@auth.route('/sign-up')
def sign_up():
    return render_template('sign_up.html')

@auth.route('/logout')
def logout():
    return render_template('logout.html')

# login
@auth.route('/sign-in')
def sign_in():
    return render_template('sign_in.html', user = "SemiCircle")