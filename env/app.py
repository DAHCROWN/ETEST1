from flask import Flask,render_template,jsonify,request, redirect, url_for, session
from examination.exam1 import exam_list
from werkzeug.utils import redirect


app = Flask(__name__)
app.config['SECRET_KEY'] = 'random'


@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        otp = request.form['otp']
        session['username'] = request.form['username']
        if request.form['username'] == 'test':
            session['username'] = request.form['username']
            return redirect(url_for('courses'))
    return render_template('index.html')

@app.route('/courses')
def courses():
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
             return render_template('instruction.html', exam=exam_ids[this])
    request.method == 'POST'
        return redirect(url_for('exam', exam_id=exam)) 

@app.route('/exams/<string:exam_id>')
def exam(exam_id):
    return render_template('test.html', exam_id=exam_id)

from examination import exam1
app.register_blueprint(exam1.bp)

if "__name__" == "__main__":
    app.run(debug=True)

