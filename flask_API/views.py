import json
from flask import request, redirect, url_for, render_template, flash,jsonify
from ramen import app, db
from ramen.models import Entry

@app.route('/')
def show_entries():
    entries = Entry.query.order_by(Entry.id.desc()).all()
    return render_template('show_entries.html', entries=entries)

@app.route('/answer', methods=['POST'])
def add_entry():
    json = request.get_json()
    entry = Entry(
            id=json['id'],
            q1=json['q1'],
            q2=json['q2'],
            q3=json['q3'],
            q4=json['q4'],
            q5=json['q5'],
            q6=json['q6'],
            q7=json['q7'],
            q8=json['q8'],
            q9=json['q9'],
            q10=json['q10'],
            q11=json['q11'],
            q12=json['q12'],
            q13=json['q13'],
            q14=json['q14'],
            q15=json['q15']
            )
    db.session.add(entry)
    db.session.commit()


    #flash('New entry was successfully posted')
    #Id = id=request.form['id']
    ##return redirect('/result/{int}',Id) #下の関数へ飛ばす


@app.route('/result/{int:Id}',method=['Get'])
def calc_result(Id):

    ans = Entry.query.filter(id==Id)


    #
    #計算内容の記述
    #
    #

    your_ramen = 3

    result = {"result" : your_ramen}

    return jsonify(result)
