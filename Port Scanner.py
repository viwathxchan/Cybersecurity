# CEH
EH Project(s)

Port Scanner

import socket
from IPy import IP


def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.10)
        sock.connect((ipaddress, port))
        print('[+] Port' + str(port) + ' Is Open')
    except:
        print('[-] Port' + str(port) + ' Is Closed')
        
ipaddress = input('[+] Enter Target To Scann: ')

for port in range (1, 500):
    scan_port(ipaddress, port)
