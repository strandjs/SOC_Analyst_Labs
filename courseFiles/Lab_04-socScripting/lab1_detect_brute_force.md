# Lab 1: Python - Detect Brute Force Attempts from a JSON Log File

## Goal

In this lab, you'll write a Python script to analyze a JSON log file containing authentication events. Your goal is to detect potential brute-force attacks by identifying IP addresses with multiple failed login attempts.


## Sample Log Format

The log file is a JSON where each entry represents an authentication event:

```json
[
  {
    "timestamp": "2025-07-16T12:32:10Z",
    "username": "admin",
    "ip": "192.168.1.5",
    "status": "fail"
  },
  {
    "timestamp": "2025-07-16T12:33:02Z",
    "username": "admin",
    "ip": "192.168.1.5",
    "status": "fail"
  },
  {
    "timestamp": "2025-07-16T12:34:00Z",
    "username": "admin",
    "ip": "192.168.1.5",
    "status": "success"
  }
]
```

## Task

Write a Python script that:

1. Reads the JSON log file.
2. Counts failed login attempts per IP address.
3. Prints IP addresses that had **3 or more failed login attempts**.

## Bonus (Optional)

- **Add time-based filtering** (ex: 3 failed attempts within a 10-minute window)
- **Output suspicious IPs** along with the number of failed attempts
- **Allow configurable threshold** via command-line arguments'

### Example Output

```
Suspicious IPs detected:
192.168.1.5 - 4 failed attempts
203.0.113.77 - 3 failed attempts
```

## Hints

- Use Python's `json` module to parse the file.
- Use a dictionary to count failed attempts per IP.
- You can read timestamps as strings for simplicity or use `datetime` to do time comparisons.

---

## Solution

Once you are finished, you can check out the [solution](./lab1_solution_step_by_step.md). The solution contains step by step guidence!