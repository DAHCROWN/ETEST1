from flask import Flask,render_template,jsonify,request, redirect, url_for, session
from examination.exam1 import exam_list
from werkzeug.utils import redirect
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token, get_jwt_identity
)

app = Flask(__name__)
jwt = JWTManager(app)
app.config['SECRET_KEY'] = 'random'
app.config['JWT_SECRET_KEY'] = "b'j\x98\xcc\x088\xe9m3\xe1\xde&\x850\xaf\xcb\x19"
app.config['JWT_HEADER_NAME'] = "Authorization"
app.config['JWT_HEADER_TYPE'] = "Bearer"
app.config['JWT_TOKEN_LOCATION'] = ['headers', 'query_string']




@app.route('/', methods = ['GET', 'POST'])
def index():
    headers = request.headers
    if request.method == 'POST':
        username = request.form['username']
        otp = request.form['otp']
        session['username'] = request.form['username']
        if request.form['otp'] == 'test':
            session['username'] = request.form['username']
            access_token = create_access_token(identity={"user_id": username})
            return redirect(url_for('courses')), {"access_token": access_token}
        else:
            return render_template('index.html', error = "PLEASE ENTER VALID LOGIN DETAILS")
            
    return render_template('index.html')

@app.route('/courses')
@jwt_required()
def courses():
    user = get_jwt_identity()
    return render_template('course_pg.html', user=user)

@app.route('/admin')
def forbid():
    redirect(url_for('index'))

@app.route('/instructions/<string:exam_id>', methods =['POST', 'GET'])
@jwt_required()
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
@jwt_required()
def exam(exam_id):
    return render_template('test.html', exam_id=exam_id)

from examination import exam1
app.register_blueprint(exam1.bp)

if "__name__" == "__main__":
    app.run(debug=True)

