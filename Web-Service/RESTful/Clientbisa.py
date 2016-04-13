__author__ = 'DePut'
import json
import urllib2


server = "http://localhost:5000/"
response = urllib2.urlopen(server)
print json.load(response)
