# Lab 2 Solution: PowerShell - Collect Basic System Info and Save to File

## Overview

This guide walks through a step-by-step solution to the PowerShell lab for collecting system information and saving it to a text file named `system_info.txt`.

---

## Step-by-Step Solution

### 1. Open PowerShell

- Press `Win + X` and select **Windows PowerShell** or **Terminal (Admin)** to open PowerShell with administrative privileges (recommended for full access).

### 2. Create a New PowerShell Script File

To begin scripting, create a `.ps1` file:

```powershell
New-Item -Path C:\Users\user\Desktop -Name "collect_system_info.ps1" -ItemType "File"
```

This will create a blank PowerShell script in your Desktop directory.

You can also open it in a text editor (like VS Code, Notepad++, or the built-in Notepad) to paste in the script.

---

## 3. Write the Script

### a. Get the Hostname

```powershell
$hostname = $env:COMPUTERNAME
```

This uses the built-in environment variable `COMPUTERNAME`.

### b. Get the Current Username

```powershell
$username = whoami
```

This gives the fully qualified domain\username.

### c. Get IP Address(es)

```powershell
$ipAddresses = (Get-NetIPAddress -AddressFamily IPv4 | Where-Object {$_.IPAddress -notlike '169.*'}).IPAddress
```

Filters out automatic private IPs (e.g., 169.254.x.x).

### d. Get OS Version

```powershell
$os = (Get-CimInstance Win32_OperatingSystem).Caption
```

Returns a friendly OS name like "Microsoft Windows 10 Pro".

### e. List Running Processes

```powershell
$processes = Get-Process | Select-Object -ExpandProperty ProcessName
```

Gets only the process name field.

### f. Get Active Network Connections

```powershell
$netConnections = netstat -n | Select-String "^  TCP"
```

Filters out only TCP connections from `netstat -n` output.

---

## 4. Write Output to File

Use `Out-File` and `Add-Content` to build the output:

```powershell
"Hostname: $hostname" | Out-File system_info.txt
"Username: $username" | Add-Content system_info.txt
"IP Address: $($ipAddresses -join ", ")" | Add-Content system_info.txt
"OS Version: $os`n" | Add-Content system_info.txt

"Running Processes:" | Add-Content system_info.txt
"------------------" | Add-Content system_info.txt
$processes | Sort-Object | Add-Content system_info.txt

"`nActive Network Connections:" | Add-Content system_info.txt
"---------------------------" | Add-Content system_info.txt
$netConnections | Add-Content system_info.txt
```

---

## 5. Run the Script

After saving the script in your `.ps1` file, run it in PowerShell:

```powershell
.\collect_system_info.ps1
```
>NOTE: You may need to cd to Desktop, use `cd C:\Users\user\Desktop`
> ⚠️ If script execution is disabled, run the following command to allow local scripts:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

---

## Full PowerShell Script

```powershell

$hostname = $env:COMPUTERNAME
$username = whoami
$ipAddresses = (Get-NetIPAddress -AddressFamily IPv4 | Where-Object {$_.IPAddress -notlike '169.*'}).IPAddress
$os = (Get-CimInstance Win32_OperatingSystem).Caption
$processes = Get-Process | Select-Object -ExpandProperty ProcessName
$netConnections = netstat -n | Select-String "^  TCP"

"Hostname: $hostname" | Out-File system_info.txt
"Username: $username" | Add-Content system_info.txt
"IP Address: $($ipAddresses -join ", ")" | Add-Content system_info.txt
"OS Version: $os`n" | Add-Content system_info.txt

"Running Processes:" | Add-Content system_info.txt
"------------------" | Add-Content system_info.txt
$processes | Sort-Object | Add-Content system_info.txt

"`nActive Network Connections:" | Add-Content system_info.txt
"---------------------------" | Add-Content system_info.txt
$netConnections | Add-Content system_info.txt
```

---

