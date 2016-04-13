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
    server = "http://localhost:5001/"
    req = urllib2.Request(server)
    response = urllib2.urlopen(req)

if __name__ == "__main__":
   app.run(host='localhost', port=5000)
