**Volatility** is the world's most widely used framework for extracting digital artifacts from volatile memory (RAM) samples. The extraction techniques are performed completely independent of the system being investigated but offer visibility into the runtime state of the system. The framework is intended to introduce people to the techniques and complexities associated with extracting digital artifacts from volatile memory samples and provide a platform for further work into this exciting area of research

[Volatility Main Github Repo](https://github.com/volatilityfoundation/volatility3)

Volatility 3 is a complete rewrite of the original framework released in 2019, built to address performance, architecture, and modularity limitations of Volatility 2. It features an improved license (Volatility Software License), clean design, and better extensibility

## Setup

All you need is to clone it's repo and cd in
```bash
git clone https://github.com/volatilityfoundation/volatility3.git 
```
```bash
cd volatility3
```

To run it do
```bash
python3 vol.py
```

## General Usage

To list needed plugins and get help you can use

- For **Windows**
```bash
python3 vol.py -h | grep windows
```

- For **Linux**
```bash
python3 vol.py -h | grep linux
```

- For general help
```bash
python3 vol.py -h
```

- For specific commands ( change ``windows.pslist.PsList`` with whatever command you wish )
```bash
python3 vol.py windows.pslist.PsList -h
```

## Windows Usage
**Usefull commands**

- Lists processes seen in the OS’s active process list (name, PID, PPID, times, etc.)
```bash
python3 vol.py -f /path/to/memdump windows.pslist.PsList
```

- Shows processes in a parent/child tree to visualize lineage
```bash
python3 vol.py -f /path/to/memdump windows.pstree.PsTree
```

- Signature-scans memory to find process objects (including hidden/unlinked/terminated ones)
```bash
python3 vol.py -f /path/to/memdump windows.psscan.PsScan
```

- Extracts each process’s command-line arguments from its PEB
```bash
python3 vol.py -f /path/to/memdump windows.cmdline.CmdLine
```

- Lists DLLs/modules loaded by each process (base, size, path, load time)
```bash
python3 vol.py -f /path/to/memdump windows.dlllist.DllList
```

- Enumerates open kernel object handles per process (files, registry keys, mutexes, events, etc.)
```bash
python3 vol.py -f /path/to/memdump windows.handles.Handles
```

- Scans memory for ``FILE_OBJECTs`` to surface file artifacts (not just currently open)
```bash
python3 vol.py -f /path/to/memdump windows.filescan.FileScan
```

- Scans for kernel ``DRIVER_OBJECTs`` (can reveal hidden/unlinked drivers)
```bash
python3 vol.py -f /path/to/memdump windows.driverscan.DriverScan
```

- Flags process memory regions that look like injected code (exec-perms, not image-backed)
```bash
python3 vol.py -f /path/to/memdump windows.malware.malfind.Malfind
```

- Detects likely process hollowing (lists processes whose image has been replaced in memory)
```bash
python3 vol.py -f /path/to/memdump windows.malware.hollowprocesses.HollowProcesses
```

- Lists System Service Descriptor Table entries (index, function, owning driver) to help spot SSDT hooks
```bash
python3 vol.py -f /path/to/memdump windows.ssdt.SSDT
```

## Linux Usage
**Usefull commands**

- Lists tasks from the kernel’s task list (PID, PPID, start times, etc.)
```bash
python3 vol.py -f /path/to/memdump linux.pslist.PsList
```

- Shows parent/child process relationships as a tree
```bash
python3 vol.py -f /path/to/memdump linux.pstree.PsTree
```

- Signature-scans memory to find process objects (can catch hidden/terminated ones)
```bash
python3 vol.py -f /path/to/memdump linux.psscan.PsScan
```

- Processes with their full command-line arguments
```bash
python3 vol.py -f /path/to/memdump linux.psaux.PsAux
```

- Recovers Bash command history straight from bash process memory
```bash
python3 vol.py -f /path/to/memdump linux.bash.Bash
```

- Dumps per-process environment variables
```bash
python3 vol.py -f /path/to/memdump linux.envars.Envars
```

- Lists memory-mapped ELF files (binaries/libraries) across processes
```bash
python3 vol.py -f /path/to/memdump linux.elfs.Elfs
```

- Shows each process’s memory maps (VMAs), useful for spotting injected/executable regions
```bash
python3 vol.py -f /path/to/memdump linux.proc.Maps
```

- Lists open file descriptors for each process (paths, FDs)
```bash
python3 vol.py -f /path/to/memdump linux.lsof.Lsof
```

- Lists loaded kernel modules (Linux “drivers”)
```bash
python3 vol.py -f /path/to/memdump linux.lsmod.Lsmod
```

- Flags process memory regions that look like injected code (executable, not file-backed, etc.)
```bash
python3 vol.py -f /path/to/memdump linux.malware.malfind.Malfind
```

- Checks the system call table for hooks (classic kernel rootkit indicator)
```bash
python3 vol.py -f /path/to/memdump linux.malware.check_syscall.Check_syscall
```

- Carves for hidden kernel modules (note: marked deprecated in current docs).
```bash
python3 vol.py -f /path/to/memdump linux.malware.hidden_modules.Hidden_modules
```

- Lists all network sockets/connections for all processes across families (AF_INET/AF_INET6/AF_UNIX, etc.). Outputs include netns ID, FD number, family, type, protocol, plus source/destination (addr:port) and state; also surfaces any socket filters attached (e.g., BPF ids/names)
```bash
python3 vol.py -f /path/to/memdump linux.sockstat.Sockstat
```

## Some problems with linux
Volatility 3 uses **Intermediate Symbol Files (ISF)** that describe kernel types/offsets. Windows symbols can often be pulled automatically; Linux/macOS must usually be generated for the exact kernel that produced the dump

- To identify the kernel banner of the dump
```bash
python3 vol.py -f /path/to/memdump banners
```

- See what symbols you already have
```bash
python3 vol.py isfinfo
```

***Important***

If you don't want to install symbols for every linux dump, you can use a remote ISF

(edit volatility3/framework/constants/__init__.py)
<pre>REMOTE_ISF_URL = "https://raw.githubusercontent.com/leludo84/vol3-linux-profiles/main/banners-isf.json"</pre>

***Or do***
```bash
SYMS='--remote-isf-url https://github.com/Abyss-W4tcher/volatility3-symbols/raw/master/banners/banners.json'
```

And then all the commands would look like this

```bash
python3 vol.py -f /path/to/memdump $SYMS linux.pslist.PsList
```

### Notes
Volatility does not provide the ability to acquire memory, for that best use scenario is [LiME](https://github.com/504ensicsLabs/LiME), and for windows [WinPmem](https://github.com/Velocidex/WinPmem) from Velociraptor

# Try our [Volatility Lab](/courseFiles/Section_09-forensicsFundamentals/volatilityLab1.md)

---
[Back to the section](/courseFiles/Section_09-forensicsFundamentals/forensicsFundamentals.md)
