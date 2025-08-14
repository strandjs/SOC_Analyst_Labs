from scapy.all import srp, Ether, ARP, conf
conf.verb = 0
ans, _ = srp(Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(pdst='10.0.0.0/24'), timeout=2)
for s,r in ans:
    print(f'{r.psrc} -> {r.hwsrc}')

    