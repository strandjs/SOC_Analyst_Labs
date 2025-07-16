Windows Event Viewer is a built-in administrative tool that allows users to view and analyze logs of system, security, and application events on a Windows machine. It’s essential for troubleshooting, auditing, and monitoring system activity in real time.

You can open it either through the **Start Menu Search**
<img width="781" height="679" alt="image" src="https://github.com/user-attachments/assets/4d586a4f-8d06-444a-a2bc-a097aef8c871" />
<br><br>

Or through the **Run Dialog**

`WIN + R`

Then type

`eventvwr.msc`

<img width="390" height="195" alt="image" src="https://github.com/user-attachments/assets/d4a049bf-bee3-4dac-bea8-7cf4ae30325e" />
<br><br>

There are multiple types of logs
- **Application**  - Logs from applications like SQL Server, Outlook, etc
- **Security**  - Audit logs for logon attempts, file access, etc
- **System**  - Logs from Windows system components like drivers and services
- **Setup**  - 	Logs from system setup processes (e.g., Windows updates)
- **Forwarded Events**	- Logs collected from remote computers

![Screenshot 2025-07-16 180150](https://github.com/user-attachments/assets/1ee0e202-b7e3-40b9-97f6-486e4ea687f9)
You can open the **Security** logs to experiment around with the alerts in there
<br><br>

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






