from flask import Flask, jsonify
from flask import abort
from flask import make_response
from flask import request
from functools import wraps
import uuid

from redis_connector import RedisConn


app = Flask(__name__)
valid_user_tokens = []


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


@app.route('/v1.0/redis/entries', methods=['GET'])
def get_all_redis_entries():
    return jsonify({'tasks': ""})


@app.route('/v1.0/redis/healthcheck', methods=['GET'])
def health():
    return jsonify({'status': "I'm Healthy!!"})


@app.route('/v1.0/redis/entry/<int:task_id>', methods=['GET'])
def get_redis_entry(entry_key):
    value = RedisConn().redis_read(entry_key)
    if value is None:
        abort(404)
    return jsonify({'data': value})


@app.route('/v1.0/add_redis_entry', methods=['POST'])
def add_redis_entry():
    if not request.json or 'redis_entry' not in request.json:
        abort(400)
    data = request.json['redis_entry']
    key = data['key']
    value = data['value']
    k = RedisConn().redis_write(key, value)
    if k is None:
        abort(501)
    return jsonify({'data': k}), 201


@app.route('/todo/api/v1.0/login', methods=['POST'])
def login():
    token = uuid.uuid1()
    valid_user_tokens.append(str(token))
    return jsonify({'token': token})


@app.route('/todo/api/v1.0/tokens', methods=['GET'])
def get_tokens():
    return jsonify({'tokens': valid_user_tokens})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=12000)
