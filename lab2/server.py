from socket import *
from threading import *

def client_thread(connectionSocket ,addr):
	while 1 :
		message = connectionSocket.recv(1024)
		print"client send : "+ str(addr) +' : ' +message
		if(message =='exit'):
			connectionSocket.close()
			exit(1)
		connectionSocket.send(message)

HOST = "127.0.0.1"
PORT = 1503

server = socket(AF_INET,SOCK_STREAM)
server.bind(('',PORT))
server.listen(5)

while 1:
	connectionSocket, addr = server.accept()
	thread = Thread(target=client_thread, args=[connectionSocket ,addr])
	thread.start()