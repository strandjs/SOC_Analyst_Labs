# For the Ubuntu VM

[Part1](/courseFiles/Section_09-forensicsFundamentals/volatilityLab1.md)   [Part2](/courseFiles/Section_09-forensicsFundamentals/volatilityLab2.md)   [Part3](/courseFiles/Section_09-forensicsFundamentals/volatilityLab3.md)   [Part4](/courseFiles/Section_09-forensicsFundamentals/volatilityLab4.md)

This lab should be done as a continuation of the [Volatility Documentation](/courseFiles/tools/Volatility.md)

This is the 2nd of 4 parts

# Setup

```bash
IMG=~/labs/volatility3/stage2.lime
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

Stage 2 is about a binary ``kswapd0`` launched with a malicious ``LD_PRELOAD`` hook connects out on port **4444**

Using ``linux.pslist.PsList`` is useless since the name of the malware sounds System-ish, but using ``linux.sockstat.Sockstat`` reveals us all outbound connections, one in particular stands out, a `nc` one, a netcat listener

<img width="1620" height="65" alt="image" src="https://github.com/user-attachments/assets/65a38720-6fe7-4a99-bbd9-e0e014a45ff9" />

The **PID** is ``1050``

A SOC Analyst should be curious and run ``linux.envars.Envars --pid 1050`` to see more about it and confirm it is malware

<img width="549" height="266" alt="image" src="https://github.com/user-attachments/assets/1b4df2ae-693e-497a-aa17-548a3e6646d7" />

This confirms it is a reverse shell!
