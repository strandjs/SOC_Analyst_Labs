## Overview
FTK Imager is a free forensic tool from AccessData used to preview and capture data in a forensically sound manner. In SOC and IR work, it’s mainly used to acquire disk images, capture volatile memory, and quickly review files without altering the source system

## Core Features
- **Disk Imaging** – Create exact, bit-level copies of entire drives, partitions, or removable media
- **File System Preview** – Browse directories and files before imaging
- **Memory Acquisition** – Capture live RAM, including pagefile.sys if needed
- **Hashing** – Generate MD5, SHA1, or SHA256 values to confirm evidence integrity
- **Export Options** – Save in multiple formats: E01, RAW/DD, AFF, SMART
- **Evidence Mounting** – Mount acquired images in read-only mode for safe examination

## Installing FTK Imager
Get the Setup from [Here](https://www.exterro.com/ftk-product-downloads/ftk-imager-4-7-3-81)



## Common Use Cases in a SOC
- Creating forensic images from compromised machines
- Capturing volatile memory during incident response
- Extracting email containers (PST/OST) for investigation
- Quick triage: checking file systems, logs, or suspicious files
- Preserving evidence in a defensible format for later deep analysis

## Basic Workflows
### Creating a Disk Image
1. Open FTK Imager -> File -> Create Disk Image
2. Choose the source: physical drive, logical drive, or existing image
3. Select output format (E01 is most common)
4. Enter case details: Case Number, Examiner, Notes
5. Choose the destination folder and file size splitting if required
6. Start acquisition
7. Verify image hashes to confirm integrity

### Capturing Memory
1. Go to File -> Capture Memory
2. Pick a destination for the dump file
3. Optionally include pagefile.sys and crash dump
4. Start capture

### Mounting Evidence
1. Open File -> Image Mounting
2. Select the image file
3. Mount as read-only
4. Browse like a normal drive in Windows Explorer

## Handling Evidence Correctly
- Use write blockers whenever imaging drives
- Always hash both source and acquired images
- Keep a detailed chain-of-custody log
- Store output on secure, access-controlled media



---
[Back to the section](/courseFiles/Section_09-forensicsFundamentals/forensicsFundamentals.md)

