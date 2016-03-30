__author__ = 'Indra Gunawan'

import pika
import sys

#credentials = pika.PlainCredentials('test', 'test')
#parameters = pika.ConnectionParameters('192.168.0.24', credentials=credentials)

#connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.0.24', credentials=credentials))
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs',
                         type='fanout')

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='logs',
                   queue=queue_name)

print ' [*] Waiting for logs. To exit press CTRL+C'

def callback(ch, method, properties, body):
    print " [x] %r" % (body,)

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

try:
    channel.start_consuming()

except KeyboardInterrupt:
    sys.exit(1)