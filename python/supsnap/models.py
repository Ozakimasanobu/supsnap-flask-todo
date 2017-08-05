from db import db

class tasks(db.Model):
    id = db.Column('student_id', db.Integer, primary_key = True)
    title = db.Column(db.String(200))
    
    def __init__(self, title):
        self.title = title

def init():
    db.create_all()
