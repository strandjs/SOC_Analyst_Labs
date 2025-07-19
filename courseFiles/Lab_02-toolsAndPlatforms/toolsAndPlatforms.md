# Security Tools & Foundational Platforms
**Security tools and foundational platforms** are the core technologies used to detect, investigate, and respond to cyber threats. These include tools that collect and analyze data from endpoints, networks, and systems to provide visibility into suspicious activity
<br><br>

Categories of Security Tools
- **Endpoint Detection and Response** (EDR) - Tools like [LimaCharlie](/courseFiles/tools/LimaCharlie.md) monitor activities on endpoints (e.g., workstations and servers), collecting telemetry and enforcing detection logic in real-time
- **Security Information and Event Management** (SIEM) - Platforms such as [Elastic SIEM](/courseFiles/tools/Elastic.md) aggregate logs from across the infrastructure, providing detection rules, dashboards, and analytics
- **Network Monitoring Tools** - Tools like Zeek or Wireshark are used to inspect raw network traffic and identify anomalies or known malicious behavior

## Intro
**A Security Operations Center** (SOC) is a centralized unit that monitors, detects, responds to, and mitigates cybersecurity threats in real time. SOC analysts are the front line of defense, working with a variety of tools and platforms to protect an organization’s assets

This lab introduces interns to **foundational tools and platforms** used daily in a SOC environment. Understanding how data flows from endpoints to security platforms—and how to investigate, triage, and act—is key to being an effective SOC analyst

## LimaCharlie Hands-On
[LimaCharlie](/courseFiles/tools/LimaCharlie.md) is a cloud-native EDR and infrastructure-as-a-service platform. It collects detailed telemetry from endpoints and allows for custom detection and response rules

After setting it up, you can try the [LimaCharlie Lab](/courseFiles/Lab_02-toolsAndPlatforms/limaCharlieLab.md)

## Elastic SIEM Hands-On
[Elastic SIEM](/courseFiles/tools/Elastic.md), part of the Elastic Stack (Elasticsearch, Logstash, Kibana), provides a flexible and powerful SIEM solution for log ingestion, search, visualization, and detection

After setting it up, you can try the [Elastic Lab](/courseFiles/Lab_02-toolsAndPlatforms/elasticLab.md)

## Viewing Alerts & Logs
SOC analysts must interpret alerts in context and verify their validity

Understanding Alerts:
- **Components** - Rule name, severity, MITRE technique, timestamp, affected host/user, raw log snippet
- **Enrichment** - Threat intel (e.g., VirusTotal hash lookup), geolocation, asset context
- **Triage Steps**
1. Is this a known good or benign behavior?
2. Can we correlate with other logs to confirm malicious intent?
3. Are other hosts showing similar behavior?

Log Types to Recognize:
- **Windows Event Logs** (Security, System, Application)
- **Sysmon events** (detailed host telemetry)
- **Firewall logs** (source/destination IP, port, action)
- **DNS logs** (lookups to malicious domains)
- **Web proxy logs** (user-agent, URL visited)

## Writing & Modifying Basic Detection Rules
Detection rules define what behavior is suspicious and should generate alerts. Interns should be able to read, tweak, and eventually write basic rules.

Detection Rule Elements
- **Condition** - What patterns or values to match (e.g., parent process = cmd.exe, child process = powershell.exe)
- **Filters/Exceptions** - Known-good behaviors to suppress false positives
- **Severity & Tactic** - Classification based on MITRE ATT&CK

Examples
- **Sigma Rule (YAML)** - <pre>Detect PowerShell with base64-encoded strings</pre>
- **Elastic Rule (KQL)** - <pre>event.code: 4625 and winlog.event_data.LogonType: 3</pre>
- **LimaCharlie Rule (YAML)** - <pre>Match file writes to suspicious locations</pre>

## Telemetry Searching
Analysts often need to go beyond alerts and search the raw telemetry for related or supporting evidence

Key Skills
- **Search Syntax** - Learn how to query data (e.g., KQL in Elastic, telemetry filters in LimaCharlie)
- **Pivoting** - From an IP to related processes, users, or domains
- **Filtering** - Time ranges, specific hostnames, or event types<br>
- **Common Use Cases:**
1. "Show all PowerShell executions on this host in the last 24 hours"
2. "List all logon events from a suspicious IP"
3. "Search for DLL side-loading activity using Sysmon logs"

***                                                       

<b><i>Continuing the course?</b>
</br>
[Click here for the Next Lab](/courseFiles/Lab_03-detectionAndThreatBehavior/detectionAndThreatBehaviormd)</i>

<b><i>Want to go back?</b>
</br>
[Click here for the Previous Lab](/courseFiles/Lab_01-logAnalysis_Basics/logAnalysis_basicsmd)

<b><i>Looking for a different lab? </b></br>[Back to Lab Directory](/coursenavigationmd)</i>

