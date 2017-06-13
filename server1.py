#!/usr/bin/env python
# coding=utf-8
import time
from hashlib import md5
from datetime import datetime
from flask import Flask, request, session, url_for, redirect, \
	 render_template, abort, g, flash, _app_ctx_stack
from werkzeug import check_password_hash, generate_password_hash
import time
from book_dao import *
import sys

reload(sys)  
sys.setdefaultencoding('utf8')

app = Flask(__name__)

app.config.from_object(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)



@app.route('/')
def index():
    return render_template('login.html')

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        user_name = request.form['username']
        password = request.form['password']
        #session['user_id'] = app.config['MANAGER_NAME']

        user = query_user(user_name,password)
        if user and user['role']==0:
            return redirect(url_for('manager'))
        else:
            error = '用户名或者密码错误'
            return render_template('login.html', error = error)
@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
        if not request.form['username']:
            error = 'You have to enter a username' 
        elif not request.form['password']:
            error = 'You have to enter a password'
        elif request.form['password'] != request.form['password2']:
            error = 'The two passwords do not match'
        elif get_user_id(request.form['username']) is not None:
             error = 'The username is already taken'
        else:
            #pass
            sql="""insert into users (user_name, password, college, num, email) values ({}, {}, {}, {}, {})""".format(request.form['username'], generate_password_hash(request.form['password']), request.form['college'], request.form['number'],request.form['email'])
            #db_update(sql)
            #return redirect(url_for('login'))
        return render_template('register.html', error = error)

if __name__ == '__main__':
	
    app.run(host='0.0.0.0',port=80,threaded=True,debug=True)
    #app.run(debug=True)

