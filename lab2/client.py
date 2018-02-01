from socket import *
import sys

def main(domain_name='www.jamesbond.com',serverName='127.0.0.1'):
	serverPort 		= 53
	clientSocket 	= socket(AF_INET, SOCK_DGRAM)
	request 		= generateRequest(domain_name)
	clientSocket.sendto(request, ( serverName ,serverPort) )
	data, server 	= clientSocket.recvfrom(1024)
	ip 				= decryptResponse(data[12:] ,data[6:8]) # data[6:8] :- no. of answers
	for i in ip:
		print(i)
	clientSocket.close()

def generateRequest(domain):
	header 	= generateHeader()
	domain	= encryptDomain(domain)
	return header + domain


def encryptDomain(domain):
	encr 	= b''
	count 	= 0
	for i in domain[::-1]:
		if i=='.' :
			encr =  int(count).to_bytes(1,byteorder='big') + encr
			count = 0
			continue
		encr = int.from_bytes(i.encode(), byteorder='big').to_bytes(1,byteorder='big') + encr
		count = count+1
	encr =  int(count).to_bytes(1,byteorder='big') +encr
	return encr + b'\x00' + b'\x00\x01' + b'\x00\x01' 
	# domain + end + class + type

def generateHeader():
	ID 		= (512).to_bytes(2,byteorder='big')
	FLAG 	= int('1' + '0000' + '0' + '0' + '0' + '0' + '000' + '0000', 2).to_bytes(2, byteorder = 'big')
	# 		 (QR + OPCODE + AA + TC + RD + RA + Z  + RCODE)
	QDCOUNT = (1).to_bytes(2,byteorder='big')
	ANCOUNT = (0).to_bytes(2,byteorder='big')
	NSCOUNT = (0).to_bytes(2,byteorder='big')
	ARCOUNT = (0).to_bytes(2,byteorder='big')
	return ID + FLAG + QDCOUNT + ANCOUNT  + NSCOUNT + ARCOUNT

def decryptResponse(data ,ans_num):
	data = getDomain(data)
	data = data[4:] #class ,type
	ip=[]
	for j in range(int.from_bytes(ans_num, byteorder='big')):
		data = data[2:]
		data = data[4:] #class ,type
		data = data[4+2:] ## ttl ,rdlength
		tmp =''
		for i in range(4):
			tmp = tmp + str(int.from_bytes(data[i:i+1], byteorder='big'))+'.'
		ip.append( tmp[:-1])
		data = data[4:]
	return ip

def getDomain(data):
	length	= 0
	index	= 0
	for i in data:
		index 	= index+1
		if(length !=0):
			length 	= length -1
		else :
			length 	= int(i)
			if(int(i) == 0):
				break
	return data[index:]

try:
	main(sys.argv[1] , sys.argv[2]) #domain name / ip of server
except :
	main()	