import requests
import time

API_KEY = 'YOUR_ABUSEIPDB_API_KEY'  #replace with an actual API key
API_URL = 'https://api.abuseipdb.com/api/v2/check'

HEADERS = {
    'Accept': 'application/json',
    'Key': API_KEY
}

ip_list = [
    '8.8.8.8',
    '1.1.1.1',
    '185.199.108.153',
] #change with the actual IP-s you want to check

def enrich_ip(ip_address):
    params = {
        'ipAddress': ip_address,
        'maxAgeInDays': '90'
    }

    response = requests.get(API_URL, headers=HEADERS, params=params)

    if response.status_code == 200:
        data = response.json()['data']
        print(f"\n[+] IP: {data['ipAddress']}")
        print(f"    Abuse Score: {data['abuseConfidenceScore']}")
        print(f"    Country: {data.get('countryCode', 'N/A')}")
        print(f"    ISP: {data.get('isp', 'N/A')}")
        print(f"    Domain: {data.get('domain', 'N/A')}")
        print(f"    Total Reports: {data.get('totalReports', 0)}")
        print(f"    Last Reported At: {data.get('lastReportedAt', 'N/A')}")
    else:
        print(f"[-] Failed to fetch data for IP {ip_address}: {response.status_code} - {response.text}")

def main():
    for ip in ip_list:
        enrich_ip(ip)
        time.sleep(1)  # this is for the API rate limits

if __name__ == '__main__':
    main()
