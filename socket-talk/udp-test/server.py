#!/usr/bin/python

import sys, socket

if len(sys.argv) == 1:
	print sys.argv[0] + '[tcp|udp] ip port [reuse | bool]'
	exit(0)

if 'tcp' == sys.argv[1]:
	bltcp = True
	socket_type = socket.SOCK_STREAM
else:
	bltcp = False
	socket_type = socket.SOCK_DGRAM

s = socket.socket(socket.AF_INET, socket_type)

if 'true' == sys.argv[4]:
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind((sys.argv[2], int(sys.argv[3])))

if bltcp:
	s.listen(1)

while True:
	if bltcp:
		clientsock, clientaddr = s.accept()
		print("got connect from: ", clientsock.getpeername())
	else:
		clientdate,clientaddr = s.recvfrom(2048)
		print("got connect from:" + str(clientaddr) + " data: " + clientdate)

