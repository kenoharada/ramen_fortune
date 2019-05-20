from flask import request, redirect, url_for, render_template, flash
from ramen import app, db
from ramen.models import Entry

@app.route('/')
def show_entries():
    entries = Entry.query.order_by(Entry.id.desc()).all()
    return render_template('show_entries.html', entries=entries)

@app.route('/answer', methods=['POST'])
def add_entry():
    entry = Entry(
            id=request.form['id'],
            q1=request.form['q1'],
            q2=request.form['q2'],
            q3=request.form['q3'],
            q4=request.form['q4'],
            q5=request.form['q5'],
            q6=request.form['q6'],
            q7=request.form['q7'],
            q8=request.form['q8'],
            q9=request.form['q9'],
            q10=request.form['q10']
            )
    db.session.add(entry)
    db.session.commit()
    #flash('New entry was successfully posted')
    Id = id=request.form['id']
    ##return redirect('/result/{int}',Id) #下の関数へ飛ばす


@app.route('/result/{int:Id}',method=['Get'])
def calc_result(Id):

    ans = Entry.query.filter(id==Id)


    #
    #計算内容の記述
    #
    #


    return render_template("結果表示するページ","送信する結果")
