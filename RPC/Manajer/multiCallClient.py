__author__ = 'Indra Gunawan'
import xmlrpclib
import re
import time
start_time = time.time()
#main()

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
Server = "http://192.168.88.79:8000/"
Server1 = "http://192.168.88.89:8000/"
proxy = xmlrpclib.ServerProxy(Server)
proxy2 = xmlrpclib.ServerProxy(Server1)
#proxy2 = xmlrpclib.ServerProxy("http://localhost:8000/", allow_none=True)
multicall = xmlrpclib.MultiCall(proxy)
multicall2 = xmlrpclib.MultiCall(proxy2)
# folder_hasil_komputasi = "Hasil_Server/"
multicall.SplitElementTxt("cron")
multicall.SplitElementTxt("cron.1")
multicall.SplitElementTxt("cron.2")

multicall2.SplitElementTxt("cron.3")
multicall2.SplitElementTxt("cron.4")
multicall2.SplitElementTxt("cron.5")
result = multicall()
result2 = multicall2()
print tuple(result)
with open("fetched_python_data.txt", "wb") as handle:
    handle.write(proxy.datakirim().data)

print tuple(result2)
# with open(folder_hasil_komputasi + "fetched_python_data2.txt", "wb") as handle:
with open("fetched_python_data2.txt", "wb") as handle:
    handle.write(proxy2.datakirim().data)

tempc1 = []
temp1 = []
buka = open('fetched_python_data.txt')
for i, line in enumerate(buka):
    lol = re.split("\W+", line, 2)
    tempc1.append(int(lol[1]))
    temp1.append('('+lol[2])
print temp1
print tempc1

tempc2 = []
temp2 = []
buka = open('fetched_python_data2.txt')
for i, line in enumerate(buka):
    lol = re.split("\W+", line, 2)
    tempc2.append(int(lol[1]))
    temp2.append('('+lol[2])
print temp2
print tempc2

lentemp1 = len(temp1)
lentemp2 = len(temp2)
cek = 0
for i in range(lentemp2):
    for j in range(lentemp1):
        cek+=1
        if temp2[i] == temp1[j]:
            tempc1[j] += tempc2[i]
            cek = -10;
        if cek==lentemp1-1 :
            #print 'masuk'
            temp1.append(temp2[i])
            tempc1.append(tempc2[i])
    cek = 0

lentemp1 = len(temp1)
for i in range(lentemp1):
    for j in range(lentemp1):

        if tempc1[i] > tempc1[j]:
            tempoftemp = temp1[i]
            tempoftempc = tempc1[i]
            temp1[i] = temp1[j]
            tempc1[i] = tempc1[j]
            temp1[j] = tempoftemp
            tempc1[j] = tempoftempc

fmt = '%-8s%-20s%s'
print(fmt % ('',  'Frequent','Command'))
hitung = 0

for i, (name, grade) in enumerate(zip(tempc1,temp1)):
    #print(fmt % (i, name, grade))
    if hitung != 10 :
        data3 = fmt % (i, name, grade)
        print data3
        hitung = hitung +1


print("--- %s seconds ---" % (time.time() - start_time))
