# About
**Dionaea** is a low-interaction honeypot designed to capture malware and exploits targeting services such as
- SMB (port 445)
- HTTP (port 80)
- FTP (port 21)
- TFTP
- MSSQL
- SIP

It emulates vulnerable services, logs attacker interactions, and stores any malware that is dropped, **Dionaea** is especially useful for SOC analysts, threat researchers, and blue teams to understand attacker behavior and collect Indicators of Compromise (IOCs)

| Use Case  | Description |
| ------------- | ------------- |
| Cyber Deception  | Trick attackers into interacting with fake services |
| Threat Intelligence | Collect malware and IPs for IOC feeds |
| Malware Analysis | Capture real-world malware for sandbox analysis |
| Attack Surface Monitoring | Observe how attackers scan and probe services |

### Features
- Emulates multiple vulnerable services
- Captures malware binaries
- Logs interaction in JSON format or SQLite DB
- Can forward logs to SIEM or threat intel platforms
- Supports integration with tools like ELK, Splunk, or Cuckoo Sandbox

# Installation
- $`sudo apt update && sudo apt upgrade -y`
- $<pre>sudo apt install -y \
  git cmake build-essential \
  libcurl4-openssl-dev libev-dev libglib2.0-dev \
  libnl-3-dev libnl-route-3-dev libpcap-dev \
  python3 python3-pip python3-venv \
  sqlite3 libsqlite3-dev libtool autoconf automake \
  libssl-dev libudns-dev libnetfilter-queue-dev</pre>
- $`sudo nano /dionaea/modules/CMakeLists.txt` - comment out anything emu related like this
<pre>#if(WITH_MODULE_EMU)
#  if(LIBEMU_FOUND)
#    add_subdirectory(emu)
#  else()
#    message(FATAL_ERROR "You have selected the emu module, but libemu could not be found")
#  endif()
#endif()
</pre>

- $`sudo git clone https://github.com/DinoTools/dionaea.git` + $`cd dionaea`
- $`mkdir build && cd build`
- $`nano ~/Desktop/dionaea/build/modules/python/setup.py` - make sure you have: `version = "0.11.0"`
- $`python3 -m venv ../venv`
- $`source ../venv/bin/activate`
- $`pip3 install Cython`
- $`pip3 install setuptools`
- $`pip3 install pyyaml`
- $`pip3 install boto3`
- $`mkdir -p venv/lib/python3.12/site-packages/distutils && cd venv/lib/python3.12/site-packages/distutils && for f in __init__ archive_util cmd config core debug dep_util dir_util dist errors extension fancy_getopt file_util log spawn util; do curl -sLO https://raw.githubusercontent.com/python/cpython/3.10/Lib/distutils/$f.py; done`
- $`cmake ..`
- $`make -j$(nproc)`
- $`sudo make install`
- $`sudo nano /usr/local/etc/dionaea/dionaea.cfg` - Delete anything emu related from modules and processors, should have 4 references from the start

# I know that was a lot... Now you can move over to the lab!
### [Dionaea Lab](/courseFiles/Lab_07-deceptionSystems/dionaeaLab.md)
