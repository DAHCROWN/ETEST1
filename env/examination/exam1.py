import functools
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
bp = Blueprint('exam', __name__, url_prefix='/exam')

@bp.route('/<string:exam_id>')
def fetch_exam(exam_id):
    if session['logged_in'] == True:
        if exam_id == 'MAT111':
            return redirect(url_for('exam.mat111', question=0))
        if exam_id == 'MAT112':
            return redirect(url_for('exam.mat112', question=0))
        if exam_id == 'CHM111':
            return redirect(url_for('exam.chm111', question=0))
        else:
            return redirect(url_for('exam.mat111', question=1))
    else:
        return redirect(url_for('index'))


@bp.route('/exams/mat111/<int:question>')
def mat111(question):
    if session['logged_in'] == True and session['exam_chosen'] == 'MAT111':
    
        exam = [{
            'EXAM': 'MAT111',
            'question': 'This is the first question',
            'optiona': 'This',
            'optionb': 'That',
            'optionc': 'The other',
            'optiond': 'correct',
            'answer': 'Correct'},

            {'EXAM': 'MAT111',
            'question': 'This is the second question',
            'optiona': 'This',
            'optionb': 'That',
            'optionc': 'The other',
            'optiond': 'Correct',
            'answer': 'correct'
        }]
        examination = exam[question]
        return render_template('test.html', q_id=examination)
    else:
        return redirect(url_for('index'))

@bp.route('/exams/mat112/<int:question>')
def mat112(question):
    if session['logged_in'] == True and session['exam_chosen'] == 'MAT112':
        exam = [{
            'EXAM': 'MAT112',
            'question': 'This is the first question',
            'optiona': 'This',
            'optionb': 'That',
            'optionc': 'The other',
            'optiond': 'correct',
            'answer': 'Correct'},
        {   'EXAM': 'MAT112',
            'question': 'This is the second question',
            'optiona': 'This',
            'optionb': 'That',
            'optionc': 'The other',
            'optiond': 'Correct',
            'answer': 'correct'
        }]
        examination = exam[question]
        return render_template('test.html', q_id=examination)
    else:
        return redirect(url_for('index'))

@bp.route('/exams/chm111/<int:question>')
def chm111(question):
    if session['logged_in'] == True and session['exam_chosen'] == 'CHM111':
        exam = [{
            'EXAM': 'CHM111',
            'question': 'This is the first question',
            'optiona': 'This',
            'optionb': 'That',
            'optionc': 'The other',
            'optiond': 'correct',
            'answer': 'Correct'},
        {   'EXAM': 'CHM111',
            'question': 'This is the second question',
            'optiona': 'This',
            'optionb': 'That',
            'optionc': 'The other',
            'optiond': 'Correct',
            'answer': 'correct'
        }]
        examination = exam[question]
        return render_template('test.html', q_id=examination)
    else:
        return redirect(url_for('index'))

@bp.route('/logout')
def logout():
    session.pop('username', None)
    session['logged_in'] = False
    session.clear()
    return redirect(url_for('index'))