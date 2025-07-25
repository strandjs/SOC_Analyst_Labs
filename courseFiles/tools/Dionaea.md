# About
**Dionaea** is a low-interaction honeypot designed to capture malware and exploits targeting services such as
- SMB (port 445)
- HTTP (port 80)
- FTP (port 21)
- TFTP
- MSSQL
- SIP

It emulates vulnerable services, logs attacker interactions, and stores any malware that is dropped, **Dionaea** is especially useful for SOC analysts, threat researchers, and blue teams to understand attacker behavior and collect Indicators of Compromise (IOCs)

| Use Case  | Description |
| ------------- | ------------- |
| Cyber Deception  | Trick attackers into interacting with fake services |
| Threat Intelligence | Collect malware and IPs for IOC feeds |
| Malware Analysis | Capture real-world malware for sandbox analysis |
| Attack Surface Monitoring | Observe how attackers scan and probe services |

### Features
- Emulates multiple vulnerable services
- Captures malware binaries
- Logs interaction in JSON format or SQLite DB
- Can forward logs to SIEM or threat intel platforms
- Supports integration with tools like ELK, Splunk, or Cuckoo Sandbox

# Installation
- $`sudo dnf update -y`
- $<pre>sudo dnf install -y git gcc cmake make glib2-devel \
  libev-devel libcurl-devel openssl-devel \
  python3 python3-pip libpcap-devel sqlite-devel \
  libnl3-devel netfilter-devel</pre>
