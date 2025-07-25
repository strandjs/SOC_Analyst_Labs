# Lab 2: PowerShell - Collect Basic System Info and Save to File

## Goal

In this lab, you'll write a PowerShell script to collect essential system information and save it to a `.txt` file. This is especially useful for asset inventory, triage during incident response, and general host profiling.

---

## Why It’s Relevant

- Teaches **PowerShell basics** for scripting and automation.
- Demonstrates **system information gathering** and basic **log collection**.
- Provides foundational skills for **incident response** and **asset fingerprinting**.

---

## Task

Write a PowerShell script that gathers the following information from the system and saves it to a file named `system_info.txt`:

### Information to Collect

- Hostname
- Current username
- IP address(es)
- Operating system version
- List of running processes
- Active network connections

---

## Sample Output (system_info.txt)

```
Hostname: DESKTOP-12345
Username: DOMAIN\user
IP Address: 192.168.1.100
OS Version: Microsoft Windows 10 Pro

Running Processes:
------------------
explorer
powershell
chrome

Active Network Connections:
---------------------------
TCP 192.168.1.100:50328 93.184.216.34:443 ESTABLISHED
TCP 192.168.1.100:50329 172.217.9.174:443 ESTABLISHED
```

---

## Hints

- Use `Get-ComputerInfo` or `Get-WmiObject` for OS and host details.
- Use `Get-Process` to list processes.
- Use `Get-NetTCPConnection` or `netstat` for active connections.
- Use `Out-File` or `Set-Content` to write to a file.

---

## Solution

Once you are finished, you can check out the [solution](./lab2_solution_steb_by_step.md). The solution contains step by step guidence!