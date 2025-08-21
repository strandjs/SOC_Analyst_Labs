# For the Ubuntu VM

[Part1](/courseFiles/Section_09-forensicsFundamentals/volatilityLab1.md)   [Part2](/courseFiles/Section_09-forensicsFundamentals/volatilityLab2.md)   [Part3](/courseFiles/Section_09-forensicsFundamentals/volatilityLab3.md)   [Part4](/courseFiles/Section_09-forensicsFundamentals/volatilityLab4.md)

This lab should be done as a continuation of the [Volatility Documentation](/courseFiles/tools/Volatility.md)

This is the 3rd of 4 parts

# Setup

```bash
IMG=~/labs/volatility3/stage3.lime
```
```bash
SYMS='--remote-isf-url https://github.com/Abyss-W4tcher/volatility3-symbols/raw/master/banners/banners.json'
```

The commands will be in this template:
```bash
python3 vol.py -f "$IMG" $SYMS linux.something
```

## Your turn
Try to find the malware using the commands in the [Volatility Documentation](/courseFiles/tools/Volatility.md) and then scroll down to see what you should've looked for

<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>

Stage 3 is about a backdoor process pretending to be ``kworker`` listens on **TCP** **5555**

Again using ``linux.pslist.PsList`` is pointless since the name isn't suspicious so you have to use ``linux.sockstat.Sockstat`` again, at which point you see like in Stage 2 a suspicious ``nc`` listener with **PID** 1209

<img width="1637" height="64" alt="image" src="https://github.com/user-attachments/assets/3d0cc817-f1e5-4f34-9a52-322ce7e98f9a" />

Using ``linux.lsof.Lsof | grep 1209`` show the open File Descriptors for that PID

Here, **STDIN**/**STDOUT**/**STDERR** are all redirected to ``/dev/null`` -> stealth technique (no terminal output)

FD 3 is a socket, consistent with the sockstat network listener

**This is a confirmation:** the process isn’t just listening, it’s intentionally hiding activity by throwing output away

Using ``linux.proc.Maps --pid 1209`` doesn't output anything strange, seems like a traditional nc binary, but the anomaly is in how it was launched, not what it loads

Finally using ``linux.envars.Envars --pid 1209`` reveals exactly how the process was started 

<img width="689" height="346" alt="image" src="https://github.com/user-attachments/assets/1cd66147-cc8a-4bc6-b41d-bc08049e8b63" />

<pre>SUDO_COMMAND=/usr/bin/unshare -m /bin/bash -c 
    mount -t proc proc /proc
    nc -l -p 5555 >/dev/null 2>&1 &
    /tmp/kworker &
    sleep 999999</pre>

You see the attacker used ``unshare`` (to isolate namespaces), mounted ``/proc``, then ran **nc** to listen silently on 5555, plus launched ``/tmp/kworker``

The presence of /tmp/kworker ties into the persistence/stealth part of Stage 3
