#!/usr/bin/env python

from suds.client import Client

client = Client('http://localhost:8888/Calculator/soap/description')

hasil = client.service.count('cron')
print 'Hasil count : ', hasil