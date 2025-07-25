# Lab 1 Solution: Detect Brute Force Attempts from a JSON Log File

This page walks you through the step-by-step solution to detect brute-force login attempts from a JSON log file using Python.

---

##  Step-by-Step Guide

### Step 1: Import Required Modules

```python
import json
import argparse
from collections import defaultdict
from datetime import datetime, timedelta
```

---

### Step 2: Parse Command-Line Arguments

Allow users to specify the log file, threshold, and time window.

```python
parser = argparse.ArgumentParser(description="Detect brute-force login attempts.")
parser.add_argument("logfile", help="Path to the JSON log file.")
parser.add_argument("--threshold", type=int, default=3, help="Number of failed attempts to consider as suspicious.")
parser.add_argument("--window", type=int, default=10, help="Time window in minutes.")
args = parser.parse_args()
```

---

### Step 3: Load the JSON Log File

```python
with open(args.logfile, "r") as f:
    logs = json.load(f)
```

---

### Step 4: Organize Failed Attempts by IP

Convert timestamps and group all failed attempts by IP.

```python
failed_logins = defaultdict(list)

for entry in logs:
    if entry.get("status") == "fail":
        ip = entry.get("ip")
        timestamp = datetime.fromisoformat(entry["timestamp"].replace("Z", "+00:00"))
        failed_logins[ip].append(timestamp)
```

---

### Step 5: Detect Suspicious IPs

Check for N or more failed attempts within the specified time window.

```python
suspicious_ips = {}

for ip, times in failed_logins.items():
    times.sort()
    for i in range(len(times)):
        window_start = times[i]
        window_end = window_start + timedelta(minutes=args.window)
        count = sum(1 for t in times[i:] if t <= window_end)
        if count >= args.threshold:
            suspicious_ips[ip] = count
            break
```

---

### Step 6: Display the Results

```python
if suspicious_ips:
    print("Suspicious IPs detected:")
    for ip, count in suspicious_ips.items():
        print(f"{ip} - {count} failed attempts")
else:
    print("No suspicious activity detected.")
```

---

## Example Run

```bash
python detect_brute_force.py auth_log.json --threshold 3 --window 10
```

---

## Full python script

```python
import json
import argparse
from collections import defaultdict
from datetime import datetime, timedelta

parser = argparse.ArgumentParser(description="Detect brute-force login attempts.")
parser.add_argument("logfile", help="Path to the JSON log file.")
parser.add_argument("--threshold", type=int, default=3, help="Number of failed attempts to consider as suspicious.")
parser.add_argument("--window", type=int, default=10, help="Time window in minutes.")
args = parser.parse_args()

with open(args.logfile, "r") as f:
    logs = json.load(f)

failed_logins = defaultdict(list)
for entry in logs:
    if entry.get("status") == "fail":
        ip = entry.get("ip")
        timestamp = datetime.fromisoformat(entry["timestamp"].replace("Z", "+00:00"))
        failed_logins[ip].append(timestamp)

suspicious_ips = {}
for ip, times in failed_logins.items():
    times.sort()
    for i in range(len(times)):
        window_start = times[i]
        window_end = window_start + timedelta(minutes=args.window)
        count = sum(1 for t in times[i:] if t <= window_end)
        
        if count >= args.threshold:
            suspicious_ips[ip] = count
            break

if suspicious_ips:
    print("Suspicious IPs detected:")
    for ip, count in suspicious_ips.items():
        print(f"{ip} - {count} failed attempts")
else:
    print("No suspicious activity detected.")
```

---

## Example output:
![lab1 test script](https://i.ibb.co/ym8PXnSZ/image.png)