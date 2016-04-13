# Source: http://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask
import json
import urllib2
import os
import hello
import SplitElement
from flask import Flask, jsonify


app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

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


@app.route('/test', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

@app.route('/hello', methods=['GET'])
def print_berhasil():
    hello.write()
    return "berhasil"

@app.route('/run/<id>', methods=['GET'])
def run(id):
    if id()==1000:
        SplitElement.SplitElementTxt("cron");
    else:
        SplitElement.SplitElementTxt("cron"+"."+id);
        return 'yey';


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5001,debug=True)
    # app.register_blueprint(printme)

