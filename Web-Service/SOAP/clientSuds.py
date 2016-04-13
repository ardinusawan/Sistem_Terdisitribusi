__author__ = 'Indra Gunawan'
__author__ = 'Dwi Pratama'
#C:\Python27\python.exe C:\Python27\Scripts\ladon-2.7-ctl.py testserve serverLadon.py -p 8888
from suds.client import Client
import re
import collections

client = Client('http://localhost:8888/Calculator/soap/description')
#client2 = Client('http://192.168.0.0:8888/Calculator/soap/description')

hasil = client.service.count('cron')
hasil = client.service.count('cron.1')

#hasil1 = client2.service.count('cron.3')
#print 'Hasil count : ', hasil

bagi = hasil.split("[")
bagi2 = bagi[1].split("]")
bagi3 = bagi2[0].split(",")
#print bagi
#print bagi[1]
#print bagi[2]
#print bagi2[0][0]
#print bagi3
#print bagi3[0]
bagi4 =bagi[2].split(",")

#print bagi4

#listranking = bagi3
#listcomand = bagi4
tempc1 = []
temp1 = []
tempc2 = []
temp2 = []

temp1 = bagi4
tempc1 = [int(i) for i in bagi3]

temp2 = bagi4
tempc2 = [int(i) for i in bagi3]

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
        data3 = fmt % (i+1, name, grade)
        print data3
        hitung = hitung +1



