from scapy.all import *
import argparse

MAX_TTL = 30
DST = "8.8.8.8"
TIMEOUT = 1

##########################
parser = argparse.ArgumentParser("My traceroute")
parser.add_argument("dst", help="Target IP")
parser.add_argument("timeout",type=int, default=1)
parser.add_argument("max-ttl",type=int, default=30)

##########################

for ttl in range(1, MAX_TTL):
    pkt = IP(dst=DST, ttl=ttl) # on laisse ça si on veut fdaire de l'ICMP et pas du TCP pour le traceroute/ICMP(type="echo-request")
    #pkt = pkt/TCP(dport=80) # --> Si on veut rajouter du TCP par dessus
    ans = sr1(pkt, verbose=False, timeout=TIMEOUT)
    ip = None
    if ans is None:
        print("*")
    else:
        ip = ans[IP].src
    print(f"{ttl}. {ip}")
    
    if ip == DST:
        break 