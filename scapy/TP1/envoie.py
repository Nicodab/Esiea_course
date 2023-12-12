from scapy.all import IP, ICMP, srp, Ether, Raw

def send_icmp_broadcast(target_ip, iface):
    # Créer un paquet ICMP en utilisant Ether pour spécifier l'adresse de destination en broadcast
    packet = Ether(dst="ff:ff:ff:ff:ff:ff") / IP(dst=target_ip) / ICMP() / Raw(b"shradfine + shrafdine = bruh")

    # Envoyer le paquet et recevoir les réponses
    responses, _ = srp(packet, iface=iface, timeout=2, verbose=False)

    # Afficher les réponses reçues
    for _, response in responses:
        print(f"Réponse reçue de {response[IP].src}")

# Définir l'adresse IP cible (par exemple, '192.168.1.255' pour un réseau local)
target_ip = '192.168.1.255'

# Définir l'interface réseau à utiliser (par exemple, 'eth0' pour Ethernet)
interface = 'eno1'

# Envoyer les paquets ICMP en broadcast
send_icmp_broadcast(target_ip, interface)


