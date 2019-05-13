import scapy.all as scp

eth = scp.Ether(dst = "ff:ff:ff:ff:ff:ff")
arp = scp.ARP(pdst = "172.22.0.0/16")
ans, unans = scp.srp(eth / arp, timeout = 2)

print("        IP -- MAC")
for send, recv in ans:
    print recv.sprintf(r"%ARP.psrc% -- %Ether.src%")

