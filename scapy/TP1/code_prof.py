from scapy.all import *
from pdb import set_trace

def callback(pkt):
    hexdump(pkt[ICMP].payload) # ou ().load) c'est plaisant pour envoyer... .payload ça donne la couche Raw
    

    # Si un jour on reçoit un truc auquel on ,ne s'attend pas on récupère la trace 
    #if pkt[ICMP].type != 8:
    #    set_trace()
    
    # Ecrire du code

sniff(prn=callback, filter="icmp", store=0)

def myFun(pkt):
    return Dot11Beacon in pkt

myFun = lambda pkt: Dot11Beacon in pkt
