# Lab: Introduction to Detection & Threat Behavior

## Goal
Simulate and detect basic adversarial techniques mapped to the MITRE ATT&CK framework using PowerShell, Sysmon, and open-source tools.

---

## Step 1: Install Sysmon with Configuration

1. Download these:
- [Sysmon](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon)
- [Sysmon config](https://github.com/SwiftOnSecurity/sysmon-config)
- [procdump](https://learn.microsoft.com/en-us/sysinternals/downloads/procdump)
- [Hayabusa](https://github.com/Yamato-Security/hayabusa/releases/download/v3.2.0/hayabusa-3.2.0-win-x64.zip)

2. Extract the archives:

![archive extract](https://i.ibb.co/wNbnzyPk/image.png)

3. Move the **Sysmon config** to the extracted Sysmon directory

![move sysmon](https://i.ibb.co/nqktYbB8/image.png)

4. Open **Command Prompt**.

![cmd](https://i.ibb.co/tPMQDmvf/image.png)

5. Navigate to the Sysmon directory:

```cmd
cd C:\Users\Administrator\Downloads\Sysmon
```

6. Install Sysmon with the provided configuration:

```cmd
Sysmon64.exe -accepteula -i sysmonconfig-export.xml
```

![cmd sysmon install](https://i.ibb.co/hRDFjvs0/image.png)

---

## Step 2: Simulate ATT&CK Techniques

### Tactic 1: Execution
**Technique**: PowerShell with EncodedCommand  
**ATT&CK ID**: [T1059.001](https://attack.mitre.org/techniques/T1059/001/)

1. Open **PowerShell**.

![powershell](https://i.ibb.co/Lzw3mXmj/image.png)

2. Run the following script:

```powershell
$command = 'Start-Process notepad.exe'
$bytes = [System.Text.Encoding]::Unicode.GetBytes($command)
$encoded = [Convert]::ToBase64String($bytes)
powershell.exe -EncodedCommand $encoded
```

![powershell tactic 1](https://i.ibb.co/VdTbYWY/image.png)

- this should open a Notepad window.

---

### Tactic 2: Credential Access
**Technique**: LSASS Dumping with ProcDump  
**ATT&CK ID**: [T1003.001](https://attack.mitre.org/techniques/T1003/001/)

1. Navigate to the `Procdump` directory:

```cmd
cd C:\Users\Administrator\Downloads\Procdump
```

2. Run the memory dump command:

```cmd
.\procdump.exe -ma lsass.exe lsass.dmp
```

![powershell tactic 2](https://i.ibb.co/Xr7qG10P/image.png)

>[!IMPORTANT]
>
> **Note**: Windows Defender may block this action. If necessary, disable it temporarily for testing.

---

## Step 3: Analyze with Hayabusa

1. Open **CMD**
2. Navigate to the Hayabusa directory:

```cmd
cd C:\Users\Administrator\Downloads\hayabusa-3.2.0-win-x64
```

3. Generate an ATT&CK-mapped CSV timeline from Sysmon logs:

```cmd
hayabusa-3.2.0-win-x64 csv-timeline --file "C:\Windows\System32\winevt\Logs\Microsoft-Windows-Sysmon%4Operational.evtx" -o results.csv
```

>[!TIP]
>
>use 3. Core++ (3,952 rules) ( status: experimental, test, stable | level: medium, high, critical )
>
>Include sysmon rules? (1,977 rules) · yes

---

## Step 4: Map Activity to MITRE ATT&CK

Map the activity from result.csv as in the example below:

| Tactic             | Technique                     | Example Command                               | Sysmon Event |
|--------------------|-------------------------------|-----------------------------------------------|--------------|
| Execution          | PowerShell EncodedCommand     | `powershell.exe -EncodedCommand ...`          | ID 1         |
| Credential Access  | LSASS Dumping (ProcDump)      | `procdump.exe -ma lsass.exe`                  | ID 10        |

---

## Evidence & Detection (results.csv Summary)

I attached a file named [results.csv](./results.csv) which is the summary from testing the lab. Down below are some notes from the Tactic detections

### Tactic 1: Execution via Encoded PowerShell Commands

These events indicate the use of base64-encoded PowerShell commands—a known obfuscation and execution technique.

- **Detection**: Suspicious Encoded PowerShell Command Line  
- **Severity**: High  
- **Example Timestamp**: `2025-07-16 17:16:08.919 +03:00`  
- **Detection Rows**: 94 through 124 (and more)  
- **Indicators**:
  - Use of `-EncodedCommand` flag
  - Multiple repeated command-line executions

---

### Tactic 2: Credential Dumping via LSASS / ProcDump

These events show interaction with the `lsass.exe` process—an indicator of credential dumping.

- **Detection**: 
  - LSASS Process Memory Dump
  - Tools Dropping Dump Files
  - `lsass` or `procdump` in CommandLine
- **Severity**: High  
- **Example Timestamp**: `2025-07-16 17:19:56.021 +03:00`  
- **Detection Rows**: 1–16 and 56–148  
- **Indicators**:
  - `procdump.exe` usage
  - Creation of `lsass.dmp`
  - Alerts on memory access to `lsass.exe`


# links and sources:
https://github.com/SwiftOnSecurity/sysmon-config

https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon

https://learn.microsoft.com/en-us/sysinternals/downloads/procdump

https://github.com/Yamato-Security/hayabusa

https://www.microsoft.com/en-ca/software-download/windows10

https://www.virtualbox.org/

---

For learning more about MITRE ATT&CK Framework check out [MITRE_ATT&CK.md](/courseFiles/Section_03-detectionAndThreatBehavior/MITRE_ATT&CK.md)


***                                                       

<b><i>Continuing the course?</b>
</br>
[Click here for the Next Section](/courseFiles/Section_04-socScripting/socScripting.md)</i>

<b><i>Want to go back?</b>
</br>
[Click here for the Previous Section](/courseFiles/Section_02-toolsAndPlatforms/toolsAndPlatforms.md)

<b><i>Looking for a different section? </b></br>[Back to Section Directory](/coursenavigation.md)</i>
