#usage: python3 failed_logins_extractor.py YOUR_JSON_OR_CSV

import csv
import json
import os
import sys

def parse_csv(file_path):
    failed_logins = []
    with open(file_path, mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row.get("EventID") == "4625":  #Here anyone can modify the name of the row from EventID if it doesn't work. For example in a log file I saw only "Id", so in that case the code would not work
                failed_logins.append({
                    "TimeCreated": row.get("TimeCreated", "N/A"),  #Here(1)
                    "TargetUserName": row.get("TargetUserName", "N/A"), #Here(2)
                    "IpAddress": row.get("IpAddress", "N/A")  #and here(3) are the same cases as for "EventID" row names
                })
    return failed_logins

def parse_json(file_path):
    failed_logins = []
    with open(file_path, mode='r', encoding='utf-8') as jsonfile:
        logs = json.load(jsonfile)
        if isinstance(logs, dict):
            logs = logs.get("Events", [])  # if JSON wraps events in a key
        for entry in logs:
            if str(entry.get("EventID")) == "4625":    #Don't forget to also modify here(1)
                failed_logins.append({
                    "TimeCreated": entry.get("TimeCreated", "N/A"),   #Here(2)
                    "TargetUserName": entry.get("TargetUserName", "N/A"),  #Here(3)
                    "IpAddress": entry.get("IpAddress", "N/A") #Here(4)
                })
    return failed_logins


def print_results(failed_logins):
    print(f"\n[!] Found {len(failed_logins)} failed login attempts (Event ID 4625):\n")
    for entry in failed_logins:
        print(f"Time: {entry['TimeCreated']}, User: {entry['TargetUserName']}, IP: {entry['IpAddress']}")  #and also here(5)!

def main():
    if len(sys.argv) != 2:
        print("Usage: python failed_logins_parser.py <logfile.csv|logfile.json>")
        return
    file_path = sys.argv[1]
    if not os.path.exists(file_path):
        print("File not found")
        return
    ext = os.path.splitext(file_path)[1].lower()
    if ext == ".csv":
        results = parse_csv(file_path)
    elif ext == ".json":
        results = parse_json(file_path)
    else:
        print("[X] Unsupported file format. Please provide a CSV or JSON file.")
        return
    print_results(results)
    
if __name__ == "__main__":
    main()