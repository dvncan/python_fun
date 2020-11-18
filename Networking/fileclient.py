import socket
from time import *

s = socket.socket()

s.connect(("localhost", 6767))

fileName = input("Enter a file name:")

s.send(fileName.encode())
sleep(1)
content = s.recv(1024)

print(content.decode())
    
s.close()
