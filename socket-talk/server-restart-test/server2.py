#!/usr/bin/python

import socket

host='0.0.0.0'
port=1234

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
## avoid "Address already in use" on server restart
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host,port))
s.listen(1)

while True:
	clientsock,clientaddr = s.accept()
	print("got connect from: ", clientsock.getpeername())

