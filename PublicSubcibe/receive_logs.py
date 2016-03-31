__author__ = 'Indra Gunawan'

import pika
import sys
import re
import collections
import socket


credentials = pika.PlainCredentials('test', 'test')
connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.43.123', credentials=credentials))
#connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.0.30'))
channel = connection.channel()

channel.exchange_declare(exchange='logs',type='fanout')

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='logs',
                   queue=queue_name)

print ' [*] Waiting for logs. To exit press CTRL+C'
'''
def callback(ch, method, properties, body):
    print " [x] %r" % (body,)
'''

f=open("crongabung1.txt","wb")

temp3=[]
tempc=[]
tempoftemp = []
tempoftimec = []
hit = 0
flag=0
nama_server="WAWAN_SERVER"
#IP_Server="192.168.43.207"
#PORT_Server=8000
# folder_hasil_computasi="Hasil_Computasi/"
def SplitElementTxt(ofile):
    global folder_hasil_computasi, flag, temp3, hit, tempc, tempoftemp, tempoftimec
    temp1=[]
    temp_count=[]
    #folder_log="Log/"

    #ofile = folder_log + ofile
    buka = open(ofile)
    for i, line in enumerate(buka):
        lol = re.split("\W+", line, 8)
        temp1.append('(' + lol[8])
    # f = open(folder_hasil_computasi + "cron-copy.txt", 'wb')
    f = open("cron-copy.txt", 'wb')
    f.writelines(temp1)
    buka.close()
    temp2=[]
    temp_count=[]
    # with open(folder_hasil_computasi + "cron-copy.txt") as infile:
    with open("cron-copy.txt") as infile:
        counts = collections.Counter(l.strip() for l in infile)
    for line, count in counts.most_common():
        temp2.append(line)
        temp_count.append(count)
        # return line, count
    infile.close()
    f.close()
    #tempoftemp.append([temp2, temp_count])
    #buka2 = open(ofile)

    if hit == 0 :
        temp3 = temp2
        tempc = temp_count
        hit=hit +1
    else :
        tempoftemp = temp2
        tempoftempc = temp_count
        hit=hit +1

    iter1 = 0
    iter2 = 0
    if hit>1 :
        lentemp = len(tempoftemp)
        lentemp3 = len(temp3)

        cek = 0
        for i in range(lentemp):
            for j in range(lentemp3):
                cek+=1
                if tempoftemp[i] == temp3[j]:
                    tempc[j] += tempoftempc[i]
                    cek = -10;
                if cek==lentemp3-1 :
                    temp3.append(tempoftemp[i])
                    tempc.append(tempoftempc[i])
            cek = 0

    buka2 = open(ofile)
    fmt = '%-8s%-20s%s'
    print(fmt % ('',  'Frequent','Command'))
    fole = open(nama_server, 'w')
    # fole = open(folder_hasil_computasi +  "server1.txt", 'w')
    for i, (name, grade) in enumerate(zip(tempc,temp3)):
        print(fmt % (i, name, grade))
        data3 = fmt % (i, name, grade)
        #print data3
        fole.write(data3+"\n")

    buka2.close()
    fole.close()


def kirim(ofile):
    server_addr = ('localhost',9000)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(server_addr)

    server_socket.listen(1)
    #print 'waiting connection...'
    server_socket.accept()
    f=open(ofile,"rb")
    bytesToSend = f.read(4096)
    server_socket.send(bytesToSend)
    while bytesToSend != "":
        bytesToSend = f.read(4096)
        server_socket.send(bytesToSend)



def callback(ch, method, properties, body):
    f.write(body)
    f.close()
    SplitElementTxt('crongabung1.txt')



channel.basic_consume(callback,queue=queue_name,no_ack=True)

print ' [*] logs diterima'
try:
    channel.start_consuming()

except KeyboardInterrupt:
    sys.exit(1)