## The objective of this lab is to use Hayabusa to analyze Sysmon logs and detect suspicious activity related to process creation, network connections, and authentication events.

**If you don't have hayabusa installed follow the tutorial from the [Hayabusa Documentation](/courseFiles/tools/Hayabusa.md)**


To start off we need to make sure we have the detection rules of hayabusa

$ `hayabusa update-rules`

<img width="745" height="189" alt="image" src="https://github.com/user-attachments/assets/271348e7-8d88-4962-a761-798c01e173e3" />


Let's also get the logs that we will be working with

$ `wget https://github.com/sbousseaden/EVTX-ATTACK-SAMPLES/blob/master/AutomatedTestingTools/PanacheSysmon_vs_AtomicRedTeam01.evtx`

