from app import db
from datetime import datetime

class Courses(db.Model):
    __tablename__ = "lectures"
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(500))
    video = db.Column(db.String(500))
    date = db.Column(db.DateTime)
    mark = db.Column(db.Float)

    def __init__(self, username, video, date=datetime.now(), mark=-1):
        self.username = username
        self.video = video
        self.date = date
        self.mark = mark

    def __repr__(self):
        return str(self.username) + ' ' + str(self.video)  + ' ' + str(self.date) + ' ' + str(self.mark)

class Stata(db.Model):
    __tablename__ = 'stata'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500))
    num_lec = db.Column(db.Integer)
    num_video = db.Column(db.Integer)
    mark = db.Column(db.Float)

    def __init__(self, name, num_lec, num_video, mark):
        self.name = name
        self.num_lec = num_lec
        self.num_video = num_video
        self.mark = mark

    def __repr__(self):
        return self.name + ' ' + str(self.num_lec) + ' ' + str(self.num_video) + ' ' + str(self.mark)
#тестирование на коленке
#test = Courses(username = 'None',num_video = 2, num_lectures =  12)
#print(test)
#test = Stata(name='defd', num_lec=1, num_video=3, mark = 4)
#print(test)
