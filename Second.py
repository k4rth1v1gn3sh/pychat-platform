from threading import Thread
import socket as sk

class sender(Thread):
    def __init__(self, msg, name):
        Thread.__init__(self)
        self.msg = msg
        self.name = name

    def run(self):
        while True:
            x = input()
            x = self.name + ' : ' + x
            self.msg.send(bytes(x, 'utf-8'))

class reciever(Thread):
    def __init__(self,msg):
        Thread.__init__(self)
        self.msg = msg

    def run(self):
        while True:
            x = self.msg.recv(100)
            print(x.decode('utf-8'))

name = input("Enter your name ")
c = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
c.connect(('127.0.0.1', 4096))

s1 = sender(c, name)
r1 = reciever(c)

s1.start()
r1.start()
