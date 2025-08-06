Windows Event Viewer is a built-in administrative tool that allows users to view and analyze logs of system, security, and application events on a Windows machine. It’s essential for troubleshooting, auditing, and monitoring system activity in real time.

You can open it either through the **Start Menu Search**
<img width="784" height="684" alt="image" src="https://github.com/user-attachments/assets/9565a313-6199-40d1-8d35-accebc217f94" />
<br>

Or through the **Run Dialog**

```
WIN + R
```

Then type

```
eventvwr.msc
```

<img width="405" height="225" alt="image" src="https://github.com/user-attachments/assets/db042d24-6818-479f-be11-8452ee889a54" />
<br>

There are multiple types of logs
- **Application**  - Logs from applications like SQL Server, Outlook, etc
- **Security**  - Audit logs for logon attempts, file access, etc
- **System**  - Logs from Windows system components like drivers and services
- **Setup**  - 	Logs from system setup processes (e.g., Windows updates)
- **Forwarded Events**	- Logs collected from remote computers

<img width="1507" height="995" alt="image" src="https://github.com/user-attachments/assets/13d8e7d2-9674-4f82-acd3-66e552674e8f" />
You can open the **DC1-secLogs-3-26-DomainPasswordSpray** logs to experiment around with the alerts in there
<br>

Stuff you can with this tool
- **Search** - Right-click a log → Find → Type keywords (e.g., error, shutdown)
- **Filter** - Right-click log → Filter Current Log (Filter by Level, Event ID, Source, Time, Keywords, Users, et.)
- **Custom Time Range** - Filter to events within a specific date/time range

Some useful IDs
- **4624** - Successful logon
- **4625** - Failed logon attempt
- **6005** - Event log service started (system startup)
- **6006** - Event log service stopped (system shutdown)

Advanced Features
- **Custom Views** - Create filters that persist to track specific events over time
- **Event Subscriptions** - Collect events from remote computers using Event Forwarding (requires setup via Group Policy)
- **Export Logs** - Right-click a log → Save All Events As (.evtx, .txt, .csv, .xml)
- **Task Scheduling** - Right-click an event → Attach Task to This Event to trigger actions (email, script, etc)


---
[Back to the Lab](/courseFiles/Lab_01-logAnalysis_Basics/logAnalysis_basics.md)





