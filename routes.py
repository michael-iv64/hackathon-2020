from flask import Blueprint
from models import Courses
from flask import request
from app import db
from models import Stata
from flask import Response
from json import dumps

api = Blueprint('api', __name__)

response_id = 0

@api.route('/add', methods=['POST'])
def online_courses():
       data = request.get_json()
       global response_id
       response_id += 1
       username = data[0]['username']
       video = data[0]['video']
       new_lectory = Courses(username=username, video=video)
       new_stata = Stata(name=username, num_lec = 100, num_video = 1, mark=-1)
       if Stata.query.filter_by(name=username).first():
           db.session.add(new_lectory)
           db.session.commit()
           courses = Stata.query.filter_by(name=username).first()
           courses.num_video += 1
           db.session.commit()
           name, num_lectury, num_video, mark = str(courses).split(' ')
           return Response(dumps([{'id':response_id, 'statistic': {'name':name,'num_lectury':num_lectury, 'num_video':num_video, 'mark':mark}}]), status=201, mimetype='application/json')

       db.session.add_all([new_lectory, new_stata])
       db.session.commit()
       return Response(dumps([{'id':response_id, 'statistic': {'name': username, 'num_video': 1}}]), status=201, mimetype='application/json')

@api.route('/stata', methods=['GET'])
def stata():
    global response_id
    response_id += 1
    statistic = Stata.query.all()
    statistic = list(statistic)
    list_dict = []
    for i in range(len(statistic)):
       record = str(statistic[i]).split(' ')
       data = {'id': response_id, 'username':record[0], 'lec': record[1], 'video':record[2], 'mark':record[3]}
       response_id += 1
       list_dict.append(data)
    return Response(dumps(list_dict), status=200, mimetype='application/json')

@api.route('/', methods=['GET'])
def test():
    global response_id
    response_id += 1
    return Response(dumps([{'id': response_id ,'name': 'Ivanov Ivan', 'num_video': 1, 'num_lectury':100}]), status=200, mimetype='application/json')
