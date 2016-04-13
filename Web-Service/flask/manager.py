__author__ = 'DePut'

import xmlrpclib
import re
import time
start_time = time.time()

tempc1 = []
temp1 = []
buka = open('S1_SERVER')
for i, line in enumerate(buka):
    lol = re.split("\W+", line, 2)
    tempc1.append(int(lol[1]))
    temp1.append('('+lol[2])
print temp1
print tempc1

tempc2 = []
temp2 = []
buka = open('S2_SERVER')
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
