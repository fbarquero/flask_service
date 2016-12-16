from flask import Flask, jsonify
from flask import abort
from flask import make_response
from flask import request
from functools import wraps
import uuid

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]

valid_user_tokens = ['9a16cf99-c28a-11e6-a3ed-6c40089a7e6e']


def authenticate():
    return "authenticate with valid user token", 401


def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'auth-token' not in request.headers:
            return authenticate()
        if request.headers['auth-token'] not in valid_user_tokens:
            return authenticate()
        return f(*args, **kwargs)
    return decorated


@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})


@app.route('/todo/api/v1.0/healthcheck', methods=['GET'])
def health():
    return jsonify({'status': "I'm Healthy!!"})


@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})


@app.route('/todo/api/v1.0/tasks', methods=['POST'])
def create_task():
    if not request.json or 'title' not in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 200


@app.route('/todo/api/v1.0/login', methods=['POST'])
def login():
    token = uuid.uuid1()
    valid_user_tokens.append(token)
    return jsonify({'token': token})


@app.route('/todo/api/v1.0/html', methods=['GET'])
@requires_auth
def get_html():
    html = '<html>' \
                '<body>' \
                    '<h1>HELLO WORLD!!<h1>' \
                '</body>' \
           '</html>'
    return html



@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=11000)
