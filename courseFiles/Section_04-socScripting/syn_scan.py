import csv
from scapy.all import IP, TCP, sr, conf
conf.verb = 0
target = '10.0.0.5'
ports = [22, 80, 443, 8080]
ans, _ = sr(IP(dst=target)/TCP(dport=ports, flags='S'), timeout=2)
open_ports = []
for s,r in ans:
    if r.haslayer(TCP) and (r[TCP].flags & 0x12):
        open_ports.append(r[TCP].sport)
with open('scan_results.csv','w',newline='') as f:
    w = csv.writer(f)
    w.writerow(['target','open_ports'])
    w.writerow([target, ';'.join(map(str, open_ports))])
print('Done :)')
