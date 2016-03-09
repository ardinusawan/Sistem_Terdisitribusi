__author__ = 'Indra Gunawan'
import xmlrpclib
"""
def unzip(args):

    inverse of zip. Given: ((1,"a"),(2,"b")) --> ((1,2),("a","b"))

    seq == unzip(zip(seq)) if seq is a rectangular matrix (all of its row has the same length.

    result = []
    n = min(map(len,args))
    for i in range(n):result.append([])
    for i in range(len(args)):
        for j in range(n):
            result[j].append(args[i][j])
    return tuple(result)
"""

proxy = xmlrpclib.ServerProxy("http://192.168.88.47:8000/")
proxy2 = xmlrpclib.ServerProxy("http://192.168.88.89:8000/")
#proxy2 = xmlrpclib.ServerProxy("http://localhost:8000/", allow_none=True)
multicall = xmlrpclib.MultiCall(proxy)
multicall2 = xmlrpclib.MultiCall(proxy2)
folder_hasil_komputasi = "Hasil_Server/"
multicall.SplitElementTxt("cron")
multicall.SplitElementTxt("cron.1")
multicall.SplitElementTxt("cron.2")

multicall2.SplitElementTxt("cron.3")
multicall2.SplitElementTxt("cron.4")
multicall2.SplitElementTxt("cron.5")

#multicall.SortCount()
##server mendapatkan return value
result = multicall()
result2 = multicall2()

# for i in range((result)):
#     x,y=zip(*result)
# xy=(list(x),list(y))
#
# list1, list2 = unzip((*result)
# list(result) == zip(list1, list2)

# list1= ( x[0] for x in result )
# list2= ( x[1] for x in result )
#
# print str(list1), str(list2)


# zip(result)
# print tuple(zip(result))
print tuple(result)
with open(folder_hasil_komputasi + "fetched_python_data.txt", "wb") as handle:
    handle.write(proxy.datakirim().data)

print tuple(result2)
with open(folder_hasil_komputasi + "fetched_python_data2.txt", "wb") as handle:
    handle.write(proxy.datakirim().data)
#multicall.SplitElementTxt("coba.txt")
#multicall.SortCount()
##server mendapatkan return value
#result = multicall()
#print tuple(result)