from scapy.all import *
import argparse
from pdb import pm
from pprint import pprint as pp # souvent utilisé en scapy pour faire du pretty print

MAX_TTL = 30
DST = "8.8.8.8"
TIMEOUT = 1

##########################
parser = argparse.ArgumentParser("My traceroute")
parser.add_argument("dst", help="Target IP")
parser.add_argument("--timeout", type=int, default=1)
parser.add_argument("--max-ttl", type=int, default=30)
options = parser.parse_args()
##########################

# Création d'une liste de paquets que je vais envoyé
def icmp_fast():
    pkts = [
        IP(dst=options.dst, ttl=ttl)/ICMP(seq=ttl)
        for ttl in range(1, options.max_ttl)
    ]
    ans, unans = sr(pkts, verbose=False, timeout=options.timeout) # ensuite j'envoies mon paquet
    
    # ttl -> IP
    t2ip = {}
    for pkt in unans:
        t2ip[pkt[IP].ttl] = "*"
    
    # Handle answered packets
    # Oon peut lvoir le pkt envoyé et le retour obtenu
    # comme qa est un tuple, on auait pu écrire query, response
    for qa in ans:
        t2ip[qa.query[IP].ttl] = qa.answer[IP].src
    
    # parcourir le dico --> mais c'est pas trié donc pas ouf 
    #for ttl, ip in t2ip.items():
    #    print(f"{ttl}. {ip}")

    # parcourir le dico trié directement
    for ttl, ip in sorted(t2ip.items(), key= lambda x:x[0]):
        print(f"{ttl}. {ip}")

def icmp_slow():

    for ttl in range(1, MAX_TTL):
        pkt = IP(dst=options.dst, ttl=ttl) / ICMP(type="echo-request")
        ans, _ = sr(pkt, verbose=False, timeout=options.timeout)
        if ans is None:
            ip = "*"
        else:
            print(list(ans[IP]))
            print(type(ans))
            ips = [response[IP].src if IP in response else "N/A" for _, response in ans]
            ip = ", ".join(ips)
        
        print(f"{ttl}. {ip}")
        
        if options.dst in ips:
            break

icmp_fast()