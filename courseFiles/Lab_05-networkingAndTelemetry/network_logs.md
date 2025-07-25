
# Understanding Network Logs

## What is a Network Log?
Network logs are structured records of events and traffic observed by network devices and monitoring tools such as firewalls, routers, IDS/IPS, and SIEM platforms. These logs provide visibility into who is communicating, what protocols are used, and whether the traffic is legitimate or suspicious.

---

## Typical Fields in Network Logs

| Field                   | Description                                  |
| ----------------------- | -------------------------------------------- |
| **Source IP**           | IP address initiating the connection         |
| **Destination IP**      | IP address receiving the connection          |
| **Source Port**         | Ephemeral port on the source device          |
| **Destination Port**    | Port for the service (e.g., 80 for HTTP)     |
| **Protocol**            | Transport layer protocol (TCP/UDP/ICMP)      |
| **Action**              | Outcome (e.g., allowed, denied, logged)      |
| **Bytes Sent/Received** | Amount of data transferred                   |
| **Packets**             | Number of packets transferred                |
| **Flags**               | TCP flags (e.g., SYN, ACK, FIN)              |
| **Application**         | Identified application or service            |
| **Timestamp**           | Time the event occurred                      |

### Sample Log (Zeek Format)
```
192.168.1.5 -> 93.184.216.34 TCP 443 "SSL" Bytes: 4321
```

---

## Log Sources and Use Cases

- **Firewall Logs**: Show traffic allowed/denied by firewall rules
- **Proxy Logs**: Record web browsing activity (URLs, domains)
- **IDS/IPS Logs**: Alert on detected malicious patterns
- **Endpoint Logs**: Provide insight into local process activity and network usage
- **SIEM Aggregated Logs**: Centralized log aggregation, correlation, alerting

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
