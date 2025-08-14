import csv
from scapy.all import rdpcap
pkts = rdpcap('capture.pcap')
with open('iocs.csv','w',newline='') as f:
    w = csv.writer(f)
    w.writerow(['type','value'])
    for p in pkts:
        if p.haslayer('DNS') and p.getlayer('DNS').qd:
            w.writerow(['dns', p.getlayer('DNS').qd.qname.decode()])
        if p.haslayer('Raw') and b'Host: ' in bytes(p['Raw']):
            try:
                host = bytes(p['Raw']).split(b'Host: ')[1].split(b"\r\n")[0].decode()
                w.writerow(['host', host])
            except Exception:
                pass
            