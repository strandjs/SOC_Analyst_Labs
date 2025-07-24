# tcpdump 

tcpdump is a powerful command-line packet analyzer that allows you to capture and inspect live traffic on a network. It is commonly used for quick triage, scripting, and environments where a GUI is not available.

---

## Installation
- **Linux**: `sudo apt install tcpdump`
- **macOS**: Pre-installed or use `brew install tcpdump`
- **Windows**: Use via WSL or with tools like WinDump

Make sure your user has privileges to capture traffic, or use `sudo`.

---

## Basic Syntax
```bash
tcpdump [options] [expression]
```
Examples:
```bash
tcpdump -i eth0
sudo tcpdump -i wlan0 port 80
```

![tcpdump example usage](https://i.ibb.co/wZzvGbt6/image.png)
---

## Common Use Cases for SOC Analysts
| Task                                | Command Example                                                  |
|-------------------------------------|------------------------------------------------------------------|
| Capture all traffic on eth0         | `tcpdump -i eth0`                                               |
| Filter by host IP                   | `tcpdump -i eth0 host 10.0.0.5`                                  |
| Filter by source/dest IP            | `tcpdump src 192.168.1.1` or `tcpdump dst 8.8.8.8`              |
| Filter by port                      | `tcpdump port 443`, `tcpdump tcp port 22`                       |
| Specific protocol                   | `tcpdump icmp`, `tcpdump udp`                                   |
| Save capture to file                | `tcpdump -w capture.pcap`                                       |
| Read from file                      | `tcpdump -r capture.pcap`                                       |
| Capture with timestamp              | `tcpdump -tttt -i eth0`                                         |
| Limit packet count                  | `tcpdump -c 100 -i eth0`                                        |

---

## Important Flags
| Flag        | Description                                |
|-------------|--------------------------------------------|
| `-i`        | Specify interface                         |
| `-n`        | Don't resolve hostnames                   |
| `-v` `-vv`  | Increase verbosity of output              |
| `-X`        | Show hex + ASCII dump of packets          |
| `-A`        | Show packet contents in ASCII             |
| `-c`        | Limit number of packets captured          |
| `-w`        | Write to file (.pcap format)              |
| `-r`        | Read from file                            |
| `-s`        | Snap length (use `-s 0` for full packet)  |

---

## Filtering Expressions (tcpdump syntax)
- IP filter: `host 192.168.1.1`
- Port filter: `port 443`
- Combine filters: `tcp and port 443 and host 192.168.1.10`
- Exclude: `not port 22`
- Complex: `(src 10.0.0.5 and dst port 80) or icmp`

---

## Use Cases in SOC
- Confirm if malware beaconed to a C2 server
- Capture suspicious outbound connections
- Verify DNS tunneling
- Capture evidence during live response
- Triage alerts when SIEM logs are inconclusive

---

## Exporting and Analyzing
- Captures are saved in `.pcap` format and can be opened in Wireshark:
```bash
tcpdump -i eth0 -w suspicious.pcap
```
- Combine with other tools (e.g., `grep`, `awk`, `cut`) for parsing in scripts

---

## Best Practices
- Always specify interface with `-i`
- Use `-n` to avoid DNS delay unless hostname resolution is needed
- Keep captures short or limited with `-c` or filters to avoid large files
- Avoid running without filters in production environments

---

## Resources
- [tcpdump man page](https://www.tcpdump.org/manpages/tcpdump.1.html)
- [tcpdump examples](https://danielmiessler.com/study/tcpdump/)


---