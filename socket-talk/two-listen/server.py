#!/usr/bin/python

import socket, os

host='0.0.0.0'
port=12345

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host,port))
s.listen(1)

os.fork()

while True:
	clientsock,clientaddr = s.accept()
	clientsock.sendall("server pid: " + str(os.getpid()))
