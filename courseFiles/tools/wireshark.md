# Wireshark

Wireshark is a powerful open-source network protocol analyzer used for capturing and analyzing packets in real time. It is an essential tool for any SOC Analyst to inspect suspicious network activity, troubleshoot issues, and perform deep packet inspection during investigations.

---

##  Installation
- **Linux**: `sudo apt install wireshark`
- **macOS**: Use Homebrew: `brew install --cask wireshark`
- **Windows**: Download from [wireshark.org](https://www.wireshark.org/download.html)

Ensure you have permissions to capture packets (ex: join the `wireshark` group or run with `sudo`).

---

##  Interface Overview

Wireshark has a multi-pane GUI with these main components:

![wireshark interface](https://i.ibb.co/sd23bmPv/Screenshot-2025-07-22-143031.jpg)

1. **Menu Bar**: File, Edit, View, Capture, Analyze, Statistics, etc.

![wireshark menu bar](https://i.ibb.co/xSgKxgTM/image.png)

2. **Main Toolbar**: Common actions (start/stop capture, save, open, restart)

![Wireshark main toolbar](https://i.ibb.co/qLtRHqnt/image.png)

3. **Filter Bar**: Where display filters are typed (ex: `http`, `ip.addr == 8.8.8.8`)

![Wireshark Filter bar](https://i.ibb.co/qYWsTYPP/image.png)

4. **Packet List Pane**: Top pane shows summary of captured packets (No., time, src/dst, protocol, info)

![Wireshark List Pane](https://i.ibb.co/t0XKcqJ/image.png)

5. **Packet Details Pane**: Down left pane shows selected packet dissected by protocol layers

![Wireshark Packet details pane](https://i.ibb.co/Jw9vytC4/image.png)

6. **Packet Bytes Pane**: Bottom pane shows raw packet data in hex and ASCII

![Wireshark Packet Bytes Pane](https://i.ibb.co/kV9PQD9n/image.png)

7. **Status Bar**: Displays file size, dropped packets, and more

![Wireshark Status Bar](https://i.ibb.co/PGCyJDtQ/image.png)

---

##  Basic Usage Workflow
1. **Select Interface**: Choose an active network interface (e.g., `eth0`, `wlan0`).
2. **Start Capture**: Click the blue shark fin icon.
3. **Stop Capture**: Click the red square.
4. **Filter Traffic**: Use display filters to narrow down to relevant packets.
5. **Inspect Packets**: Click on a packet to view details in the middle and bottom panes.

---

##  Common Display Filters for SOC

| Use Case                        | Filter Example                          |
|--------------------------------|-----------------------------------------|
| Filter HTTP traffic            | `http`                                  |
| Filter DNS traffic             | `dns`                                   |
| Filter IP address              | `ip.addr == 192.168.1.5`                |
| Filter specific protocol       | `tcp`, `udp`, `icmp`                    |
| Traffic to/from a port         | `tcp.port == 443`                       |
| Suspicious TCP flags           | `tcp.flags.syn == 1 && tcp.flags.ack == 0` |
| Only traffic between two IPs   | `ip.src==10.0.0.5 && ip.dst==10.0.0.7`  |
| Traffic over time              | Use Statistics > IO Graphs              |

---

##  Opening and Saving Captures
- Save capture: `File > Save As...` (.pcap or .pcapng format)
- Open capture: `File > Open`
- Export specific packets: `File > Export Specified Packets`

---

##  Useful Features

### 1. **Follow TCP Stream**
- Right-click a TCP packet → "Follow" → "TCP Stream"
- This will reconstructs the full conversation (ex: HTTP request/response)

### 2. **Protocol Hierarchy**
- `Statistics > Protocol Hierarchy`
- Shows protocol breakdown by % and packet count

### 3. **Endpoints and Conversations**
- `Statistics > Endpoints` — List of all IP/MAC addresses
- `Statistics > Conversations` — Active communication pairs

### 4. **IO Graphs**
- Graph network usage over time
- Useful for identifying peaks (e.g., DDoS or exfiltration)

### 5. **Expert Info**
- `Analyze > Expert Information`
- Shows warnings, errors, anomalies in traffic

---

##  Analyzing Encrypted Traffic
- **HTTPS/TLS**: You can't decrypt without SSL keys
- If you have the server private key and the session uses RSA key exchange:
  - Go to `Edit > Preferences > Protocols > TLS`
  - Add the key under (pre)master-secret log
- Use `JA3` fingerprinting for TLS client/server behavior

---

##  Use Cases for SOC Analysis
- Detect C2 communication
- DNS tunneling detection
- Exfiltration over HTTP/S
- Malware beaconing or periodic connections
- Unusual protocols in use
- Unauthorized RDP/SSH traffic
- Data leaks (PII in cleartext traffic)

---


##  Resources
- [Wireshark Display Filter Reference](https://www.wireshark.org/docs/dfref/)
- [Wireshark User Guide](https://www.wireshark.org/docs/wsug_html_chunked/)
- [Malware Traffic Analysis Lab](https://www.malware-traffic-analysis.net/)
- https://sw4pn1lp.github.io/wireshark/navgui.html

---