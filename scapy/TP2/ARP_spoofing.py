from scapy.all import *

def broadcast_ping(target_ip, iface, timeout=2):
    # Créer un paquet ICMP Echo Request avec l'adresse IP de destination en broadcast
    packet = IP(dst=target_ip) / ICMP()

    # Envoyer le paquet en broadcast et recevoir les réponses
    responses, _ = srp(packet, iface=iface, timeout=timeout, verbose=False)

    # Afficher les adresses IP des hôtes qui ont répondu
    for _, response in responses:
        ip_src = response[IP].src
        print(f"Host responded: {ip_src}")

# Définir l'adresse IP cible en broadcast (par exemple, '192.168.1.255' pour un réseau local)
broadcast_ip = 'ff::ff::ff::ff::ff'

# Définir l'interface réseau à utiliser (par exemple, 'eth0' pour Ethernet)
interface = 'eno1'

# Envoyer les paquets ICMP en broadcast
broadcast_ping(broadcast_ip, interface)
