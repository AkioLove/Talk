#!/usr/bin/python

import sys, socket, time

SYSTEMD_FIRST_SOCKET_FD = 3

time.sleep(20)

s = socket.fromfd(SYSTEMD_FIRST_SOCKET_FD, socket.AF_INET, socket.SOCK_STREAM)

while True:
	clientsock, clientaddr = s.accept()
	clientsock.sendall("socker fd: " + str(clientsock.fileno()) + ", got connect from: " + str(clientsock.getpeername()))

