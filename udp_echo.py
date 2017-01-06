from socket import *
from time import ctime

HOST = ''
PORT = 8743
BUFSIZ = 128
ADDR = (HOST, PORT)

udpServer = socket(AF_INET, SOCK_DGRAM)
udpServer.bind(ADDR)

while True:
    print('waiting for message...')
    data, addr = udpServer.recvfrom(BUFSIZ)
    udpServer.sendto(data, addr)
    print('...received from and returned to:', addr)
	
udpServer.close()

