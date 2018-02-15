from socket import *
from threading import *

HOST = "127.0.0.1"
PORT = 1503

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((HOST,PORT))
while 1 :
	send_message = raw_input('Send    : ')   
	clientSocket.send(send_message)
	if(send_message == 'exit'):
		break
	received_message = clientSocket.recv(1024)
	print 'Received:', received_message
clientSocket.close()