#!/usr/bin/python2
#encode: utf-8
import socket
import os
import time

Host = "172.16.9.102"
Port = 5005

sock_udp = socket.socket(socket.AF_INET, # Internet 
				 socket.SOCK_DGRAM)  # UDP
# Faz o bind local. Associa um socket com um IP e uma Porta.

n_pacotes = 5
pacotes_perdidos = 0
sock_udp.settimeout(0.5)
media = 0

print "Bem vindo ao Teste de RTT e Perda de Pacote"
time.sleep(1)


for i in range(n_pacotes):
	mensagem = 'a'
	sair = False;
	inicio = time.time()
	sock_udp.sendto(mensagem, (Host,Port))
	try:
		resposta = sock_udp.recv(1024)
	except socket.timeout :
		print "Pacote Perdido"
		continue
	fim = time.time()
	if mensagem != '':
		media = media+ (fim-inicio)
		print "Ping", ((fim-inicio)*1000), "ms"
	time.sleep(1)


qtd_pacote_enviado = n_pacotes - pacotes_perdidos
media = (media/qtd_pacote_enviado)*1000
print "tempo medio de RTT: ", media, "ms\n"
print "numero de pacotes perdidos: ", pacotes_perdidos, "\n"

sock_udp.close();
