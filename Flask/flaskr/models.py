from flaskr import db

class Entry(db.Model):
    __tablename__ = 'entries'
    id = db.Column(db.Integer, primary_key=True)
    q1 = db.Column(db.Text)
    q2 = db.Column(db.Text)
    q3 = db.Column(db.Text)
    q4 = db.Column(db.Text)
    q5 = db.Column(db.Text)
    q6 = db.Column(db.Text)
    q7 = db.Column(db.Text)
    q8 = db.Column(db.Text)
    q9 = db.Column(db.Text)
    q10 = db.Column(db.Text)

    def __repr__(self):
        return '<Entry id={id} q1={q1} q2={q2} q3={q3} q4={q4} q5={q5} q6={q6} q7={q7} q8={q8} q9={q9} q10={q10}>'.format(
                id=self.id,q1=self.q1, q2=self.q2,q3=self.q3,q4=self.q4,q5=self.q5,q6=self.q6,q7=self.q7,q8=self.q8,q9=self.q9,q10=self.q10)

def init():
    db.create_all()
