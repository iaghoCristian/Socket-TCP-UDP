#!/usr/bin/python2
#encode: utf-8
import socket
import os

Host = "localhost"
Port = 5005

sock_udp = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
                     
# Faz o bind local. Associa um socket com um IP e uma Porta.
sock_udp.bind((Host, Port))

while True:
	mensagem, addr = sock_udp.recvfrom(1024) # Tamanho do buffer eh 1024 bytes
	sock_udp.sendto(mensagem,addr)
	print "Ping Recebido"
