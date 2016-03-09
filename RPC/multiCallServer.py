__author__ = 'Indra Gunawan'
from SimpleXMLRPCServer import SimpleXMLRPCServer
import re
import collections


def SplitElementTxt(ofile):
    temp=[]
    temp_count=[]
    buka = open(ofile)
    for i, line in enumerate(buka):
        lol = re.split("\W+", line, 8)
        temp.append('(' + lol[8])
    f = open("cron-copy.txt", 'wb')
    f.writelines(temp)
    buka.close()
    temp2=[]
    temp_count=[]
    with open('cron-copy.txt') as infile:
        counts = collections.Counter(l.strip() for l in infile)
    for line, count in counts.most_common():
        temp2.append(line)
        temp_count.append(count)
        # return line, count
    infile.close()
    '''
    print 'Assignment \t\tGrade'
    for n,g in zip(temp,temp_count):
        print n + '\t\t\t' + g
    '''
    fmt = '%-8s%-20s%s'

    print(fmt % ('',  'Frequent','Command'))
    for i, (name, grade) in enumerate(zip(temp_count,temp2)):
        print(fmt % (i, name, grade))
    #lola = temp + " "
    #lolu = lola + str(temp_count)
    #return lolu
    return temp2, temp_count

'''
def SortCount():
    temp=[]
    temp_count=[]
    with open('cron-copy.txt') as infile:
        counts = collections.Counter(l.strip() for l in infile)
    for line, count in counts.most_common():
        temp.append(line)
        temp_count.append(count)
        # return line, count
    infile.close()
    return temp, temp_count
'''



server = SimpleXMLRPCServer(("localhost", 8000), allow_none=True)
print "Listening on port 8000 ... "
server.register_multicall_functions()
server.register_function(add, "add")
server.register_function(SplitElementTxt,"SplitElementTxt")
#server.register_function(SortCount,"SortCount")
server.serve_forever()