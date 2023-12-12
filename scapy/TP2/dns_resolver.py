# Afficher l'addr IP de la requete dns demandé
from scapy.all import *

def resolve_dns_manually(query_name, dns_server="8.8.8.8"):
    # Construire une requête DNS personnalisée
    dns_request = IP(dst=dns_server) / UDP(dport=53) / DNS(
        id=42,  # Identifiant de la requête
        rd=1,   # Recursive Desired
        qd=DNSQR(qname=query_name, qtype="A"),  # Type de requête A (adresse IPv4)
    )

    # Envoyer la requête DNS
    dns_response = sr1(dns_request, verbose=False)

    # REVOIR CAR CA RENVOIE QUE UN SEUL RDATA ALORS QUE Y'EN A 2
    if dns_response and DNS in dns_response and dns_response[DNS].ancount > 0:
        # Extraire l'adresse IP de la réponse DNS
        resolved_ip = dns_response[DNSRR].rdata
        print(f"Resolved IP for {query_name}: {resolved_ip}")
    else:
        print(f"Unable to resolve {query_name}")

# Test de la fonction avec un nom de domaine
resolve_dns_manually("perdu.com")
