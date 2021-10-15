from flask import Flask,render_template,jsonify,request, redirect, url_for, session
from examination.exam1 import exam_list
import flask
from flask.helpers import make_response
from werkzeug.utils import redirect
from werkzeug.wrappers import response

app = Flask(__name__)
app.config['SECRET_KEY'] = 'random'
app.config['JWT_SECRET_KEY'] = "b'j\x98\xcc\x088\xe9m3\xe1\xde&\x850\xaf\xcb\x19"

def logged_in():
        return redirect(url_for('index'))

@app.route('/', methods = ['GET', 'POST'])
def index():
    session['username'] = ''
    if request.method == 'POST':
        username = request.form['username']
        otp = request.form['otp']
        session['username'] = request.form['username']
        if request.form['otp'] == 'test':
            session['username'] = username
            return redirect(url_for('courses'))
        else:
            return render_template('index.html', error = "PLEASE ENTER VALID LOGIN DETAILS")
            
    return render_template('index.html')

@app.route('/courses')
def courses():
    if session['username'] == '':
        return redirect(url_for('index'))       
    else:
        return render_template('course_pg.html')

@app.route('/admin')
def forbid():
    redirect(url_for('index'))

@app.route('/instructions/<string:exam_id>', methods =['POST', 'GET'])
def instructions(exam_id):

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


@app.route('/exams/<string:exam_id>')
def exam(exam_id):
    return render_template('test.html', exam_id=exam_id)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))
    
from examination import exam1
app.register_blueprint(exam1.bp)

if "__name__" == "__main__":
    app.run(debug=True)