#!/usr/bin/python

import socket, time, os

host='0.0.0.0'
port=12345

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
## avoid "Address already in use" on server restart
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
print("process start, not bind socket yet, pid = ", os.getpid())

s.bind((host,port))
print("after bind port, sleep 20s")
time.sleep(20)

print("after listen port, sleep 20s")
s.listen(1)
time.sleep(20)

while True:
	print("accept connection, sleep 20s")
	clientsock,clientaddr = s.accept()
	print("got connect from: ", clientsock.getpeername())
	time.sleep(20)
	print("consume data: ", clientsock.recv(2048))

