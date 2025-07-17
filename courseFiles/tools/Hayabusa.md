Being the first time you have probably heard about this tool, if you search it up you will get some japanese motorcycles, search Hayabusa event viewer.
[Hayabusa-Repo](https://github.com/Yamato-Security/hayabusa)
# What I used to install on a fedora OS:
- $sudo dnf install git rust cargo
- $git clone https://github.com/Yamato-Security/hayabusa.git
- $cd hayabusa
- $cargo build --release
- ### I got an error on the build and had to install PerlCore: $sudo dnf install perl-core + $cargo clean + again $cargo build --release
- $sudo cp target/release/hayabusa /usr/local/bin/  (so I can use it from anywhere)

### FYI 'dnf' is the same as 'apt' and 'cargo' is pretty much 'make' from kali

# Using the actual tool
## Some commands that I found most interesting and useful:
- ### $hayabusa update-rules
Updates detection rules(necessary)

- $`hayabusa log-metrics --file something.evtx`
Check log file Metadata

- $`hayabusa csv-timeline --file something.evtx -o timeline.csv`
This creates a DFIR timeline in CSV format 

- $`hayabusa json-timeline --file something.evtx -o timeline.json`
Same, but in JSON format

- $`hayabusa eid-metrics --file something.evtx`
Summarize events by ID

- $`hayabusa computer-metrics --file Security.evtx`
Summarize events by Computer Name

- $`hayabusa extract-base64 --file Security.evtx --output decoded.txt`
Extract Base64 strings

- $`hayabusa search --file something.evtx --keyword powershell`
Search by keyword

- `$hayabusa logon-summary --file something.evtx`
Get Logon activity summary


# Some notes and links
- This tools is basically a cli version of the Windows Event Viewer, much better in my opinion, but it can't work in real time
- Had a hard time finding the new command syntaxes, as they have changed over the years
- I prefer it to the Windows Event Viewer, easier to do bulk searching
- You can't do much without updating the rules
- You still need to know what to look for in the files you export, it doesn't hint you towards anything, just makes you do 80% of your job in 20% of the time
- Took me a good while to find some good .evtx file to play with: [Log File For Lab](https://github.com/sbousseaden/EVTX-ATTACK-SAMPLES/blob/master/AutomatedTestingTools/PanacheSysmon_vs_AtomicRedTeam01.evtx)
