__author__ = 'DePut'
from flask import Flask, jsonify
import math
import re
import collections
import json
import urllib2

app = Flask(__name__)

nama_server = "ManServer"

@app.route("/")
def smanager():
    server = "http://192.168.88.89:5000/"
    response = urllib2.urlopen(req)
    return json.load(response)

if __name__ == "__main__":
   app.run(host = "192.168.88.32")
