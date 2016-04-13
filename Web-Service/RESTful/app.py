__author__ = 'DePut'
import math
import re
import collections
import json
import urllib2



nama_server = "ManServer"


server = "http://192.168.88.65:5000/"
server1 = "http://192.168.88.64:5000/"
response = urllib2.urlopen(server)
response1 = = urllib2.urlopen(server1)
print json.load(response)
print json.load(response1)


