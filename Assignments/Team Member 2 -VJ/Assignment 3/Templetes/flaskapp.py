# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 11:52:08 2022

@author: O
"""

from flask import *

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/signin')
def sigin():
    return render_template('signin.html')

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)