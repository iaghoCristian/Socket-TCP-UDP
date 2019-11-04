#!/usr/bin/env python

import socket

TCP_IP = 'localhost'
TCP_PORT = 5006

socket_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_tcp.bind((TCP_IP, TCP_PORT))
socket_tcp.listen(1)
 

while True:
	conn, addr = socket_tcp.accept()
	mensagem = conn.recv(1024)
	print "Recebendo Mensagem"
	while mensagem:
		mensagem = conn.recv(1024)
		
	conn.close()

