# NetFlow vs Full Packet Capture

## NetFlow (Metadata-Only)
- Originally developed by Cisco, NetFlow provides summarized network flow metadata.
- Does **not** include payload, only metadata about traffic flows.
- Widely supported (NetFlow, IPFIX, sFlow are variants)

### NetFlow Fields:
- Source/Destination IP & Port
- Protocol (TCP, UDP, ICMP)
- Number of packets
- Number of bytes
- Start and end timestamps
- Interface identifiers (ingress/egress)
- Flow direction

### Advantages:
- Lightweight, scalable
- Good for traffic patterns, anomaly detection, volumetrics
- Often used in large networks to detect DDoS, scanning, and beaconing

### Limitations:
- No packet contents (can't see commands, data exfiltration, malware)
- Not suitable for detailed forensics

### Example:
```
Src IP: 10.0.0.5 -> Dst IP: 172.16.0.1
Protocol: TCP
Bytes: 1540
Packets: 10
```

---

## Full Packet Capture (PCAP)
- Captures the entire content of each packet, including headers and payloads
- Tools: Wireshark, tcpdump, Zeek (for indexing), Arkime

### Advantages:
- Enables deep forensic analysis
- Useful for malware reverse engineering
- Detects zero-day and custom exploits

### Limitations:
- Requires large storage
- Privacy concerns (captures passwords, PII)
- Needs indexing/metadata tools for scalability

---

## Comparison

| FEATURE            | NetFlow              | Full Packet Capture         |
|--------------------|----------------------|------------------------------|
| **Data Type**       | Flow metadata only   | Full content + headers       |
| **Detail Level**    | Medium               | Very high                    |
| **Storage Needs**   | Low                  | High                         |
| **Use Cases**       | Trend analysis, alerting | Deep forensics, payload analysis |
| **Tooling**         | nfcapd, YAF, SiLK     | Wireshark, tcpdump, Arkime  |
| **Privacy Risk**    | Low                  | High                         |

---
## Resources

- [IANA Service Name and Port Number Registry](https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml)
- [Cloudflare Learning Center: What is DNS?](https://www.cloudflare.com/learning/dns/what-is-dns/)
- [Blog about Protocols](https://www.geeksforgeeks.org/computer-networks/types-of-network-protocols-and-their-uses/)
- [Zeek Documentation](https://docs.zeek.org/en/current/)
- [Suricata IDS/IPS](https://docs.suricata.io/en/latest/)
- [MITRE ATT&CK Network-Based Techniques](https://attack.mitre.org/tactics/TA0011/)
- [Wireshark User Guide](https://www.wireshark.org/docs/wsug_html_chunked/)
- [tcpdump Cheat Sheet](https://danielmiessler.com/study/tcpdump/)
- [ibm blog releted to netflow](https://www.ibm.com/think/topics/netflow)
