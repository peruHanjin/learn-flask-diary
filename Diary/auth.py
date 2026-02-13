from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/sign-up')
def sign_up():
    return '<h1>sign-up<h1>'

@auth.route('/logout')
def logout():
    return '<h1>logout<h1>'

@auth.route('/sign-in')
def sign_in():
    return '<h1>sign-in<h1>'