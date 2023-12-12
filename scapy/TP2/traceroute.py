from scapy.all import *

def traceroute(target_ip, max_hops=20):
    for ttl in range(1, max_hops + 1):
        # Créer un paquet ICMP Echo Request avec un TTL spécifié
        packet = IP(dst=target_ip, ttl=ttl) / ICMP(type="echo-request")

        reply = sr1(packet, timeout=1, verbose=False) # on met le timeout sinbon on reste bloqué

        if reply is None:
            print(f"{ttl}. * * *")
        elif IP in reply:
            ip_src = reply[IP].src
            print(f"{ttl}. {ip_src}")
            
            # si l'IP de answer est celle de la destination, terminer le traceroute
            if ip_src == target_ip:
                break

traceroute("8.8.8.8")
