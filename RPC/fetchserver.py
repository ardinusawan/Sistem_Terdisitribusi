__author__ = 'Indra Gunawan'
from SimpleXMLRPCServer import SimpleXMLRPCServer
import xmlrpclib

def datakirim():
    with open("server1.txt", "rb") as handle:
        return xmlrpclib.Binary(handle.read())

server = SimpleXMLRPCServer(("localhost", 8000))
print "Listening on port 8000 ... "
server.register_function(datakirim, "datakirim")
server.serve_forever()