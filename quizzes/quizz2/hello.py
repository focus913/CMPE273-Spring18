from flask import Flask
from flask import request
import json
app = Flask(__name__)

usersMap = {}
id = 1

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/users', methods=['POST'])
def users():
    if request.method == 'POST':
        global id
        usersMap[id] = request.form['name']
        ret = json.dumps({'id': id, 'name': request.form['name']})
        id = id + 1
        return ret, 201
    else:
        return "Invalid method"

@app.route('/users/<int:userId>', methods=['GET', 'DELETE'])
def users1(userId):
    if request.method == 'GET':
        return json.dumps({'id': userId, 'name': usersMap[userId]})
    elif request.method == 'DELETE':
        usersMap.pop(userId, None)
        return "", 204
