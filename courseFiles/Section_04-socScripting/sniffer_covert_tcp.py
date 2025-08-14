#!/usr/bin/env python3
"""
sniffer_covert_tcp.py — sniff SYN packets and reconstruct the covert message.

Run inside ns2 as root:
  sudo ip netns exec ns2 python3 sniffer_covert_tcp.py

Protocol (recap):
- The first SYN from a sender uses src port == src_port_base and seq == total_length (message length in bytes).
- Subsequent SYNs use src port == src_port_base + 1 + chunk_index and seq == 4-byte chunk encoded as big-endian integer.

This sniffer uses a simple heuristic to detect and reassemble sessions.
"""

import time
from scapy.all import sniff, TCP, IP

sessions = {}


class Session:
    """Holds state for one covert-send session from a single source IP and base port."""
    def __init__(self, src_ip, base_port):
        self.src_ip = src_ip
        self.base_port = base_port
        self.total_len = None    
        self.chunks = {}         
        self.start_time = time.time()

    def add_length(self, total_len):
        self.total_len = int(total_len)

    def add_chunk(self, index, value_int):
        self.chunks[int(index)] = int(value_int) & 0xFFFFFFFF

    def expected_chunks(self):
        if self.total_len is None:
            return None
        return (self.total_len + 3) // 4

    def is_complete(self):
        exp = self.expected_chunks()
        if exp is None:
            return False
        return len(self.chunks) >= exp

    def reassemble(self):
        """Return the reconstructed bytes of the message."""
        exp = self.expected_chunks()
        if exp is None:
            return b''
        out = bytearray()
        for i in range(exp):
            v = self.chunks.get(i, 0)
            out += v.to_bytes(4, 'big')
        return bytes(out[:self.total_len])


def pkt_callback(pkt):
    """Callback invoked by scapy.sniff for each received packet that matches the BPF filter."""
    if not pkt.haslayer(IP) or not pkt.haslayer(TCP):
        return
    ip = pkt[IP]
    tcp = pkt[TCP]

    if not (tcp.flags & 0x02):
        return

    src = ip.src
    sport = tcp.sport
    seq = tcp.seq
    if sport < 1024:
        return
    if seq > 0 and seq <= 1024*1024 and (src, sport) not in sessions:
        sess = Session(src, sport)
        sess.add_length(seq)
        sessions[(src, sport)] = sess
        print(f"[INFO] New session from {src} base_port={sport} total_len={seq}")
        return
    matched = False
    for (s_src, s_base), sess in list(sessions.items()):
        if s_src != src:
            continue
        idx = sport - s_base - 1
        if idx < 0:
            continue
        sess.add_chunk(idx, seq)
        matched = True
        print(f"[INFO] Got chunk idx={idx} from {src} base={s_base} seq=0x{seq:08x}")
        if sess.is_complete():
            msg_bytes = sess.reassemble()
            try:
                msg_str = msg_bytes.decode('utf-8', errors='replace')
            except Exception:
                msg_str = str(msg_bytes)
            print(f"[DETECTED] From {src}: Reassembled message: {msg_str}")
            del sessions[(s_src, s_base)]
        break

    if not matched:
        if seq > 0 and seq <= 1024*1024 and (src, sport) not in sessions:
            sess = Session(src, sport)
            sess.add_length(seq)
            sessions[(src, sport)] = sess
            print(f"[INFO] Fallback new session from {src} base_port={sport} total_len={seq}")


if __name__ == '__main__':
    print("Starting sniffer — listening for covert SYN packets. Press Ctrl+C to stop.")
    sniff(filter='tcp and tcp[13] & 2 != 0', prn=pkt_callback, store=False)