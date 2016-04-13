__author__ = 'DePut'
import json
import urllib2


server = "http://localhost:5000/"
req = urllib2.Request(server)
response = urllib2.urlopen(req)
print response.read()
