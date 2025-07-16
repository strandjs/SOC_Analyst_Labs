# Log Analysis Basics

Log analysis involves reviewing system and security logs to detect unusual or malicious activity. Each log entry typically includes a timestamp, source, user account, event type, and a unique Event ID.
Most important IDs are:
- **4624** = Succesfull Logon
- **4625** = Failed logon
- **4688** = Process creation
- **4670** = Permission changes

Effective log analysis involves:
- Filtering noise
- Correlating events over time (easy using special tools like [Hayabusa](/courseFiles/tools/Hayabusa.md)
- Flagging anomalies like brute-force logins or unusual logon times



## Sysmon Logs
Sysmon (System Monitor) is a Windows system service that logs detailed system activity to the Event Log, beyond what standard logs capture. It’s often used in security monitoring and DFIR.
Sysmon logs appear under the Microsoft-Windows-Sysmon/Operational and include details like:
- **Event ID 1** – Process creation (with full command line, parent/child PID)
- **Event ID 3** – Network connections
- **Event ID 10** – Process access (used for example in credential dumping detection)
- **Event ID 11** – File creation



## Authentication Logs
Authentication logs include detailed information about the device used to access the service, the user’s location, and other considerations that might influence risk. Generally, these logs only include information about the following events:

- Successful logins
- Login attempts
- Login errors
- Logouts, with additional information shows whether a logout was manual or due to session expiration.

This information can be useful to detect identity breaches. We can use authentication logs to identify brute force credential-guessing attempts, for example, as this will show up as failed authentications in the audit trail. They can pinpoint users that were affected by a breach, but not what those user accounts were able to access/do. That is where authorization audit logs come into play. Authorization decision logs will allow us to define the blast radius of the breach.



## Tools to Learn
Viewing alerts and logs is key to detecting suspicious activity on a system. Tools like [Hayabusa](/courseFiles/tools/Hayabusa.md) allow analysts to quickly analyze Windows event logs (.evtx), apply detection rules, and generate timelines or alerts for threats such as privilege escalation, malware, or lateral movement as well as the built in [Windows Event Viewer](/courseFiles/tools/WinEventViewer.md).


***                                                       

<b><i>Continuing the course?</b>
</br>
[Click here for the Next Lab](/courseFiles/toolsAndPlatforms/toolsAndPlatforms.md)</i>

<b><i>Want to go back?</b>
</br>
[Click here for the Previous Lab](/courseFiles/welcome/welcome.md)

<b><i>Looking for a different lab? </b></br>[Back to Lab Directory](/coursenavigation.md)</i>
