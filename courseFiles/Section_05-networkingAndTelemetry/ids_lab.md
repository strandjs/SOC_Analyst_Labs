# IDS Lab — Using Suricata
 
## Lab Goals
 
Learn how to:
- Use **Suricata** 
- Create and test **custom detection rules**
- Simulate **attacks** (ping, Nmap, Nikto, curl, etc.)
- Monitor and analyze **alerts**
 
 
---
 
## 1. Install IDS Tools on Kali

`sudo su -`

`wget https://archive.kali.org/archive-keyring.gpg -O /usr/share/keyrings/kali-archive-keyring.gpg`

`apt-get update`

---
 
### Install Suricata
 
`apt-get install suricata`

If you get any popups just tab to select OK and keep the default values.

Verify:
 
```bash
suricata --build-info
```

<img width="645" height="104" alt="image" src="https://github.com/user-attachments/assets/87693277-2be8-4198-b10f-0766c241878f" />




 
## 4. Running Suricata
 
### A. Add Custom Rules
 
```bash
sudo nano /var/lib/suricata/rules/suricata.rules
```
 
Paste:
 
```suricata
alert icmp any any -> any any (msg:"[Suricata] ICMP Ping Detected"; itype:8; sid:2000001;)
```

Then hit Ctrl+O to save the file and Ctrl+X to exit Nano.
 
---
 
### B. Run Suricata
 
```bash
sudo suricata -c /etc/suricata/suricata.yaml -i lo
```

<img width="644" height="112" alt="image" src="https://github.com/user-attachments/assets/26c0b848-78b3-4470-bc2b-8badef146814" />


Then(in another terminal):
 
```bash
ping 127.0.0.1
```

<img width="459" height="113" alt="image" src="https://github.com/user-attachments/assets/601b9292-3a5a-40f8-a025-690a2cc2a731" />


 
Check alerts(in a 3rd terminal):
 
```bash
sudo tail -f /var/log/suricata/fast.log
```

<img width="661" height="247" alt="image" src="https://github.com/user-attachments/assets/a2d19793-4cd4-460e-9151-5e5e3e91a46d" />

 
---

Update full Suricata ruleset

`sudo suricata-update`

<img width="660" height="322" alt="image" src="https://github.com/user-attachments/assets/fad4799a-46c6-45b9-bf4b-bca8a599f059" />



 
## 5.Skills You're Practicing
 
| Skill              | Purpose                                           |
|-------------------|---------------------------------------------------|
| IDS Configuration | Setup and tuning for detection effectiveness      |
| Rule Writing       | Customize detection, reduce false positives       |
| Alert Triage       | Investigate logs quickly and efficiently          |
| Attack Simulation  | Understand adversary behavior                     |
| Incident Reporting | Communicate findings clearly in report format     |
 
---
 
##  6. Mini-Incident Report Example
 
| Field           | Example                       |
|----------------|-------------------------------|
| **Time**        | 2025-07-24 14:32              |
| **Tool**        | Suricata                      |
| **Alert**       | ICMP Ping Detected            |
| **Source IP**   | 127.0.0.1                     |
| **Dest IP**     | 127.0.0.1                     |
| **Rule SID**    | 2000001                       |
 
 
---
 
## 7. Useful resource
 
- [snorpy](https://snorpy.cyb3rs3c.net) -A Web Based Snort Rule Creator


---
[Back to the section](/courseFiles/Section_05-networkingAndTelemetry/networkingAndTelemetry.md)
