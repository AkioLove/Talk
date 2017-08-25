#!/usr/bin/python

import socket, os, time

host='0.0.0.0'
port=12345

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host,port))
s.listen(1)

for x in range(0, 4):
	pid = os.fork()
	if 0 == pid:
		break;

while True:
	clientsock,clientaddr = s.accept()
	clientsock.sendall("server pid: " + str(os.getpid()))
	time.sleep(30)
