import socket
import sys
#import struct

print(chr(255))
print(chr(0))
mac_address_raw = raw_input('Enter mac address (xx:xx:xx:xx:xx:xx):')
ip = raw_input('Enter ip address:')
destination_ip = (ip, 9)
mac_address_splited = mac_address_raw.split(':')

#print (mac_address_splited)

packet = ""
for i in range(6):
    print i
    packet += chr(255)

for e in mac_address_splited:
    packet += chr(int(e.upper(), 16))

for i in range(6):
    print i
    packet += chr(0)

#print(mac_address_final)

sct = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sct.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
sct.sendto(packet, destination_ip)
