__author__ = 'Indra Gunawan'

import xmlrpclib
import re

'''
import socket

server_addr = ('localhost',9000)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(server_addr)

client_socket.send('yolo')
data = client_socket.recv(1024)

fo=open("hasil1",'wb')

while True:
    data=client_socket.recv(1024)
    if not data: break
    fo.write(data)
fo.close()
'''

Server = "http://192.168.0.23:5672/"
proxy = xmlrpclib.ServerProxy(Server)
multicall = xmlrpclib.MultiCall(proxy)
result = multicall()
with open("fetched_python_data.txt", "wb") as handle:
    handle.write(proxy.datakirim().data)
