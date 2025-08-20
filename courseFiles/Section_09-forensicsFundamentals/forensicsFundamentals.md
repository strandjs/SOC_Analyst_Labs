## Overview
Digital forensics is the process of collecting, analyzing, and preserving digital evidence to investigate security incidents. In a SOC environment, forensic techniques are essential for understanding how an incident occurred, determining its impact, and ensuring evidence is preserved in a way that can support internal reports, compliance requirements, or even legal action

The primary objectives of forensics in the SOC are:
- Identify and scope incidents
- Preserve both volatile (RAM, network traffic) and non-volatile (disk, logs) data
- Reconstruct attacker activity and techniques
- Provide intelligence for remediation and threat hunting
- Ensure evidence is defensible in case of audits

## Order of Volatility
- Data disappears at different rates, analysts must know what to capture first
- Order (most -> least volatile)
1. CPU registers, cache
2. RAM (running processes, encryption keys, malware in memory)
3. Network traffic (active sessions, transient connections)
4. Disk (files, partitions, deleted data)
5. Logs, backups, archives

- **Practical Tip:** During live response, prioritize memory dumps and network captures before imaging disks

## FTK Imager - Evidence Acquisition
FTK Imager is an open-source software by AccessData that is used for creating accurate copies of the original evidence without actually making any changes to it

**Purpose:** Create forensic disk images, capture volatile data, preview evidence

**Key Features:**
- Disk/partition imaging (E01, raw formats)
- File system browsing without altering source
- Hashing for integrity verification
- Exporting specific files or folders from an image

**Practical Use Case:**
- Capture a suspect USB drive
- Generate MD5/SHA256 hash
- Save in E01 format for further analysis in Autopsy

If interested check out our [FTK Imager Documentation](/courseFiles/tools/FTK-Imager.md)

## Autopsy – Evidence Analysis
**Purpose:** Open-source digital forensics platform for disk and file analysis

**Key Features:**
- Timeline analysis of file activity
- Keyword search across disk images
- Recovery of deleted files
- Parsing of browser history, emails, registry entries

Practical Use Case:
- Load the FTK Imager-acquired disk
- Run a keyword search for suspicious domains or filenames
- Reconstruct a timeline of user activity around an incident

Check out our [Autopsy Documentation](/courseFiles/tools/Autopsy.md)

## Memory Forensics (Volatility Framework)
**Purpose:** Extract and analyze volatile memory from live systems or dumps

**Key Features:**
- List running processes (pslist, pstree)
- Detect hidden/injected code (malfind)
- Analyze network connections (netscan)
- Extract registry hives, DLLs, or command history

**Practical Use Case:**
- Capture RAM during live response
- Dump suspicious DLLs for malware analysis
- Find malicious processes

Make use of our [Volatility Documentation](/courseFiles/tools/Volatility.md) and hour [Volatility Hands-On Lab](/courseFiles/Section_09-forensicsFundamentals/volatilityLab1.md)

## Common Artifacts
- **Windows:** Event Logs, Registry, Prefetch, LNK files
- **Linux/Unix:** system logs, shell history, crontabs
- **Web browsers:** cookies, cache, browsing history
- **Cloud/SaaS:** audit logs, authentication events
- **Email:** headers, attachments, phishing payloads

## Workflow Example
1. **Incident occurs** – suspect machine identified
2. **Preserve volatile data** – capture RAM dump and active connections
3. **Image disk with FTK Imager** – hash and export to evidence repository
4. **Analyze with Autopsy** – check user activity, deleted files, artifacts
5. **Correlate with Volatility findings** – confirm persistence mechanisms, malware behavior
6. **Document everything** – timestamps, tools used, evidence hashes

## Legal and Ethical Considerations
- Compliance requirements (GDPR, HIPAA, PCI DSS)
- Admissibility of evidence in court (documentation standards)
- Coordination with incident responders, hunters, and external parties
- Producing clear reports for management or compliance teams

***
<b><i>Continuing the course?</b>
</br>
[Click here for the Next Section](/courseFiles/Section_10-emailFundamentals/emailFundamentals.md)</i>

<b><i>Want to go back?</b>
</br>
[Click here for the Previous Section](/courseFiles/Section_08-deceptionSystems/deceptionSystems.md)

<b><i>Looking for a different section? </b></br>[Back to Section Directory](/coursenavigation.md)</i>
