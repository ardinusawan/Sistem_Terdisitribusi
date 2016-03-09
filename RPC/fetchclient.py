__author__ = 'Indra Gunawan'
import xmlrpclib

proxy = xmlrpclib.ServerProxy("http://localhost:8000/")
with open("fetched_python_data.txt", "wb") as handle:
    handle.write(proxy.datakirim().data)