__author__ = 'Dwi'

import re

pattern = re.compile("abc")

buka = open('cron.txt')
temp = []
tempCount = []
count = 0
j = 0
for i, line in enumerate(buka):
    lol = re.split("\W+", line, 8)
    temp.append('(' + lol[8])

f = open("cron-copy.txt", 'wb')
f.writelines(temp)