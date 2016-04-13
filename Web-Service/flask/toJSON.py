__author__ = 'DePut'

import re

tempc1 = []
temp1 = []
buka = open('WAWAN_SERVER.txt')
for i, line in enumerate(buka):
    lol = re.split("\W+", line, 2)
    print lol[0]
    print lol[1]
    print lol[2]
    #tempc1.append(lol[1])
    #temp1.append('('+lol[2])

f = open("jsontext.txt", 'wb')
print tempc1
print temp1

#for i, line in enumerate(temp1):
    #f.write(str(i))
    #f.write(str(tempc1[i]))
    #f.write(temp1[i])
    #f.write("|-")
