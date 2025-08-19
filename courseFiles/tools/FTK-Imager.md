<img width="496" height="381" alt="image" src="https://github.com/user-attachments/assets/19125f6f-7feb-4174-ad6a-169bcd569e1d" />## Overview
FTK Imager is a free forensic tool from AccessData used to preview and capture data in a forensically sound manner. In SOC and IR work, it’s mainly used to acquire disk images, capture volatile memory, and quickly review files without altering the source system

<img width="1422" height="816" alt="image" src="https://github.com/user-attachments/assets/80663ca8-be4e-403a-80b9-e44e4632d6ef" />


## Core Features
- **Disk Imaging** – Create exact, bit-level copies of entire drives, partitions, or removable media
- **File System Preview** – Browse directories and files before imaging
- **Memory Acquisition** – Capture live RAM, including pagefile.sys if needed
- **Hashing** – Generate MD5, SHA1, or SHA256 values to confirm evidence integrity
- **Export Options** – Save in multiple formats: E01, RAW/DD, AFF, SMART
- **Evidence Mounting** – Mount acquired images in read-only mode for safe examination

## Installing FTK Imager
Get the Setup from [Here](https://www.exterro.com/ftk-product-downloads/ftk-imager-4-7-3-81) adn **run** it

Click **Next**

<img width="496" height="381" alt="image" src="https://github.com/user-attachments/assets/1f62bcb2-2de8-4a87-8469-07a6a2b235ab" />

Accept the terms and click **Next**

<img width="496" height="381" alt="image" src="https://github.com/user-attachments/assets/b5cd08c2-16b9-4134-a1e2-0f89650f94da" />

Install it wherever and include make sure the box is ticked and click **Next**

<img width="496" height="381" alt="image" src="https://github.com/user-attachments/assets/1bae97e1-cdc7-4fdf-9519-b1ef174b9bcd" />

Click **Install**

<img width="496" height="381" alt="image" src="https://github.com/user-attachments/assets/237f1195-74b1-48a4-b46a-6b3756c0ec94" />

Tick the box and click **Finish**

<img width="496" height="381" alt="image" src="https://github.com/user-attachments/assets/641c66a7-5544-44d8-8641-68ce05d72fef" />




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

