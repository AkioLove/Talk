#!/usr/bin/python

import sys, socket

if len(sys.argv) == 1:
	print sys.argv[0] + 'ip port [reuse | bool]'
	exit(0)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if 'true' == sys.argv[3]:
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)

s.bind((sys.argv[1], int(sys.argv[2])))

s.listen(1)

while True:
	clientsock, clientaddr = s.accept()
	print("got connect from: ", clientsock.getpeername())

