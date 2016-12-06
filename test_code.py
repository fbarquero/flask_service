from requests import Session

headers = {'Content-Type': 'application/json'}

session = Session()

response = session.get('http://localhost:5000/todo/api/v1.0/tasks', headers=headers)
# response = session.post('http://localhost:5000/todo/api/v1.0/login', headers=headers)
print response.content
print response.status_code