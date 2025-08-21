**Autopsy** is one of the most widely used open-source digital forensics platforms. It is built on top of The Sleuth Kit (TSK) and provides a graphical interface for investigating digital evidence. Its modular design allows analysts to process disk images, extract artifacts, and generate reports in a streamlined, repeatable fashion

In Security Operations Center (SOC) workflows, Autopsy is often leveraged for:
- Incident response investigations (e.g., analyzing compromised endpoints)
- Insider threat and data exfiltration cases
- Malware triage and persistence discovery
- Timeline reconstruction of user and system activity

## Setup 
```bash
sudo apt update
```
```bash
sudo apt install snapd
```
```bash
sudo snap install autopsy
```

## Key Features
- **Disk Image Analysis:** Supports raw images (dd), E01 (EnCase), VHD, and others
- **File Carving:** Recovers deleted files, even if directory entries are lost
- **Artifact Parsers:**
1. Web history, cookies, downloads
2. Email (PST, MBOX)
3. Registry and system configuration
- **Keyword Search:** Indexed and live searching, with regex support
- **Timeline Analysis:** Correlates file system activity into a chronological view
- **Hash Filtering:** Known good/bad hash set matching (NSRL, custom)
- **Reporting:** HTML, CSV, Excel exports for sharing findings
- **Modular Plugins:** Extendable with third-party modules for specific cases


## Typical Workflow

1. Acquire Evidence
- Imaging the suspect drive or exporting a VM disk
- Ensuring chain of custody with hashes (MD5/SHA1)

2. Create a New Case in Autopsy
- Define case name, examiner details, and evidence source

3. Ingest Evidence
- Add the acquired disk or logical files
- Choose ingestion modules (hash lookup, keyword indexing, file type detection, etc)

4. Artifact Analysis
- Review parsed results: browser history, user logins, registry keys
- Carve unallocated space for deleted data

5. Timeline Reconstruction
- Build a time-based view to understand user/system activity

6. Reporting
- Export relevant findings with documented observations


---
[Back to the section](/courseFiles/Section_09-forensicsFundamentals/forensicsFundamentals.md)
