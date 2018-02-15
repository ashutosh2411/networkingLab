import socket
import struct
import time
import sys
import select

from random import randint

ICMP_ECHO_REQUEST 	= 8
ICMP_CODE		 	= 0

def checksum(source_string):
	temp 	= 0
	end		= (len(source_string)/2)*2
	count 	= 0
	while count < end:
		thisVal = ord(source_string[count + 1])*256 + ord(source_string[count])
		temp 	= temp + thisVal
		temp 	= temp & 0xffffffff # Necessary?
		count 	= count + 2

	if end < len(source_string):
		temp 	= temp + ord(source_string[len(source_string) - 1])
		temp 	= temp & 0xffffffff # Necessary?

	temp 	= (temp >> 16)  +  (temp & 0xffff)
	temp 	= temp + (temp >> 16)
	answer 	= ~temp
	answer 	= answer & 0xffff

	# Swap bytes
	answer 	= answer >> 8 | (answer << 8 & 0xff00)
	return answer

#id global 
ID = randint(0, 0xFFFF)

def icmp():
	seq 	= 1
	ck_sum 	= 0
	#kernel will fill correct checksum
	icmp_pckt 	= struct.pack("BBHHH", ICMP_ECHO_REQUEST, ICMP_CODE, ck_sum, ID, seq) 
	check_sum 	= checksum(icmp_pckt)
	icmp_pckt 	= struct.pack("BBHHH", ICMP_ECHO_REQUEST, ICMP_CODE, socket.htons(check_sum), ID, seq)
	return(icmp_pckt)
	
def main():
	sock 	= socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
	try:	
		ip 	= socket.gethostbyname(ping_to)
	except socket.error (errno, msg):
		print('invalide website')
		return	
	sock.sendto(icmp(), (ip, 0))
	sent_time 	= time.time()
	sock.settimeout(1)
	while(1):
		packet, addr 	= sock.recvfrom(1024)
		rec_time 		= time.time()
		icmp_header 	= packet[20:28]
		ttl 			= struct.unpack('B', packet[8])
		type_, code, checksum, p_id, sequence = struct.unpack('BBHHH', icmp_header)
		if(p_id == ID and type_ == 0):
			print addr
			print 'req_recieved in time :  ', rec_time - sent_time
			print 'sequence number :  ', sequence
			print 'time to live :  ', ttl[0]
			return
	print('no request recived')

ping_to = sys.argv[1]
main()