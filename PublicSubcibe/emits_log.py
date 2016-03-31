__author__ = 'Indra Gunawan'
import pika
import sys

#files = [('file', open('cron', 'rb')), ('file', open('cron1', 'rb'))]
#nama = ['cron','cron1', 'cron2']

#j=0

filenames = ['cron', 'cron.1','cron.2','cron.3','cron.4','cron.5','cron.6','cron.7','cron.8','cron.9','cron.10','cron.11','cron.12','cron.13','cron.14','cron.15','cron.16',]
with open('crongabung1', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)

credential = pika.PlainCredentials('test','test')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.0.23', credentials=credential))
channel = connection.channel()

channel.exchange_declare(exchange='logs', type='fanout')



f=open('crongabung1',"rb")
i=f.read()

message = ' '.join(sys.argv[1:]) or "logs to worker"
channel.basic_publish(exchange='logs',routing_key='',body=i)
print " [x] Sent %r" % (message,)

connection.close()