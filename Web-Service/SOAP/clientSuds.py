#!/usr/bin/env python

from suds.client import Client

client = Client('http://localhost:8888/Calculator/soap/description')


print 'Pembulatan ke atas  : 5.6      =', client.service.ceiler(5.6)
print 'Hasil count : ', client.service.count('cron')