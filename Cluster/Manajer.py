__author__ = 'Indra Gunawan'

import math, sys, time
import pp
import re
import collections, string

def isprime(n):
    """Returns True if n is prime and False otherwise"""
    if not isinstance(n, int):
        raise TypeError("argument passed to is_prime is not of 'int' type")
    if n < 2:
        return False
    if n == 2:
        return True
    max = int(math.ceil(math.sqrt(n)))
    i = 2
    while i <= max:
        if n % i == 0:
            return False
        i += 1
    return True

def sum_primes(n):
    """Calculates sum of all primes below given integer n"""
    return sum([x for x in xrange(2,n) if isprime(x)])

print """Usage: python sum_primes.py [ncpus]
    [ncpus] - the number of workers to run in parallel,
    if omitted it will be set to the number of processors in the system
"""


def count(ofile):
    #global folder_hasil_computasi, flag, temp3, hit, tempc, tempoftemp, tempoftimec
    temp3 = []
    tempc = []
    tempoftemp = []
    tempoftimec = []
    hit = 0
    flag = 0
    temp1 = []
    temp_count = []
    nama_server = "DWI_SERVER"
    # folder_log="Log/"

    # ofile = folder_log + ofile
    #print ofile

    isfile = open("isi.txt","wb")
    isfile.writelines(ofile)
    isfile.close()

    buka = open("isi.txt")
    for i, line in enumerate(buka):
        lol = re.split("\W+", line, 8)
        temp1.append('(' + lol[8])
    # f = open(folder_hasil_computasi + "cron-copy.txt", 'wb')
    f = open("cron-copy.txt", 'wb')
    f.writelines(temp1)
    buka.close()
    temp2 = []
    temp_count = []
    # with open(folder_hasil_computasi + "cron-copy.txt") as infile:
    with open("cron-copy.txt") as infile:
        counts = collections.Counter(l.strip() for l in infile)
    for line, count in counts.most_common():
        temp2.append(line)
        temp_count.append(count)
        # return line, count
    infile.close()
    f.close()
    # tempoftemp.append([temp2, temp_count])
    # buka2 = open(ofile)

    if hit == 0:
        temp3 = temp2
        tempc = temp_count
        hit = hit + 1
    else:
        tempoftemp = temp2
        tempoftempc = temp_count
        hit = hit + 1

    # lola = temp + " "
    # lolu = lola + str(temp_count)
    # return lolu
    # print tempoftemp
    iter1 = 0
    iter2 = 0
    if hit > 1:
        lentemp = len(tempoftemp)
        lentemp3 = len(temp3)
        # print nyonyo
        cek = 0
        for i in range(lentemp):
            for j in range(lentemp3):
                cek += 1
                if tempoftemp[i] == temp3[j]:
                    tempc[j] += tempoftempc[i]
                    cek = -10
                if cek == lentemp3 - 1:
                    temp3.append(tempoftemp[i])
                    tempc.append(tempoftempc[i])
            cek = 0
    #p = Page()
    #p.content = [None]*100
    #buka2 = open(ofile)
    fmt = '%-8s%-20s%s'
    # print(fmt % ('',  'Frequent','Command'))
    fole = open(nama_server, 'w')
    # fole = open(folder_hasil_computasi +  "server1.txt", 'w')
    for i, (name, grade) in enumerate(zip(tempc, temp3)):
        # print(fmt % (i, name, grade))
        data3 = fmt % (i, name, grade)
        #p.content.append(tempc[i])
        # print data3
        fole.write(data3 + "\n")

    #buka2.close()
    fole.close()
    coba = str(tempc)
    coba2 = str(temp3)
    coba3 = coba + coba2
    #print tempc
    return coba3

    #return ofile

# tuple of all parallel python servers to connect with
#ppservers = ()
ppservers = ("*",)

if len(sys.argv) > 1:
    ncpus = int(sys.argv[1])
    # Creates jobserver with ncpus workers
    job_server = pp.Server(ncpus, ppservers=ppservers)
else:
    # Creates jobserver with automatically detected number of workers
    job_server = pp.Server(ppservers=ppservers)

print "Starting pp with", job_server.set_ncpus(0), "workers"
print "Starting pp with", job_server.get_ncpus(), "workers"

# Submit a job of calulating sum_primes(100) for execution.
# sum_primes - the function
# (100,) - tuple with arguments for sum_primes
# (isprime,) - tuple with functions on which function sum_primes depends
# ("math",) - tuple with module names which must be imported before sum_primes execution
# Execution starts as soon as one of the workers will become available
#job1 = job_server.submit(sum_primes, (100,), (isprime,), ("math",))
#job1 = job_server.submit(count, ("cron",), depfuncs=(), modules=("re","collections",))

# Retrieves the result calculated by job1
# The value of job1() is the same as sum_primes(100)
# If the job has not been finished yet, execution will wait here until result is available
#result = job1()
#print result

#print "Hasilnya adalah", result

start_time = time.time()

file0 = open('cron')
str0 = str(file0.read())
file0.close()

file1 = open('cron.1')
str1 = str(file1.read())
file1.close()

file2 = open('cron.2')
str2 = str(file2.read())
file2.close()

file3 = open('cron.3')
str3 = str(file3.read())
file3.close()

file4 = open('cron.4')
str4 = str(file4.read())
file4.close()

file5 = open('cron.5')
str5 = str(file5.read())
file5.close()

file6 = open('cron.6')
str6 = str(file6.read())
file6.close()

file7 = open('cron.7')
str7 = str(file7.read())
file7.close()


job1 = job_server.submit(count, (str0,), depfuncs=(), modules=("re","collections",))
result = job1()
print result

job2 = job_server.submit(count, (str1,), depfuncs=(), modules=("re","collections",))
result = job2()
print result

# The following submits 8 jobs and then retrieves the results
'''
inputs = (str0)
jobs = [(input, job_server.submit(count,(input,), depfuncs=(), modules=("re","collections",))) for input in inputs]
for input, job in jobs:
    print "proses hasilnya adalah", job()
'''

print "Time elapsed: ", time.time() - start_time, "s"
job_server.print_stats()

# Parallel Python Software: http://www.parallelpython.com