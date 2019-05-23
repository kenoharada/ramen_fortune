from flask import request, redirect, url_for, render_template, flash
from flaskr import app, db
from flaskr.models import Entry
import numpy as np

@app.route('/')
def show_entries():
    return render_template('show_entries.html')

@app.route('/answer', methods=['POST'])
def add_answer():
    id = 10
    q1=request.form['q1']
    q2=request.form['q2']
    q3=request.form['q3']
    q4=request.form['q4']
    q5=request.form['q5']
    q6=request.form['q6']
    q7=request.form['q7']
    q8=request.form['q8']
    q9=request.form['q9']
    q10=request.form['q10']

    entry = Entry(id=id,q1=q1,q2=q2,q3=q3,q4=q4,q5=q5,q6=q6,q7=q7,q8=q8,q9=q9,q10=q10)
    db.session.add(entry)
    #db.session.commit()

    x = np.array([int(q1),int(q2),int(q3),int(q4),int(q5),int(q6),int(q7),int(q8),int(q9),int(q10)])

    scores = {"np":x[0],"cp":x[1],"ac":x[2],"a":x[3],"fc":x[4]}
    
    result = {"result":algo_ego2(scores)}
    
    return jsonify(result)

def algo_ego2(scores):
    if (scores['np'] > scores['cp']) and (max(scores.values()) == scores['np']) and (min(scores.values()) == min([scores['cp'], scores['ac']])) and (scores['a'] >= scores['fc'] >= scores['ac']):
        ego = 1
    elif (min([scores['np'], scores['ac']]) >= scores['a']) and (max([scores['cp'], scores['fc']]) <= scores['a']):
        ego = 2
    elif (max([scores['np'], scores['ac']]) <= scores['a']) and (min([scores['cp'], scores['fc']]) >= scores['a']):
        ego = 3
    elif (min([scores['cp'], scores['ac']]) >= scores['np']) and (max([scores['a'], scores['fc']]) <= scores['np']):
        ego = 4
    elif min([scores['cp'], scores['a'], scores['ac']]) >=max([scores['np'], scores['fc']]):
        ego = 5
    elif min([scores['np'], scores['fc']]) >=max([scores['cp'], scores['a'], scores['ac']]):
        ego = 6
    elif (scores['a'] >= max([scores['np'], scores['fc']])) and (min([scores['np'], scores['fc']]) >= max([scores['cp'], scores['ac']])):
        ego = 7
    elif scores['cp'] >= scores['np'] >= scores['a'] >= scores['fc'] >= scores['ac']:
        ego = 8
    elif scores['cp'] <= scores['np'] <= scores['a'] <= scores['fc'] <= scores['ac']:
        ego = 9
    else:
        ego = 10
    return ego
