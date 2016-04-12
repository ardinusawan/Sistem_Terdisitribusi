__author__ = 'Indra Gunawan'
from ladon.compat import PORTABLE_STRING

from ladon.ladonizer import ladonize
import math
import re
import collections
from ladon.types.ladontype import LadonType

temp3 = []
tempc = []
tempoftemp = []
tempoftimec = []
hit = 0
flag = 0

nama_server = "DWI_SERVER"




class Calculator(object):
    @ladonize(float, rtype=float)
    def ceiler(self, a):
        return math.ceil(a)

    @ladonize(str, rtype=str)
    def count(self, ofile):
        global folder_hasil_computasi, flag, temp3, hit, tempc, tempoftemp, tempoftimec
        temp1 = []
        temp_count = []
        # folder_log="Log/"

        # ofile = folder_log + ofile
        buka = open(ofile)
        for i, line in enumerate(buka):
            lol = re.split("\W+", line, 8)
            temp1.append('(' + lol[8])
        # f = open(folder_hasil_computasi + "cron-copy.txt", 'wb')
        f = open("cron-copy.txt", 'wb')
        f.writelines(temp1)
        buka.close()
        temp2 = []
        temp_count = []
        # with open(folder_hasil_computasi + "cron-copy.txt") as infile:
        with open("cron-copy.txt") as infile:
            counts = collections.Counter(l.strip() for l in infile)
        for line, count in counts.most_common():
            temp2.append(line)
            temp_count.append(count)
            # return line, count
        infile.close()
        f.close()
        # tempoftemp.append([temp2, temp_count])
        # buka2 = open(ofile)
        '''
        fmt = '%-8s%-20s%s'
        print(fmt % ('',  'Frequent','Command'))
        fole = open("server1.txt", 'a')
        for i, (name, grade) in enumerate(zip(temp_count,temp2)):
            #print(fmt % (i, name, grade))
            data3 = fmt % (i, name, grade)
            #print data3
            fole.write(data3+"\n")

        buka2.close()
        '''
        if hit == 0:
            temp3 = temp2
            tempc = temp_count
            hit = hit + 1
        else:
            tempoftemp = temp2
            tempoftempc = temp_count
            hit = hit + 1

        # lola = temp + " "
        # lolu = lola + str(temp_count)
        # return lolu
        # print tempoftemp
        iter1 = 0
        iter2 = 0
        if hit > 1:
            lentemp = len(tempoftemp)
            lentemp3 = len(temp3)
            # print nyonyo
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
        #p = Page()
        #p.content = [None]*100
        buka2 = open(ofile)
        fmt = '%-8s%-20s%s'
        # print(fmt % ('',  'Frequent','Command'))
        fole = open(nama_server, 'w')
        # fole = open(folder_hasil_computasi +  "server1.txt", 'w')
        for i, (name, grade) in enumerate(zip(tempc, temp3)):
            # print(fmt % (i, name, grade))
            data3 = fmt % (i, name, grade)
            #p.content.append(tempc[i])
            # print data3
            fole.write(data3 + "\n")

        buka2.close()
        fole.close()
        coba = str(tempc)
        coba2 = str(temp3)
        coba3 = coba + coba2
        #print tempc
        return coba3
