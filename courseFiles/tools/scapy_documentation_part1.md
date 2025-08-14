# Scapy - part 1

- For part 2, check out [scapy_documentation_part2.md](./scapy_documentation_part2.md)
- For lab, check out [scapy_lab.md](/courseFiles/Section_04-socScripting/scapy_lab.md)
- For lab solution, check out [scapy_lab_solution.md](/courseFiles/Section_04-socScripting/scapy_lab_solution.md)

# Introduction & Setup




## 1) What is Scapy?

Scapy is a Python library and interactive packet-manipulation tool designed for building, sending, receiving, parsing, and manipulating network packets. It combines a flexible scripting API with an interactive shell for rapid testing and prototyping.

Primary capabilities:

- **Craft:** Build arbitrary packets from the link layer up to application protocols by stacking protocol layers as Python objects.
- **Send/Receive:** Transmit packets on the wire (L2/L3) and capture responses synchronously or asynchronously.
- **Sniff:** Capture live traffic using pcap/raw sockets and apply BPF or Python filters.
- **Read/Write PCAPs:** Persist traffic to PCAP files and replay them later.
- **Dissect/Decode:** Parse packets into structured fields and support custom protocol definitions.

Common usages in a SOC context:

- Testing IDS/IPS and SIEM rules with ground-truth traffic.
- Replaying attack or benign traces to validate detection logic.
- Performing packet-level forensics and automated enrichment scripts.
- Automating network discovery and benign/malicious traffic generation for red-team/blue-team exercises.

## 2) How Scapy works (architecture & internals)

**Packet model & layering**

Scapy models packets as *layered* Python objects. Each protocol is a subclass of `Packet` with a `fields_desc` declaration that defines the format and semantics of that layer. To build a packet, you stack layers with the `/` operator, for example: `Ether()/IP()/TCP()/Raw("payload")`.

**Dissection & binding**

When Scapy receives raw bytes, it attempts to dissect them into known layers using its registered dissectors. Layer transitions are decided by protocol identifiers (e.g.; `Ether.type`, `IP.proto`, or port numbers). For custom or unknown protocols, Scapy represents leftover bytes as `Raw`. You can teach Scapy how to parse custom protocols using `bind_layers()`.

**Fields & automatic calculations**

Fields have types (e.g., `ByteField`, `ShortField`, `IPField`, `MACField`) that validate values and can compute defaults. Scapy can automatically compute certain fields (like checksums or length fields) when building a packet, unless explicitly set.

**Sending & receiving**

Scapy uses different mechanisms depending on OS and operation:

- **Linux:** raw sockets are commonly used for sending crafted packets. Sniffing can use `libpcap` or raw sockets (both require elevated privileges).
- **Windows:** requires Npcap/WinPcap to capture and send packets; often needs Administrator rights.
- **macOS:** uses libpcap for sniffing; raw sockets for some sends.

Higher-level convenience functions (`send`, `sendp`, `sr`, `srp`, `sniff`) wrap the lower-level details to let you focus on packet logic rather than socket plumbing.

**Performance trade-offs**

Scapy prioritizes flexibility and developer velocity over maximum throughput. It is excellent for prototyping, test automation, and forensic parsing, but not optimized for high wire-rate packet generation (use `tcpreplay` or specialized packet generators for very high throughput).

## 3) Installation & environment notes
>[!TIP]
>
> **Recommendation:** Use an isolated lab VM (or two VMs on a host-only network) for all active traffic generation and interception. This prevents accidental disruption of production networks.

### Requirements

- Python 3.8+ (some systems ship older versions; virtual environments are recommended).
- libpcap development headers on Linux for best sniffing support (`libpcap-dev` / `libpcap-devel`).
- Npcap on Windows (install with "WinPcap API-compatible mode"/"Support raw 802.11 traffic" as needed).

### Linux (recommended for lab)

Typical steps (Debian/Ubuntu):

```bash
sudo apt update
sudo apt install python3-pip python3-dev libpcap-dev build-essential
python3 -m pip install --upgrade pip
pip3 install scapy
```

Notes:

