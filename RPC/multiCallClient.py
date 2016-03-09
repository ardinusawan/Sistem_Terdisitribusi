__author__ = 'Indra Gunawan'
import xmlrpclib

proxy = xmlrpclib.ServerProxy("http://localhost:8000/", allow_none=True)
#proxy2 = xmlrpclib.ServerProxy("http://localhost:8000/", allow_none=True)
multicall = xmlrpclib.MultiCall(proxy)
#multicall.add(2, 3)
# multicall.subtract(2, 3)
# multicall.multiply(2, 3)
# multicall.divide(2.0, 3.0)
##server mencari pc yg terhubung
##server membagi tugas

multicall.SplitElementTxt("cron")
#multicall.SortCount()
##server mendapatkan return value
result = multicall()
print list(result)

#multicall.SplitElementTxt("coba.txt")
#multicall.SortCount()
##server mendapatkan return value
#result = multicall()
#print tuple(result)