""" import getpass
pw = input("Pass: ")
# pw = getpass.getpass("Pass: ")
print(pw) """



""" import hashlib

hl = hashlib.sha256()
# target = "hello"
target = "to be or not to be, That is a question!"

hl.update(target.encode("utf-8"))
print(hl.hexdigest()) """



""" import Crypto.Hash.keccak as keccak

target = "to be or not to be, That is a question!"

kksh = keccak.new(digest_bits=256)
kksh.update(target.encode("utf-8"))

print(kksh.hexdigest()) """



""" import getpass
import hashlib

pw = getpass.getpass("Pass: ")
print(pw)

hl = hashlib.sha256()

hl.update(pw.encode("utf-8"))
print(hl.digest())
print(hl.hexdigest()) """



""" import hashlib
import os

def pwInsert():
    if os.path.exists("pw.txt"):
        pw = input("input pass: ")
        hs = hashlib.sha256()
        hs.update(pw.encode("utf-8"))
        with open('pw.txt', 'r') as fp:
            return hs.hexdigest() == fp.read()
    else :
        return True
    
if pwInsert():
    pw =input("new pass: ")
    with open('pw.txt', 'w') as fp:
        hs = hashlib.sha256()
        hs.update(pw.encode("utf-8"))
        fp.write(hs.hexdigest())
else :
    print("not allow password") """



""" import platform as pf

pn = pf.uname()
print(pn)

pm = pf.machine()
print(pm)

pp = pf.processor()
print(pp)

ps = pf.system()
print(ps) """



""" import urllib.request as ur

# url = 'https://www.google.com'
url = "https://www.daum.net"

res = ur.urlopen(url)
web = res.read()

with open("ul2.html", "wb") as fp:
    fp.write(web)

print(web) """



""" import http.client as hc

url = "www.daum.net"
conn = hc.HTTPSConnection(url)
conn.request("GET", "/v/20231106170354285")

r = conn.getresponse()

with open("ulrp.html", "wb") as fp:
    fp.write(r.read())

conn.close()

print(r) """



""" import requests

url = "https://www.google.com"
res = requests.get(url)
web = res.content

with open("ulrp.html", "wb") as fp:
    fp.write(web) """


""" import time

def counter(str_name):
    for i in range(50000):
        print(f"Countdown {i}, name : {str_name}\n")

start = time.time()
for i in range(3) :
    counter(f"num{i}")
end = time.time()
    
print("single end", end - start) """




""" import time
import threading

def counter(str_name):
    for i in range(50000):
        print(f"Countdown {i}, name : {str_name}\n")

start = time.time()
thread1 = threading.Thread(target=counter, args=("1num",))
thread2 = threading.Thread(target=counter, args=("2num", ))
thread3 = threading.Thread(target=counter, args=("3num", ))

thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()
end = time.time()

print("multi thread end", end - start) """



""" import time
import multiprocessing

def counter(str_name):
    for i in range(50000):
        print(f"Countdown {i}, name : {str_name}\n")

start = time.time()
process1 = multiprocessing.Process(target=counter, args=("1num",))
process2 = multiprocessing.Process(target=counter, args=("2num",))
process3 = multiprocessing.Process(target=counter, args=("3num",))

process1.start()
process2.start()
process3.start()

process1.join()
process2.join()
process3.join()
end = time.time()

print("multi processing end", end - start) """



""" def main() :
    print("hello world")

def run() :
    print("hello python")

if __name__ == "__main__":
    run()
    main() """