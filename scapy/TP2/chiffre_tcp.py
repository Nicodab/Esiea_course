from scapy.all import *
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad, unpad
import base64

# Clé de chiffrement AES (16, 24 ou 32 octets pour AES-128, AES-192 ou AES-256)
encryption_key = b'mysecretkey12345'

def encrypt_message(message):
    cipher = AES.new(encryption_key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(message.encode('utf-8'), AES.block_size))
    iv = base64.b64encode(cipher.iv).decode('utf-8')
    encrypted_message = base64.b64encode(ciphertext).decode('utf-8')
    return f"{iv}:{encrypted_message}"

def send_encrypted_broadcast_message(message, iface, broadcast_ip='192.168.1.255'):
    # Chiffrer le message
    encrypted_message = encrypt_message(message)

    # Créer un paquet personnalisé avec le message chiffré
    packet = IP(dst=broadcast_ip) / TCP(dport=12345, flags="S") / Raw(load=encrypted_message)

    # Envoyer le paquet en broadcast
    send(packet, iface=iface)

# Définir le message à envoyer
message_to_send = "gabi le ptit zizi"

# Définir l'interface réseau à utiliser (par exemple, 'eno1' pour Ethernet)
interface = 'eno1'

# Envoyer le message chiffré en broadcast au sous-réseau
for i in range (1, 3000):
    send_encrypted_broadcast_message(message_to_send, interface)

# Mettre toute nos requetes dans un tzableau pour les passer en bytes avec la f° bytes j'imagine, puis 'sendp'