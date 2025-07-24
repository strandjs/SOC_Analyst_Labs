# Zeek 

Zeek (formerly known as Bro) is a powerful network security monitoring platform. Unlike traditional packet analyzers, Zeek operates as a network security engine that passively monitors traffic and generates rich logs describing network activity. For SOC Analysts, Zeek is invaluable for detecting anomalies, understanding protocol behavior, and performing incident response.

!!I was unable to install and configure zeek so this page was created from resources I found online

---

## Installation

- **Linux (Ubuntu/Debian)**:

  ```bash
  sudo apt install zeek
  ```

  Or compile from source via [https://zeek.org/get-zeek/](https://zeek.org/get-zeek/)

- **Security Onion**: Comes pre-installed

- **Zeek in Docker**:

  ```bash
  docker run --rm -it --net=host zeek/zeek zeek -i eth0
  ```

---

##  Zeek Architecture Overview

Zeek consists of multiple components:

- **Packet Capture** (via `libpcap`)
- **Event Engine** (parses protocols and extracts metadata)
- **Policy Scripts** (detect specific behaviors or extract logs)
- **Log Framework** (generates structured `.log` files)

Zeek uses a powerful scripting language for writing detection logic.

---

## Interface & CLI Tools

Zeek does not have a GUI; it works primarily through the command line and log files.

- **Basic Syntax**:
  ```bash
  zeek -i <interface>
  zeek -r <pcap_file>
  ```
- **Output**: Produces logs in the current directory (e.g., `conn.log`, `dns.log`, `http.log`, `notice.log`, etc.)

---

## Core Zeek Log Files (Essential for SOC)

| Log File       | Description                                                        |
| -------------- | ------------------------------------------------------------------ |
| `conn.log`     | All connections (source/destination IP, ports, protocol, duration) |
| `dns.log`      | DNS requests and responses                                         |
| `http.log`     | HTTP request/response metadata                                     |
| `ssl.log`      | TLS handshake data (JA3, certs, versions)                          |
| `files.log`    | Metadata about extracted files/transfers                           |
| `notice.log`   | Alerts and notable events from scripts                             |
| `weird.log`    | Protocol anomalies and unexpected behavior                         |
| `x509.log`     | Parsed SSL certificates                                            |
| `software.log` | Detected software on hosts                                         |
| `ssh.log`      | SSH handshake metadata                                             |
| `smtp.log`     | Email-related traffic (SMTP only)                                  |

---

## Zeek Scripts: Behavioral Detection

Zeek's power comes from its scripting engine. Examples:

### Detect long connections

```zeek
redef Notice::policy += {
  [$note=Conn::LongConnection, $priority=Notice::WARNING]
};
```

### Alert on cleartext password in HTTP

```zeek
event http_entity_data(c: connection, is_orig: bool, data: string) {
  if (data in /password=/) {
    print fmt("Password detected: %s", data);
  }
}
```

Scripts can be custom-built or use community ones from:

- [https://github.com/zeek/scripts](https://github.com/zeek/scripts)
- [https://packages.zeek.org/](https://packages.zeek.org/)

---

## Use Cases

| Use Case                    | Zeek Artifact           |
| --------------------------- | ----------------------- |
| Lateral movement            | `conn.log`, `ssh.log`   |
| DNS tunneling               | `dns.log`               |
| C2 beaconing                | `conn.log`, `http.log`  |
| Exfiltration via HTTP/FTP   | `files.log`, `http.log` |
| TLS anomalies (self-signed) | `ssl.log`, `x509.log`   |
| Protocol abuse              | `weird.log`             |
| Unauthorized remote access  | `ssh.log`, `conn.log`   |
| Email-based attacks         | `smtp.log`              |

---

## Useful Tools and Add-ons

- **ZeekCTL** – Cluster management tool
  ```bash
  zeekctl deploy
  zeekctl status
  ```
- **File carving**: Can extract files (enabled in config)
- **Intel framework**: Add threat intel to flag IOCs
- **Notice framework**: Send alerts to SIEM or syslog
- **Input framework**: Ingest feeds for detection (e.g., blacklists)

---

## TLS/SSL Analysis

Zeek can fingerprint TLS connections:

- **JA3 Fingerprinting**
- Certificate issuer and validity
- Weak TLS versions (e.g., SSLv3)

Use `ssl.log` and `x509.log` to detect expired, self-signed, or suspicious certs.

---

## Best Practices

- Periodically rotate and archive logs
- Forward logs to SIEM for correlation
- Watch `notice.log` and `weird.log` daily
- Write custom scripts for your use cases
- Leverage Zeek + Suricata (Security Onion) for layered detection

---

## Documentation & Learning Resources

- [Official Zeek Documentation](https://docs.zeek.org/)
- [Zeek Scripting Guide](https://docs.zeek.org/en/current/scripting/index.html)
- [Zeek Package Manager (zkg)](https://docs.zeek.org/projects/package-manager/en/stable/)

---
