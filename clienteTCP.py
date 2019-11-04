#!/usr/bin/env python

import socket
import time
import os

tcp_ip = '172.16.9.102'
tcp_port = 5006

socket_tcp = socket.socket(socket.AF_INET,
				socket.SOCK_STREAM)
socket_tcp.connect((tcp_ip, tcp_port))

print"Bem Vindo ao teste de vazao"
time.sleep(2)
arquivo = open("arquivo.txt")


mensagem = arquivo.read(1024)
inicio = time.time()
while mensagem:
	socket_tcp.send(mensagem)
	mensagem = arquivo.read(1024)
fim = time.time()

media = fim-inicio
tam = os.path.getsize("arquivo.txt")

vazao = ((tam*8)/media)/1000000

print "mensagem toda enviada"
print "Vazao = ", vazao , "Mbps"
socket_tcp.close()
