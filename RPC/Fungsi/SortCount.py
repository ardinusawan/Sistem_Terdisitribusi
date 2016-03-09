__author__ = 'Dwi'

import collections

with open('coba2.txt') as infile:
    counts = collections.Counter(l.strip() for l in infile)
for line, count in counts.most_common():
    print line, count