import functools
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
bp = Blueprint('examination', __name__, url_prefix='/examination')


answers = []


@bp.route('/exam1/<int:q_id>', methods=['GET', 'POST'])
def query_questions(q_id):
    if request.method == 'POST':
        answer = request.form['answer']
        return jsonify({'answer': answer}), 201
    return render_template('test.html', exam = exam_list[q_id])     

@bp.route('/questions/<int:q_id>')
def question(q_id):
    return jsonify(exam_list[q_id])    
exam_list = [
    {
        'question': 'this is the first question',
        'a': 'This',
        'b': 'That',
        'c': 'the other',
        'd': 'correct',
        'answer': 'correct'
    },
     {
        'question': 'this is the second question',
        'a': 'This',
        'b': 'That',
        'c': 'the other',
        'd': 'correct',
        'answer': 'correct'
    }
]