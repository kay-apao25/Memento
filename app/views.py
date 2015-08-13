from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    #user = {'nickname': 'Miguel'}  # fake user
    return render_template('index.html',
                           title='Home')
                           #, user=user)


@app.route('/login')
def login():
    return render_template('login.html', 
                           title='Sign In')
                           #, form=form)