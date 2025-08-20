# For the Ubuntu VM

[Part1](/courseFiles/Section_09-forensicsFundamentals/volatilityLab1.md)   [Part2](/courseFiles/Section_09-forensicsFundamentals/volatilityLab2.md)   [Part3](/courseFiles/Section_09-forensicsFundamentals/volatilityLab3.md)   [Part4](/courseFiles/Section_09-forensicsFundamentals/volatilityLab4.md)

This lab should be done as a continuation of the [Volatility Documentation](/courseFiles/tools/Volatility.md)

This is the 4th of 4 parts

# Setup

```bash
IMG=~/labs/volatility3/stage4.lime
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

Stage 4 is a fake **kworker** ``/tmp/kworker_packet`` opens a raw AF_PACKET socket, filtering traffic for port **5555**

The catch is it does not register with the kernel TCP stack, so there is no entry in ``/proc/net/tcp``

Now using ``linux.sockstat.Sockstat`` is also useless since the malware was edited out of the kernel TCP stack and there will be nothing on port **5555**, so ``linux.sockstat.Sockstat | grep 5555
`` with print out **nothing**

The only way to really find it is by doing ``linux.psaux.PsAux``, there you will see ``kworker_packet`` which if it was System it would be under [], from that we get that the attacker used **sudo** from the interactive bash **(PID 1040)** to run a launcher called ``kworker_packet``

<img width="444" height="143" alt="image" src="https://github.com/user-attachments/assets/7dd3874c-1b75-4f7b-a1cb-a6c2fdd50f84" />


So let's pivot off **1071** and **1040** to find what ``kworker_packet`` spawned/renamed

Our supposition is confirmed by ``linux.pstree.PsTree``

<img width="495" height="45" alt="image" src="https://github.com/user-attachments/assets/264cc9e1-ea4c-43e7-87c4-a9a068597cf1" />

After doing ``linux.envars.Envars --pid 1071`` we can say many things about the attack

<img width="540" height="244" alt="image" src="https://github.com/user-attachments/assets/e242da14-19f1-40bb-ba23-732e99e2d442" />

HISTFILE=/dev/null -> attacker explicitly disabled bash history logging

PWD=/tmp -> the launch happened in /tmp

Then normally we would use ``linux.lsof.Lsof --pid 1071``, but it doesn't help us that much here

<img width="1752" height="224" alt="image" src="https://github.com/user-attachments/assets/58b0be3a-6d01-45d5-846c-f3a1a40f122f" />

lsof shows only normal TTY pipes + /etc/sudoers — no open sockets, no executable ELF left in fd

So ``1071`` itself is just the ``sudo`` wrapper, it spawned something else (the malware) that then daemonized and detached

The real payload must be in another PID, let's check processes right after **15:33:50** so we will do ``linux.pslist.PsList``

<img width="1195" height="45" alt="image" src="https://github.com/user-attachments/assets/ded6cab2-a74d-4496-8e65-e662c9fd3136" />

We see that ``kworker/5:2`` was spawned not even a second later than the launcher, that is our malware, and that is more than enough proof the system was infected







