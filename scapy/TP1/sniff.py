from scapy.all import *

def callback(packet):
    if "IP" in packet and "ICMP" in packet:
        ip_src = packet["IP"].src
        ip_dst = packet["IP"].dst
        payload = repr(packet["ICMP"].payload)

        print(f"Source IP: {ip_src}, Destination IP: {ip_dst}")
        print(f"ayload:\n{payload}\n")

sniff(prn=callback, filter="icmp", store=0)
