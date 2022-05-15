from flask import Flask
from flask import render_template
from flask import request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from datetime import datetime

from faceflask.blog_action import face
import pymysql

conn = pymysql.connect(
    host='localhost', user='root', password='wywftxsgc92', database='Login'
)

cursor = conn.cursor()

app = Flask(__name__)

sql = 'select login_name from loginNamePass'
row1 = cursor.execute(sql)
result1 = cursor.fetchone()
name = ''.join(list(result1)[0])

sql = 'select login_password from loginNamePass'
row2 = cursor.execute(sql)
result2 = cursor.fetchone()
password = ''.join(list(result2)[0])


user = {'username': name,
        'password': password}


@app.route('/')
def index():
    return render_template('/login.html')


@app.route("/blog", methods=['GET', 'POST'])
def login1():
    if request.method == 'POST':
        password = request.form['password']
        if user['password'] == password:
            return render_template('/myblog.html', title='我的', user=user)
        else:
            return render_template('/fail.html')


@app.route("/myblog", methods=['GET', 'POST'])
def blog_action():
    ff1 = request.form["being_changed"]
    ff2 = request.form["to_change"]
    face(ff1, ff2)
    return render_template('/complete.html')


if __name__ == '__main__':
    app.run(debug=True)
