## The objective of this lab is to use Hayabusa to analyze Sysmon logs and detect suspicious activity related to process creation, network connections, and authentication events.

**If you don't have hayabusa installed follow the tutorial from the [Hayabusa Documentation](/courseFiles/tools/Hayabusa.md)**
<br><br>

- To start off we need to make sure we have the detection rules of hayabusa

$ `hayabusa update-rules`

<img width="745" height="189" alt="image" src="https://github.com/user-attachments/assets/271348e7-8d88-4962-a761-798c01e173e3" />


Let's also get the logs that we will be working with and rename them

$ `wget https://github.com/sbousseaden/EVTX-ATTACK-SAMPLES/blob/master/AutomatedTestingTools/PanacheSysmon_vs_AtomicRedTeam01.evtx`

$ `mv PanacheSysmon_vs_AtomicRedTeam01.evtx sysmon.evtx`

<br>

- First thing we will do to start disecting the logs is to get some basic **metrics** to understand what system the logs came from, number of events, time range.

$ `hayabusa log-metrics --file sysmon.evtx`

<img width="1917" height="611" alt="image" src="https://github.com/user-attachments/assets/473ad610-410e-4f82-b7bd-1f6310fc7437" />
The logs span about 30 minutes and there are only 565 events, small enough to dig manually but we will do it the smart way.<br><br>

- Next let's see the Event **ID Distribution** to dentify common or suspicious Sysmon events, we are looking for **1**, **3**, **10**, **11** or even **8**

$ `hayabusa eid-metrics --file sysmon.evtx`

<img width="627" height="503" alt="image" src="https://github.com/user-attachments/assets/f8a12a53-889d-4dd3-af42-d992bf8ec41c" />

Important observations:
1. **Process Creation (ID 1 = 90%)**, that's extremely high volume, and now our primary hunting ground
2. **WMI Activity (IDs 19, 20, 21)**, rare in normal activities, could be remote execution
3. **Network Connections (ID 3)**, check what process made the connection, destination IP/port, and timing.<br><br>

- Now let's proceed with a **Full Timeline Analysis**

$ `hayabusa csv-timeline --file sysmon.evtx -o timeline.csv` (include all rules)

<img width="989" height="1028" alt="image" src="https://github.com/user-attachments/assets/79c127a4-193d-480b-89d8-96735323296e" />

Immediately we can see some really telling information, we got hits on 50 events(8.85%), 11 of them being critical alerts of a known backdoor and ransomware

Let's dig deeper

$ `less timeline.csv | grep "high"`

One of the alerts looks like this:

<pre>"2019-07-19 17:57:04.412 +03:00","Proc Exec (Non-Exe Filetype)","high","MSEDGEWIN10","Sysmon",1,4070,"Cmdline: C:\Users\IEUser\AppData\Local\Temptcm.tmp -decode c:\file.exe file.txt ¦ Proc: C:\Users\IEUser\AppData\Local\Temptcm.tmp ¦ User: MSEDGEWIN10\IEUser ¦ ParentCmdline: cmd.exe /c C:\Users\IEUser\AppData\Local\Temptcm.tmp -decode c:\file.exe file.txt ¦ LID: 0x50951 ¦ LGUID: 747F3D96-D4B4-5D31-0000-002051090500 ¦ PID: 6260 ¦ PGUID: 747F3D96-DA40-5D31-0000-0010AB5F3C00 ¦ ParentPID: 3932 ¦ ParentPGUID: 747F3D96-DA40-5D31-0000-0010565D3C00 ¦ Description: CertUtil.exe ¦ Product: Microsoft® Windows® Operating System ¦ Company: Microsoft Corporation ¦ Hashes: SHA1=459D928381CDDFDC31D03C3DA5C28E63B1190194,MD5=535CF1F8E8CF3382AB8F62013F967DD8,SHA256=85DD6F8EDF142F53746A51D11DCBA853104BB0207CDF2D6C3529917C3C0FC8DF,IMPHASH=683B8A445B00A271FC57848D893BD6C4","CurrentDirectory: C:\AtomicRedTeam\ ¦ FileVersion: 10.0.17763.1 (WinBuild.160101.0800) ¦ IntegrityLevel: High ¦ ParentImage: C:\Windows\System32\cmd.exe ¦ RuleName: ¦ TerminalSessionId: 1 ¦ UtcTime: 2019-07-19 14:57:04.381","8d1487f1-7664-4bda-83b5-cb2f79491b6a"
</pre>
We get the command: "**C:\Users\IEUser\AppData\Local\Temptcm.tmp -decode c:\file.exe file.txt**" which is a classic Living-off-the-Land (LOLBAS) technique, certutil -decode is often used to decode base64-encoded payloads that were dropped by phishing or scripts

Why it's suspicious?
1. **CertUtil.exe** isn't normally used by regular users
2. Executing from AppData\Local with a .tmp file? Classic sign of malware staging
3. Suggests payload delivery step in malware chain

Following the chain we meet these commands:

**sc.exe create AtomicTestService binPath= C:\AtomicRedTeam\atomics\T1050\bin\AtomicService.exe** - Service Creation for Persistence

**sc.exe start AtomicTestService** - Service Execiution

**sc.exe stop AtomicTestService** - Service Stop (Cleanup?)<br><br>

- We can also do some **Hunting Scenarios**, searching for special keywords

$ `hayabusa search --file sysmon.evtx --regex '(?i)(cmd\.exe|powershell|whoami|mimikatz)'`

<img width="1915" height="661" alt="image" src="https://github.com/user-attachments/assets/3a70ca93-4c36-4f79-96f1-435322948684" />

Following up this lead we can get to the same results as earlier, or use it to group alerts by services, the possibilities are endless
<br><br

Try extracting any encrypted payloads and pulling authentication activity yourself, if there is any, using the documentation of the tool.



