#!/usr/bin/env python3
"""
sender_covert_tcp.py — send an ASCII message encoded as TCP SYN seq numbers.

Usage example (run inside ns1):
  sudo ip netns exec ns1 python3 sender_covert_tcp.py "Hello-Scapy-Covert" --src-port-base 40000 --dst 10.10.10.2

Behavior:
- Sends one meta SYN packet with src port == src_port_base and seq == total_len.
- Sends N payload SYNs with src ports src_port_base+1 ... src_port_base+N and seq == big-endian integer of 4-byte chunk;;
"""

import argparse
from math import ceil
from time import sleep
from scapy.all import IP, TCP, send, conf


conf.verb = 0 

parser = argparse.ArgumentParser(description='Covert TCP sender (encode message in SYN seq)')
parser.add_argument('message', help='ASCII/UTF-8 message to send')
parser.add_argument('--src-port-base', type=int, default=40000, help='base source port (initial meta packet)')
parser.add_argument('--dst', default='10.10.10.2', help='destination IP address')
parser.add_argument('--dport', type=int, default=80, help='destination TCP port')
parser.add_argument('--inter', type=float, default=0.05, help='inter-packet sleep (seconds)')
args = parser.parse_args()

msg_bytes = args.message.encode('utf-8')
total_len = len(msg_bytes)
num_chunks = ceil(total_len / 4)

print(f"Sending message of {total_len} bytes in {num_chunks} chunks to {args.dst}")

meta = IP(dst=args.dst)/TCP(sport=args.src_port_base, dport=args.dport, flags='S', seq=total_len)
send(meta)
for i in range(num_chunks):
    start = i * 4
    chunk = msg_bytes[start:start+4]
    if len(chunk) < 4:
        chunk = chunk + b'\x00' * (4 - len(chunk))
    value_int = int.from_bytes(chunk, 'big')
    sport = args.src_port_base + 1 + i
    pkt = IP(dst=args.dst)/TCP(sport=sport, dport=args.dport, flags='S', seq=value_int)
    print(f"  chunk {i}: sport={sport} seq=0x{value_int:08x} bytes={chunk}")
    send(pkt)
    if args.inter:
        sleep(args.inter)

print('Done :)')