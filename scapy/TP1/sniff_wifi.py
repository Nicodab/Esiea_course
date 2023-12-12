from scapy.all import *

seen = set()

def callback(pkt):
    
    if Dot11Beacon in pkt:
        # (BSSID, ESSID)
        info = (pkt.addr2, pkt.info)
        if info not in seen:
            seen.add(info)
            print(f"[{info[0]}, {info[1]}]")
        elif Dot11ProbReq in pkt:
            print(f"ProbeReq: {pkt.addr2} - {pkt.info}")

sniff(iface = "eno1", prn=callback, lfilter=lambda x : Dot11Beacon)

