from flask import Flask, json,render_template,jsonify,request, redirect, url_for, session
from examination.exam1 import exam_list
from flask.helpers import make_response
from werkzeug import wrappers
from werkzeug.utils import redirect
import jwt
from datetime import datetime, timedelta
from werkzeug.wrappers import response
from functools import wraps

app = Flask(__name__)
app.config['SECRET_KEY'] = '9748547c-edca-48cc-8ccb-1e8b6c3b0b09'

@app.route('/', methods = [ 'GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form['otp'] == 'test':
            username = request.form['username']
            otp = request.form['otp']
            session['username'] = request.form['username']
            session['logged_in'] = True
            return redirect(url_for('courses'))
        else:
            return render_template('index.html', error = "PLEASE ENTER VALID LOGIN DETAILS")
            
    return render_template('index.html')

@app.route('/courses')

def courses():
    if session['logged_in'] == True:
        return render_template('course_pg.html')
    else:
        return redirect(url_for('index'))

@app.route('/instructions/<string:exam_id>', methods =['POST', 'GET'])

def instructions(exam_id):
    if session['logged_in'] == True:
        exam_ids= {'1': 'MAT111',
                    '2': 'MAT112',
                    '3': 'CHM111',
                    '4': 'CHM112',
                    '5': 'CPT111',
                    '6': 'PHY113'}
        for this in exam_ids: 
            if this == exam_id:
                    if request.method == 'POST':
                        return redirect(url_for('exam', exam_id=exam_ids[this])) 
                    else:
                        return render_template('instruction.html', exam=exam_ids[this])
    else:
        return redirect(url_for('index'))

@app.route('/exams/<string:exam_id>')
def exam(exam_id):
    if session['logged_in'] == True:
        return render_template('test.html', exam_id=exam_id)
    else:
        return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    session['logged_in'] = False
    return redirect(url_for('index'))
    
from examination import exam1
app.register_blueprint(exam1.bp)

if "__name__" == "__main__":
    app.run(debug=True)