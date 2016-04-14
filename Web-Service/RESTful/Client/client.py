__author__ = 'Indra Gunawan'
import json
import urllib2
import time
start_time = time.time()

server = "http://localhost:5000/"
server2 = "http://192.168.3.0:5000/"
response = urllib2.urlopen(server)
response2 = urllib2.urlopen(server2)
# print return value as json
#print json.load(response)
data = json.load(response)
data2 = json.load(response2)
lol = data["message"][0]["hasil17"]
lol2 = data2["message"][0]["hasil17"]
print lol
print "[v] response dari server-server mulai diranking"
tempc1 = []
temp1 = []
tempc2 = []
temp2 = []

bagi = lol.split("[")
bagi2 = bagi[1].split("]")
bagi3 = bagi2[0].split(",")
bagi4 =bagi[2].split(", ")

temp1 = bagi4
tempc1 = [int(i) for i in bagi3]
#print temp1

bagi = lol2.split("[")
bagi2 = bagi[1].split("]")
bagi3 = bagi2[0].split(",")
bagi4 =bagi[2].split(", ")

temp2 = bagi4
tempc2 = [int(i) for i in bagi3]
#print tempc1
#print tempc2

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

print "[v] Done"
print("--- %s seconds ---" % (time.time() - start_time))
