from threading import Thread
import socket as sk

class sender(Thread):
    def __init__(self, msg):
        Thread.__init__(self)
        self.msg = msg

    def run(self):
        while True:
            x = input()
            x = 'Lucifer : ' + x
            self.msg.send(bytes(x, 'utf-8'))

class reciever(Thread):
    def __init__(self,msg):
        Thread.__init__(self)
        self.msg = msg

    def run(self):
        while True:
            x = self.msg.recv(100)
            print(x.decode('utf-8'))


c = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
c.bind(('127.0.0.1', 4096))
c.listen()
msg, address = c.accept()

s1 = sender(msg)
r1 = reciever(msg)

s1.start()
r1.start()
