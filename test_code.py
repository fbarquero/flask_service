from requests import Session
from json import dumps
from uuid import uuid1
headers = {'Content-Type': 'application/json'}
#
session = Session()
#
# response = session.get('http://localhost:5000/todo/api/v1.0/tasks', headers=headers)
# # response = session.post('http://localhost:5000/todo/api/v1.0/login', headers=headers)
task_number = 3
task_name = 'task_{}'.format(uuid1())
print task_name
description = 'description of task {}'.format(task_name)
response = session.post("http://localhost:5000/todo/api/v1.0/tasks", headers=headers,
                        data=dumps({'title': task_name, 'description': description}))

print response.content
print response.status_code