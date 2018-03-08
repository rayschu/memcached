# -*- coding: UTF-8 -*-
#!/usr/bin/env python
#Author:Rayschu Wang
#TODO: Memcached vul check in  UDP.

from socket import socket, AF_INET, SOCK_DGRAM
import sys
import time

now_time = time.strftime("%Y%m%d%H%M%S",time.localtime())
filename = sys.argv[1]

vul_name = "vulresult_" + now_time + ".txt"
novul_name = "novulresult_" + now_time + ".txt"
vul_result = open(vul_name,'a+')
novul_result = open(novul_name,'a+')

PORT = 11211
MAX_SIZE = 4096
TIME_OUT = 0.5
POC = '\x00\x00\x00\x00\x00\x01\x00\x00\x73\x74\x61\x74\x73\x0d\x0a'

ip_file = open(filename)
IP = ip_file.readline()
while IP:
#    print IP
    try:
        client = socket(AF_INET,SOCK_DGRAM)
        client.settimeout(TIME_OUT)
        client.sendto(POC, (IP, PORT))
        data =  client.recvfrom(MAX_SIZE)
        length = len(data[0])
        if length > 200 :
            print "The IP has vul of memcached: " + IP
            vul_result.write(IP)
        else:
#            print "The IP has no vul of memcached: " + IP
            novul_result.write(IP)
    except:
#        print "The IP has no vul of memcached: " + IP
        novul_result.write(IP)
    IP = ip_file.readline()

ip_file.close()
vul_result.close()
novul_result.close()
exit()
