# Lab: Covert TCP Channel

**This file does NOT include the full solution code**. Use this to write your own `sender_covert_tcp.py` and `sniffer_covert_tcp.py` (or to understand what to look for in the solution).

---

# Overview — what you'll build

You will implement two small Python scripts using **Scapy** running inside two Linux network namespaces (both inside one VM):

1. **sender\_covert\_tcp.py** — encodes an ASCII/UTF-8 message into the TCP `seq` numbers of SYN packets and sends them to the destination namespace.
2. **sniffer\_covert\_tcp.py** — sniffs incoming TCP SYN packets, recognizes the covert protocol, reassembles and prints the hidden message.

The exercise is intentionally focused on header-only covert channels (no payload), Scapy usage for send/sniff, and basic session reassembly

---

# What you must implement

Do **NOT** copy my solution directly — implement these behaviors from scratch to learn best. Below are requirements for each script so you can verify your work:

## A — Common requirements (both scripts)

- Use `scapy` (import from `scapy.all`); make sure to run the scripts as root (ex `sudo ip netns exec ...`).
- Print clear, human-readable progress/info messages while running (so you can follow what you did).
- Avoid writing to the network outside the namespaces created by the lab;  // you will run the scripts inside `ns1`/`ns2`

## B — `sender_covert_tcp.py` requirements

Implement a command-line tool that:

- Signature / CLI args (minimum):

  - positional `message` (string) — the text to send
  - `--src-port-base` (int, default `40000`) — the base source port used for encoding
  - `--dst` (str, default `10.10.10.2`) — destination IPv4 address
  - `--dport` (int, default `80`) — destination TCP port
  - `--inter` (float, default `0.05`) — inter-packet delay in seconds

- Behavior:

  1. Encode the message as UTF-8 bytes.
  2. Compute `total_len = len(bytes)`. Print `Sending message of X bytes in Y chunks to DST`.
  3. Send a single **meta** TCP SYN packet with `sport = src_port_base` and `seq = total_len`.
  4. Split the message into **4-byte** chunks (pad the final chunk with `\x00` bytes to 4 bytes if needed).
  5. For chunk index `i` (0-based) send a SYN with `sport = src_port_base + 1 + i` and `seq = int.from_bytes(chunk, 'big')`.
  6. After sending each chunk, print a short line: `chunk i: sport=XXXXX seq=0xXXXXXXXX bytes=b'....'` and sleep `--inter` seconds.
  7. Exit after sending all packets; return code 0.

- Implementation hints (sender):

  - Use `conf.verb = 0` to silence Scapy internal logs while sending.
  - To build a packet: `pkt = IP(dst=dst)/TCP(sport=..., dport=dport, flags='S', seq=value_int)` and `send(pkt)`.
  - Use `int.from_bytes(..., 'big')` for conversion and `int.to_bytes(..., 4, 'big')` when needed for printing.
  - Choose sensible validation on `src_port_base` (ex: must be an integer > 1024).

## C — `sniffer_covert_tcp.py` requirements

Implement a sniffing/decoder script that:

- CLI args (minimum): none required — you can add optional `--verbose`.

- Behavior:

  1. Use a BPF filter when calling `sniff(...)` so Scapy receives only SYN packets: ex: `filter='tcp and tcp[13] & 2 != 0'`.
  2. For each incoming SYN, read `src_ip`, `sport`, and `seq`.
  3. Ignore well-known ports (ex: `sport < 1024`) unless you choose to decorate the protocol differently.
  4. Recognize a **new session** when you see a SYN with `sport == src_port_base` (a new base) and a plausible `seq` that you treat as `total_len` (you can accept an upper bound such as 1 MiB to avoid false positives). When you detect a new session, store its state: `src_ip`, `base_port`, `total_len`, and an empty chunk map.
  5. For later SYNs from the same `src_ip` compute `index = sport - base_port - 1`. If `index >= 0` accept the packet as a chunk: store `chunks[index] = seq & 0xFFFFFFFF`.
  6. When you have `expected_chunks = ceil(total_len/4)` chunks, reassemble the message by concatenating the 4-byte big-endian values in index order and slicing to `total_len` bytes. Decode as UTF-8 with `errors='replace'` and print: `[DETECTED] From SRC_IP: Reassembled message: <text>`.
  7. Clean up per-session state once complete.

