import scapy.all as scp
import socket

#socket.inet_ntoa(fcntl.ioctl(socket.socket(socket.AF_INET, socket.SOCK_DGRAM), 
#                                 35099, struct.pack('256s', iface))[20:24])

eth = scp.Ether(dst = "ff:ff:ff:ff:ff:ff")
arp = scp.ARP(pdst = "198.13.13.0/16") 
ans, unans = scp.srp(eth / arp, timeout = 2)

print("        IP -- MAC")
for send, recv in ans:
    print recv.sprintf(r"%ARP.psrc% -- %Ether.src%")

