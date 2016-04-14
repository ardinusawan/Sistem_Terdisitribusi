__author__ = 'DePut'
from flask import Flask, jsonify
import math
import re
import collections
import json
import urllib2

app = Flask(__name__)

temp3 = []
tempc = []
tempoftemp = []
tempoftimec = []
hit = 0
flag = 0

nama_server = "S2"

def count(ofile):
    global folder_hasil_computasi, flag, temp3, hit, tempc, tempoftemp, tempoftimec
    temp1 = []
    temp_count = []
    buka = open(ofile)
    for i, line in enumerate(buka):
        lol = re.split("\W+", line, 8)
        temp1.append('(' + lol[8])
    f = open("cron-copy.txt", 'wb')
    f.writelines(temp1)
    buka.close()
    temp2 = []
    temp_count = []
    with open("cron-copy.txt") as infile:
        counts = collections.Counter(l.strip() for l in infile)
    for line, count in counts.most_common():
        temp_count.append(count)
        temp2.append(line)
    infile.close()
    f.close()

    if hit == 0:
        temp3 = temp2
        tempc = temp_count
        hit = hit + 1
    else:
        tempoftemp = temp2
        tempoftempc = temp_count
        hit = hit + 1

    iter1 = 0
    iter2 = 0
    if hit > 1:
        lentemp = len(tempoftemp)
        lentemp3 = len(temp3)
        cek = 0
        for i in range(lentemp):
            for j in range(lentemp3):
                cek += 1
                if tempoftemp[i] == temp3[j]:
                    tempc[j] += tempoftempc[i]
                    cek = -10;
                if cek == lentemp3 - 1:
                    temp3.append(tempoftemp[i])
                    tempc.append(tempoftempc[i])
            cek = 0
    buka2 = open(ofile)
    fmt = '%-8s%-20s%s'
    fole = open(nama_server, 'w')
    for i, (name, grade) in enumerate(zip(tempc, temp3)):
        data3 = fmt % (i, name, grade)
        fole.write(data3 + "\n")

    buka2.close()
    fole.close()
    coba = str(tempc)
    coba2 = str(temp3)
    coba3 = coba + coba2
    f2 = open(nama_server,'wb')
    f2.writelines(coba3)
    return coba3


@app.route("/")
def smanager():
    for i in range(17,34):
        if (i==0):
            fname="cron"
        else:
            fname="cron."+str(i)
        print "counting "+ fname
        if(i==33):
            s1 = count(fname)
        else:
            count(fname)
    print "Done 02 Done"
    return s1
            

if __name__ == "__main__":
   app.run(host='192.168.88.64', debug=True)