- Implementation hints (sniffer):

  - Use a `Session` class or a dictionary keyed by `(src_ip, base_port)` to store state.
  - Use `sniff(filter=..., prn=pkt_callback, store=False)` to handle packets in realtime.
  - When matching chunks, be mindful of missing chunks (e.g., implement `fallback` behavior or timeouts if you like as an extension).
  - For robustness, clamp seq values with `seq & 0xFFFFFFFF` before converting.

---

# Step-by-step setup tasks (what to do now)

Below is a precise, *step‑by‑step* run plan you can follow **after** you implement the two scripts. It includes the environment setup, how to run each script in separate terminals, how to test and verify, and how to clean up.

### Step A — Quick environment setup (run this first, on the host VM)

Run each command as your normal user (use `sudo` where neeeded). It creates two isolated network namespaces and a veth pair so all traffic stays inside the VM.

- create a directory for the lab and enter it
```bash
mkdir -p ~/scapy_covert_lab && cd ~/scapy_covert_lab
```
- create namespaces
```bash
sudo ip netns add ns1
sudo ip netns add ns2
```
- create veth pair
```bash
sudo ip link add veth-ns1 type veth peer name veth-ns2
```
- move veth ends into namespaces
```bash
sudo ip link set veth-ns1 netns ns1
sudo ip link set veth-ns2 netns ns2
```
- configure addresses and bring interfaces up
```bash
sudo ip netns exec ns1 ip addr add 10.10.10.1/24 dev veth-ns1
sudo ip netns exec ns1 ip link set lo up
sudo ip netns exec ns1 ip link set veth-ns1 up
```
```bash
sudo ip netns exec ns2 ip addr add 10.10.10.2/24 dev veth-ns2
sudo ip netns exec ns2 ip link set lo up
sudo ip netns exec ns2 ip link set veth-ns2 up
```
- quick verification of interfaces
```
echo 'ns1 interfaces:'
sudo ip netns exec ns1 ip a
```
```bash
echo 'ns2 interfaces:'
sudo ip netns exec ns2 ip a
```

If these commands succeed you are ready to copy your scripts into `~/scapy_covert_lab/scripts/`.

### Step B — Create script files (place your implementations)

Assuming you implemented the two scripts according to the spec, put them here:

```bash
mkdir -p ~/scapy_covert_lab/scripts
# copy or create your files
nano ~/scapy_covert_lab/scripts/sniffer_covert_tcp.py
nano ~/scapy_covert_lab/scripts/sender_covert_tcp.py
```
- make scripts executable
```bash
chmod +x ~/scapy_covert_lab/scripts/*.py
```

### Step C — Run the sniffer (Terminal A)

Open a new terminal window/tab (Terminal A) and start the sniffer inside `ns2`. Run it as root so Scapy can sniff raw packets.

> Terminal A
```bash
sudo ip netns exec ns2 python3 ~/scapy_covert_lab/scripts/sniffer_covert_tcp.py
```

What to expect in Terminal A:

- A startup message like `Starting sniffer — listening for covert SYN packets.`
- When traffic arrives you will see lines such as `New session from 10.10.10.1 base_port=40000 total_len=18` and `Got chunk idx=...`.
- Leave this terminal running while you send packets from Terminal B.

![](./attachments/terminal_A.png)

### Step D — Run the sender (Terminal B)

Open another terminal (Terminal B) and run the sender inside `ns1`. Provide a test message and (optionally) the `--src-port-base` and `--dst` values.
> Terminal B
```bash
sudo ip netns exec ns1 python3 ~/scapy_covert_lab/scripts/sender_covert_tcp.py "Hello-Scapy-Covert" --src-port-base 40000 --dst 10.10.10.2
```

What to expect in Terminal B:

