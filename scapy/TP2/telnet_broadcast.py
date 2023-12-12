from scapy.all import *

def send_telnet_broadcast_message(message, broadcast_ip='192.168.1.255', port=23):
    packet = IP(dst=broadcast_ip) / UDP(dport=port) / Raw(load=message)
    send(packet, verbose=False)

# Définir le message à envoyer
telnet_message = "laisse moi me telnet chez toi vite fait ???"

# Envoyer le message en broadcast
for i in range(1, 3000):
    send_telnet_broadcast_message(telnet_message)
