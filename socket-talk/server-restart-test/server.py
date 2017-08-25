#!/usr/bin/python

import socket

host='0.0.0.0'
port=12345

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen(1)

while True:
	clientsock,clientaddr = s.accept()
	print("got connect from: ", clientsock.getpeername())

