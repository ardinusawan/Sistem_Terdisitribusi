__author__ = 'Indra Gunawan'

from suds.client import Client

client = Client('http://localhost:8888/Calculator/soap/description')

hasil = client.service.count('cron')
print 'Hasil count : ', hasil

bagi = hasil.split("[")
bagi2 = bagi[1].split("]")
bagi3 = bagi2[0].split(",")
print bagi
#print bagi[1]
print bagi[2]
#print bagi2[0][0]
print bagi3
#print bagi3[0]
bagi4 =bagi[2].split(",")

print bagi4

listranking = bagi3
listcomand = bagi4

