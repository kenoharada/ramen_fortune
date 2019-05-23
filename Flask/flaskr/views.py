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

    mean = x.sum()
    i = (mean*1402)%3
    ans = ["二郎タイプ","家系タイプ","博多系タイプ"]
    result = {"result":ans[i]}

    return render_template('show_result.html',entries=result)
