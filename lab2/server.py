from socket import *
import sys

def main():
	# other clients assume that DNS server is bound to port 53.
	serverName 		= '127.0.0.1'
	serverPort 		= 8090
	serverSocket 	= socket(AF_INET, SOCK_DGRAM)
	serverSocket.bind((serverName, serverPort))
	while 1:
		data, addr 	= serverSocket.recvfrom(512)
		response 	= generateResponse(data)
		y 			= serverSocket.sendto(response, addr)

# creating dns response
def generateResponse(data):
	DOMAIN, typ, clas, dname_b = getQuestion(data[12:])
	HEADER 		 = getHeader(data[:12],DOMAIN)
	TYPE 		 = (1).to_bytes(2, byteorder = 'big')
	CLASS 		 = (1).to_bytes(2, byteorder = 'big')
	TTL 		 = (400).to_bytes(4, byteorder = 'big')
	RDLENGTH 	 = (4).to_bytes(2, byteorder = 'big')
	RDATA 		 = (12).to_bytes(1, byteorder = 'big') + (12).to_bytes(1, byteorder = 'big') + (12).to_bytes(1, byteorder = 'big') + (12).to_bytes(1, byteorder = 'big')
	if DOMAIN != ['www','james','bond']:
		RDATA 		 = (0).to_bytes(1, byteorder = 'big') + (0).to_bytes(1, byteorder = 'big') + (0).to_bytes(1, byteorder = 'big') + (0).to_bytes(1, byteorder = 'big')
	else :
		RDATA 		 = (10).to_bytes(1, byteorder = 'big') + (10).to_bytes(1, byteorder = 'big') + (10).to_bytes(1, byteorder = 'big') + (10).to_bytes(1, byteorder = 'big')
	return HEADER + dname_b + TYPE + CLASS + b'\xc0\x0c' + TYPE + CLASS + TTL + RDLENGTH + RDATA

# creating header for the packet
def getHeader(data, DOMAIN):
	ID 		 = data[:2]
	if DOMAIN == ['www','james','bond']:
		FLAG 	 = int('1' + '0000' + '1' + '0' + '0' + '0' + '000' + '0000', 2).to_bytes(2, byteorder = 'big')
	else:
		FLAG 	 = int('1' + '0000' + '1' + '0' + '0' + '1' + '000' + '0011', 2).to_bytes(2, byteorder = 'big')	
	# 		 (QR + OPCODE + AA + TC + RD + RA + Z  + RCODE)
	QDCOUNT	 = (1).to_bytes(2, byteorder = 'big')
	ANCOUNT	 = (1).to_bytes(2, byteorder = 'big')
	NSCOUNT	 = (0).to_bytes(2, byteorder = 'big')
	ARCOUNT	 = (0).to_bytes(2, byteorder = 'big')
	return ID + FLAG + QDCOUNT + ANCOUNT + NSCOUNT + ARCOUNT

# extracting the domain form the query
def getQuestion(data):
	DOMAIN 	= []
	tmp 	= ''
	length 	= 0
	index 	= 0
	for i in data:
		index = index + 1
		if(length != 0):
			tmp 	= tmp + chr(i)
			length 	= length - 1
		else :
			DOMAIN.append(tmp)
			tmp 	= ''
			length 	= int(i)
			if(int(i) == 0):
				break
	DOMAIN 	= DOMAIN[1:]
	TYPE 	= data[index:index + 2]
	index 	= index + 2
	CLASS 	= data[index:index + 2]
	return (DOMAIN, TYPE, CLASS, data[:index - 2])

main()
