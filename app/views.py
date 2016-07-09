from flask import render_template
from app import app
from .forms import LoginForm

# index view function suppressed for brevity

@app.route('/login', methods=['GET', 'POST'])
# @app.route('/')
# @app.route('/index')
# def index():
# 	return "Hello World!"



def login():
	form = LoginForm()
	return render_template('login.html',
		title='Sign In',
		form=form)