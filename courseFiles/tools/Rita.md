**RITA** stands for **Real Intelligence Threat Analytics**—an open-source framework that helps SOC analysts detect stealthy Command-and-Control (C2) behavior through network traffic patterns, it works by analyzing Zeek logs (TSV or JSON) or PCAPs converted into Zeek format, focusing on anomalies rather than signature-based detection

Rather than relying solely on known IoCs, RITA equips analysts to hunt signals like beaconing, DNS tunneling, and long-lived connections—subtle signs of compromise that often slip past traditional defenses

[Official Rita Github Repository](https://github.com/activecm/rita)

# Setup
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

# Why RITA Matters for SOC Teams
- **Behavior‑driven hunting:** Unlike static detection rules, RITA surfaces patterns—like regular heartbeats or long-standing sessions—that indicate potential C2 even from unknown malware
- **Accelerated triage:** The latest version consolidates all threat types into one interface—no more juggling ``show-beacons``, ``show-long-connections``, etc, everything’s visible in one streamlined view
- **Scalable & fast:** RITA 5 uses ClickHouse instead of MongoDB, offering 2× to over 20× faster data ingestion and analysis—capable of handling networks pushing ~100 Gbps

# Usage



// NOTE THAT MOST OF THE COMMANDS ARE FOR RITA v4. RITA v5 replaced most of the Examining data commands with this command:

```bash
rita view datasetname
```


## Importing & analyzing data

### From PCAP(s)

1. If you have multiple PCAPs, merge them first:

```bash
mergecap -w outfilename.pcap infilename1.pcap infilename2.pcap
```

2. Generate Zeek logs from a PCAP (example with daily log rotation):

```bash
zeek -r filename.pcap local "Log::default_rotation_interval = 1 day"
```

This will produce Zeek logs (conn.log, dns.log, http.log, user\_agent.log, etc.) which RITA consumes.

### Importing Zeek logs into RITA

- One-off import (single import of a directory of Zeek logs):

```bash
rita import /path/to/your/zeek_logs datasetname
```
> [!IMPORTANT]
>
> You might need to use `-l` after `rita import` for the log files if you are using RITA v5.

- Rolling import (progressively analyze logs as they arrive — useful for long captures or live log directories):

```bash
rita import --rolling /path/to/your/zeek_logs datasetname
```

> Default Zeek logs directory (common location on systems running Zeek):
>
> `/opt/zeek/logs/<date>`

---

## Examining data (commands & outputs)

RITA provides a set of commands to surface suspicious behaviours. Replace `datasetname` with the name you used when importing.

### List available datasets

```bash
rita list
```

### Beaconing (C2-like behavior)

- Detect hosts that show signs of C2/beaconing:

```bash
rita show-beacons -H datasetname | less -S
```

- FQDN-based beacon analysis:

```bash
rita show-beacons-fqdn -H datasetname | less -S
```

> `-H` shows host-oriented results (other output modes are available depending on dataset and RITA version).

### Fast beaconing/strobes

```bash
rita show-strobes -H datasetname | less -S
```

Strobes reveal very frequent, regular connections that may indicate automated tooling or covert-channel activity.

### Long connections

```bash
rita show-long-connections -H datasetname | less -S
```

These surface unusually long-lived sessions which may indicate interactive channels tunneled over HTTP or other protocols.

### User agent analysis

```bash
rita show-useragents -H datasetname | less -S
```

This can reveal anomalous or rare user-agent strings from clients.

### DNS / exploded DNS analysis

```bash
rita show-exploded-dns -H datasetname | less -S
```

This command highlights DNS activity that could reveal covert DNS channels or unusual query patterns.

### Blacklist hits (hosts & IPs)

- Hostnames that contacted any blacklisted domains:

```bash
rita show-bl-hostnames -H datasetname | less -S
```

- Source IPs that are blacklisted:

```bash
rita show-bl-source-ips -H datasetname | less -S
```

- Destination IPs that are blacklisted:

```bash
rita show-bl-dest-ips -H datasetname | less -S
```

---

## Filtering results and exclude lists

When working with noisy datasets, it's common to create exclude lists and filter RITA output with `grep` so the team can iteratively eliminate benign noise.

Example pattern to filter out IPs listed in a text file:

```bash
rita show-beacons datasetname | grep -v -w -F -f exclude-beacons.txt
```

- `exclude-beacons.txt` should contain one IP (or hostname) per line.
- Use similar files for other commands:
  - `exclude-strobes.txt` for strobes
  - `exclude-longconns.txt` for long connections
  - `exclude-bl-hostnames.txt`, `exclude-bl-source-ips.txt`, `exclude-bl-dest-ips.txt` for blacklist outputs

>[!TIP]
>
>kKeep a versioned exclude list per dataset so you can reproduce the analysis.

---

## Configuration & validation

The main RITA configuration file is:

```
/etc/rita/config.yaml
```

Edit it with your preferred editor (for example `sudo nano /etc/rita/config.yaml`). After changing the config, validate it with:

```bash
rita test-config
```

`rita test-config` checks for obvious configuration problems. Always run it before running large imports or scheduled tasks.

---

## Reports and exporting

Create an HTML report for an analyzed dataset:

```bash
rita html-report datasetname
```

The HTML report provides a static artifact you can hand to instructors, stakeholders, or include in lab write-ups.

---

## Dataset management

- Delete a dataset when you no longer need it:

```bash
rita delete datasetname
```

- Use `rita list` frequently to confirm dataset names and status.

---



*These commands are based of this official [RITA Cheat Sheet](https://www.activecountermeasures.com/wp-content/uploads/2021/06/RITA-Cheat-Sheet.pdf). Not all the commands have been verified!*



---
[Back to the section](/courseFiles/Section_05-networkingAndTelemetry/networkingAndTelemetry.md)