- A short summary `Sending message of X bytes in Y chunks to DST`.
- Per-chunk prints like `chunk 0: sport=40001 seq=0x48656c6c bytes=b'Hell'`.
- Script exits after sending all SYNs.

![](./attachments/terminal_B.png)


### Step E — Observe & verify (Terminal A + optional Terminal C)

- In Terminal A (sniffer) you should see chunk receipt logs and a final line like:

```
[DETECTED] From 10.10.10.1: Reassembled message: Hello-Scapy-Covert
```

- Optional: if you want to inspect raw packets, open a third terminal (Terminal C) and run `tcpdump` inside `ns2` while you send the message:

> Terminal C (optional)
```bash
sudo ip netns exec ns2 tcpdump -i veth-ns2 -nn -X 'tcp and tcp[13] & 2 != 0'
```

Look for the SYN packets and confirm the `seq` values match the sender's printed hex values.


![](./attachments/terminal_C.png)


### Step F — Troubleshooting quick checks

If the sniffer does not reassemble the message:

- Confirm you ran the sniffer inside `ns2` and the sender inside `ns1` (namespaces matter).
- Check both scripts are executable and were updated (no placeholder content left).
- Increase sender `--inter` (e.g., to `0.1`) to reduce local packet loss/reordering.
- Use `tcpdump` (Terminal C) to verify SYNs actually arrived in `ns2`.
- If the sniffer prints a fallback session message, it might have seen chunks but missed the meta packet—ensure `src_port_base` used by sender matches what sniffer expects (default 40000).

### Step G — Cleanup (when done)

Stop the sniffer (Ctrl+C) and remove the namespaces:

```bash
sudo ip netns del ns1
sudo ip netns del ns2
```

---

# Checkpoints — how you will know it's correct (tests you should pass)

1. When you run the sender you must see a short summary such as: `Sending message of 18 bytes in 5 chunks to 10.10.10.2` and lines for each chunk showing `sport` and `seq` in hex.
2. The sniffer must log a new session `New session from 10.10.10.1 base_port=40000 total_len=18` (or similar) and the chunk receipt lines.
3. The sniffer prints the final reassembled message exactly matching (or human-readable equivalent of) the original string.
4. Optional verification: `tcpdump` on the receiving namespace shows SYN packets with sequence numbers matching what the sender printed.

>[!TIP]
>
>If one of the checks fails, consult the troubleshooting hints below.

---

# Hints & common pitfalls 

- **SYN flag detection**: TCP flags are bitfields — checking `pkt[TCP].flags & 0x02` is the correct way to test SYN.

- **Byte order**: Use `int.from_bytes(chunk, 'big')` to convert 4 bytes into an integer for the `seq` field. When converting back, use `int.to_bytes(value, 4, 'big')`.


- **Padding**: Pad the final chunk with `\x00` bytes to 4 bytes before conversion; remember to slice the reassembled bytes to `total_len`.


- **seq limits**: TCP seq is a 32-bit field — mask or clamp values with & 0xFFFFFFFF when reading or storing to avoid sign/overflow surprises.

- **Running as root**: Both sending raw packets and sniffing require elevated privileges — run the scripts with sudo (or inside ip netns exec ... as root).

-**Network namespaces**: Run the sender in ns1 and the sniffer in ns2 (use ip netns exec ns1 ... / ns2 ...). Mixing them up could be the most common mistake.

- **Inter-packet timing**: If packets are lost or arrive out of order, increase the sender --inter delay (try 0.1 or 0.2 seconds) to improve reliability in the VM.

- **BPF filter:** Use a BPF filter (ex: tcp and tcp[13] & 2 != 0) in sniff() to reduce CPU and avoid processing unrelated traffic.

- **Fallback**: Expect some packet loss in any real test; consider adding a fallback in the sniffer (create a session if chunks appear before the meta packet) or a simple timeout-based cleanup to avoid stale state.

---

*For the lab solution, check out [scapy_lab_solution.md](./scapy_lab_solution.md)*


---
[Back to the Section](/courseFiles/Section_04-socScripting/socScripting.md)
