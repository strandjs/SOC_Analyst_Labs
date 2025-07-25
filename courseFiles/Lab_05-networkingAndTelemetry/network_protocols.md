# Key Network Protocols for SOC Analysts

## DNS (Domain Name System)
- **Purpose**: Resolves domain names to IP addresses.
- **Port**: UDP 53 (sometimes TCP 53)
- **SOC Relevance**:
  - Detect domain generation algorithms (DGA)
  - Unusual domain lookups (ex: `.xyz`, newly registered)
  - DNS Tunneling

**Example Log Entry**:
```
Query: suspicious-domain[.]com
Response IP: 192.0.2.123
```

---

## HTTP (HyperText Transfer Protocol)
- **Purpose**: Web communication (insecure)
- **Port**: TCP 80
- **SOC Relevance**:
  - Indicators of compromise (IOCs) in URLs
  - Unusual user-agent strings or command-and-control (C2) traffic

**Example Indicators**:
```
GET /malicious.js HTTP/1.1
Host: attacker-site.com
```

---

## HTTPS (HTTP Secure)
- **Purpose**: Encrypted web traffic
- **Port**: TCP 443
- **SOC Relevance**:
  - Cannot see payloads, but metadata (SNI, certs) still useful
  - Monitor for self-signed or expired certificates
  - JA3 fingerprinting for TLS client/server behavior

---

## SSH (Secure Shell)
- **Purpose**: Remote shell access
- **Port**: TCP 22
- **SOC Relevance**:
  - Brute-force attempts
  - Unauthorized access
  - Lateral movement
  - Abnormal usage outside admin hours

---

## RDP (Remote Desktop Protocol)
- **Purpose**: Remote desktop access to Windows systems
- **Port**: TCP/UDP 3389
- **SOC Relevance**:
  - Target for brute-force or exploitation
  - Detection of external RDP attempts
  - Beaconing or unexpected RDP session initiations

---

## SMB (Server Message Block)
- **Purpose**: File and printer sharing in Windows environments
- **Port**: TCP 445
- **SOC Relevance**:
  - Common target for lateral movement (ex: EternalBlue exploit)
  - Used for file transfers and service enumeration

---

## ICMP (Internet Control Message Protocol)
- **Purpose**: Network diagnostics (ex: ping)
- **Port**: N/A (Layer 3 protocol)
- **SOC Relevance**:
  - Can indicate reconnaissance (ex: ping sweeps)
  - May be used in covert channels (ICMP tunneling)

---

## FTP (File Transfer Protocol)
- **Purpose**: Transfer files between systems
- **Port**: TCP 21
- **SOC Relevance**:
  - Insecure; credentials are sent in plaintext
  - May be used by attackers to exfiltrate data

---

## LDAP (Lightweight Directory Access Protocol)
- **Purpose**: Access and maintain distributed directory information
- **Port**: TCP/UDP 389 (LDAPS: TCP 636)
- **SOC Relevance**:
  - Reconnaissance and enumeration in Active Directory environments
  - Abnormal queries or excessive lookups can indicate compromise

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

