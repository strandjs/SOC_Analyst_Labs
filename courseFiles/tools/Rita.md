**RITA** stands for **Real Intelligence Threat Analytics**—an open-source framework that helps SOC analysts detect stealthy Command-and-Control (C2) behavior through network traffic patterns, it works by analyzing Zeek logs (TSV or JSON) or PCAPs converted into Zeek format, focusing on anomalies rather than signature-based detection

Rather than relying solely on known IoCs, RITA equips analysts to hunt signals like beaconing, DNS tunneling, and long-lived connections—subtle signs of compromise that often slip past traditional defenses

[Official Rita Github Repository](https://github.com/activecm/rita)

## Setup
- Go to the latest release of **Rita** [here](https://github.com/activecm/rita/releases) and get the compressed installer, at my time it is ``rita-v5.0.8.tar.gz``, the version will change eventually
- Uncompress the installer
```bash
tar -xf rita-v5.0.8.tar.gz
```
- **Cd** into it
```bash
cd rita-v5.0.8-installer/
```
- Run the install script
```bash
./install_rita.sh localhost
```
- Test it
```bash
rita h
```

## Why RITA Matters for SOC Teams
- **Behavior‑driven hunting:** Unlike static detection rules, RITA surfaces patterns—like regular heartbeats or long-standing sessions—that indicate potential C2 even from unknown malware
- **Accelerated triage:** The latest version consolidates all threat types into one interface—no more juggling ``show-beacons``, ``show-long-connections``, etc, everything’s visible in one streamlined view
- **Scalable & fast:** RITA 5 uses ClickHouse instead of MongoDB, offering 2× to over 20× faster data ingestion and analysis—capable of handling networks pushing ~100 Gbps

## Usage

---
[Back to the section](/courseFiles/Section_05-networkingAndTelemetry/networkingAndTelemetry.md)