- Some distributions ship an older packaged `scapy` — `pip` installs the latest stable version.
- Consider using a virtual environment (`python3 -m venv venv && source venv/bin/activate`) to isolate dependencies. (My best advice if you don't want to strugle with errors😉)

### Windows

1. Install Python 3.8+ from python.org and add it to PATH.
2. Install Npcap (choose "Install Npcap in WinPcap API-compatible Mode" if you need WinPcap compatibility).
3. From an Admin PowerShell:

```powershell
python -m pip install --upgrade pip
pip install scapy
```

>[!IMPORTANT]
>
>- Administrative privileges are generally required to capture/send crafted packets.
>- Some features behave differently on Windows due to driver/OS-level differences.



### Optional extras & integrations

- `pip install scapy[complete]` installs optional dependencies for extended protocol support.
- Use `wrpcap()` to create PCAPs and open them in Wireshark for deeper analysis.

## 4) Privileges, safety, and legal reminders

**Privileges**

- Raw packet sends, low-level sniffing, and some interface operations require root/Administrator privileges. Prefer using dedicated lab VMs instead of personal or production hosts.

**Safety**

- Certain operations (ARP poisoning, SYN flooding, fuzzing) can disrupt networks or hosts. Run these only in isolated environments and with explicit permission.

**Legal & ethical considerations**

- Unauthorized scanning, spoofing, interception, or attack simulation on networks you don't own or manage may be unlawful. Always obtain written authorization before performing active tests on third-party infrastructure.

---
# Core Concepts & Objects


## 1. Packet object model

### Packet = single protocol layer

- Each protocol is a subclass of `Packet`. For example, `IP`, `TCP`, `Ether` are `Packet` types.
- A full network packet is a **stack** of these `Packet` objects glued together with the `/` operator: `Ether()/IP()/TCP()/Raw()`.

### How composition works

- When you write `A()/B()/C()`, Scapy creates objects for A, B, and C and links them as `A.payload = B`, `B.payload = C`, etc.
- Serialization (`bytes(pkt)` or `raw(pkt)`) walks the stack, serializes each layer, and concatenates results. During serialization Scapy may fill computed fields (checksums, lengths).

### Dissection (parsing incoming bytes)

- When Scapy receives raw bytes, it tries to match the outermost dissector (e.g., `Ether`) and then repeatedly uses the current layer's logic to decide the next layer.
- Decision points include: `Ether.type`, `IP.proto`, `TCP.dport`/`sport`, and other protocol-specific markers.
- Unknown bytes become `Raw` payload.

## 2. Fields: types, semantics, and computed behavior

Fields declare how a `Packet`'s bytes map to Python attributes.

### Basic field categories

- **Integer fields:** `ByteField`, `ShortField`, `IntField`, `LongField` — for fixed-size numeric values.
- **Network/address fields:** `IPField`, `MACField`, `HostField` — for addresses with validation.
- **Bit-level fields:** `BitField`, `FlagsField`, `BitEnumField` — when values occupy specific bits inside a byte/word.
- **String/bytes fields:** `StrFixedLenField`, `StrLenField` — fixed or variable-length text data.
- **Container/list fields:** `PacketListField`, `FieldListField` — used for sequences of sub-packets or repeated items.
- **Length helpers:** `FieldLenField`, `ShortEnumField` — used to tie lengths/counts to actual data content.

### Defaults & automatic computation

- Many fields accept `None` as a default. When the packet is built, Scapy computes sensible defaults (for example, `IP.len`, `IP.chksum`, `UDP.len`, `TCP.chksum`) unless you explicitly set them.
- You can force computation early with `p.build()` or by converting to bytes.

### Example: inspecting fields

```python
from scapy.all import IP, TCP
p = IP(dst='8.8.8.8')/TCP(dport=80)
print('Before build:', p[IP].chksum)
bytes(p)
print('After build:', p[IP].chksum)
```

## 3. Packet inspection utilities

- `p.show()` — deep, human-readable breakdown of the packet and fields.
- `p.summary()` — single-line summary (useful for lists of packets).
- `ls(Layer)` — lists the available fields for a layer and their types/defaults.
- `hexdump(p)` — hex + ASCII dump of the packet bytes.
- `raw(p)` / `bytes(p)` — get serialized bytes; useful when sending to raw sockets or saving to PCAP.

**Examples**

```python
p.show()
print(p.summary())
ls(TCP)
hexdump(p)
```

## 4. Layer access and safe field manipulation

### Common access patterns

- `p.haslayer(TCP)` — `True` if TCP layer exists.
- `p[TCP]` or `p.getlayer(TCP)` — get the TCP layer object (raises/returns `None` if absent with `getlayer`).
- `p[IP].src` — read/write IP source address.
- `p.getlayer(Raw)` — retrieve raw payload safely.

### Safe access idioms

```python
if p.haslayer(DNS) and p[DNS].qd:
    print('Query:', p[DNS].qd.qname)

tcp = p.getlayer(TCP)
if tcp:
    tcp.flags = 'S'
```

### Replacing or inserting layers

- To replace the payload of a layer: `p[IP].remove_payload(); p[IP].add_payload(new_layer)` or simpler `p = p/NEWPAYLOAD` (creates a new stack).
- Use `p.copy()` before heavy mutation if you need the original preserved.

## 5. Packet lists: sniff/rdpcap output handling

- `PacketList` behaves like a Python list with convenience methods.
- Useful methods: `packets.summary()`, indexing (`packets[0]`), slicing, and iteration.
- Filtering in Python is straightforward: `[p for p in pkts if p.haslayer(TCP) and p[TCP].dport==80]`.

**Example: unique IPs & top talkers**

```python
pkts = rdpcap('capture.pcap')
from collections import Counter
ips = [p[IP].src for p in pkts if p.haslayer(IP)]
print(Counter(ips).most_common(10))
```

## 6. Common built-in layers

### Link layer

- `Ether`: fields `src`, `dst`, `type`. Use `sendp()` to send `Ether()` frames.
- `Dot1Q`: VLAN tag. Often seen stacked: `Ether()/Dot1Q()/IP()`.

### ARP

- `ARP`: fields like `hwsrc`, `psrc`, `hwdst`, `pdst`, `op` (1=request, 2=reply).
- `srp(Ether()/ARP(...))` is a common ARP discovery idiom.

### Network layer

- `IP`: `src`, `dst`, `ttl`, `proto`, `flags`, `tos`.
- `IPv6`: similar fields, different handling. Use `IPv6()` when needed.
- `ICMP`: echo request/reply and types for errors.

### Transport layer

- `TCP`: `sport`, `dport`, `flags`, `seq`, `ack`, `window`.
  - Flags string examples: `'S'` (SYN), `'SA'` or `0x12` (SYN+ACK), `'FA'` (FIN+ACK).
- `UDP`: simple `sport`, `dport`, `len`.

### Application-ish layers

- `DNS`: `qd` (question), `an` (answer), `qdcount`, `ancount` — good for DNS exfil simulations.
- `Raw`: generic payload container when no parser exists.

## 7. Creating and binding custom protocols

>[!TIP]
>
>When you need Scapy to understand a proprietary or uncommon protocol, define it as a `Packet` subclass and use `bind_layers()`.

### Minimal custom layer example

```python
from scapy.all import Packet, ByteField, ShortField, bind_layers, IP

class MyProto(Packet):
    name = 'MyProto'
    fields_desc = [
        ByteField('version', 1),
        ShortField('length', 0),
    ]

bind_layers(IP, MyProto, proto=222)
```

### Binding by TCP/UDP port

```python
# If your protocol sits on UDP port 5555
bind_layers(UDP, MyProto, dport=5555)
```

### Advanced: conditional binding

- `bind_layers(Upper, Lower, condition=...)` can be used with lambda-like checks or field values to guide dissection.
- For complex cases implement `guess_payload_class()` in your Packet subclass.

## 8. Useful packet methods & helpers

- `p.copy()` — copy the packet (useful before mutation).
- `p.remove_payload()` — strip higher layers.
- `p.add_payload(x)` — attach new payload.
- `p.build()` — force packet assembly and field computation.
- `raw(p)` / `bytes(p)` — serialized raw bytes.
- `p.summary()` / `p.show()` — quick views.

**Example: force build and send**

```python
p = IP(dst='10.0.0.5')/TCP(dport=80)
bytes(p)  # calculates checksums
send(p)
```

## 9. Troubleshooting & common pitfalls

- **Missing layers after sniff**: Scapy may not dissect higher layers if it doesn't know the mapping (bind\_layers may be needed). Use `Raw` fallback to inspect bytes.
- **BPF vs lfilter confusion**: `filter` (BPF string) is executed in kernel space via libpcap; `lfilter` is Python-level and slower but can inspect decoded fields.
- **Windows oddities**: Ensure Npcap is installed in the correct compatibility mode; driver issues are a common source of errors.
- **Permission errors**: Always run as root/Administrator for sending raw frames and promiscuous sniffing.
- **High-volume captures**: Use BPF filters to reduce volume, or capture to file with `tcpdump` and analyze offline with Scapy.

---

Also check out [this official Scapy documentation](https://scapy.readthedocs.io/en/latest/index.html)


---
*End of Part 1. For part 2, check out [scapy_documentation_part2.md](./scapy_documentation_part2.md)*


---
[Back to the Section](/courseFiles/Section_04-socScripting/socScripting.md)