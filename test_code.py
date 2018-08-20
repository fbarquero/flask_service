from requests import Session
from json import dumps
from uuid import uuid1
headers = {'Content-Type': 'application/json', 'auth-token': '9a16cf99-c28a-11e6-a3ed-6c40089a7e6e'}
#
session = Session()
#
#response = session.get('http://localhost:5000/todo/api/v1.0/tasks', headers=headers)
# # response = session.post('http://localhost:5000/todo/api/v1.0/login', headers=headers)

key = "test_key"
value = "value to be assigned to the key as test data"
response = session.post("http://localhost:12000/v1.0/add_redis_entry", headers=headers,
                        data=dumps({'redis_entry': {'key': key, 'value': value}}))

print response.status_code
print response.content

