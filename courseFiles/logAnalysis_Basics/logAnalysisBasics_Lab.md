## The objective of this lab is to use Hayabusa to analyze Sysmon logs and detect suspicious activity related to process creation, network connections, and authentication events.

**If you don't have hayabusa installed follow the tutorial from the [Hayabusa Documentation](/courseFiles/tools/Hayabusa.md)**


To start off we need to make sure we have the detection rules of hayabusa

$ `hayabusa update-rules`

<img width="745" height="189" alt="image" src="https://github.com/user-attachments/assets/271348e7-8d88-4962-a761-798c01e173e3" />


Let's also get the logs that we will be working with and rename them

$ `wget https://github.com/sbousseaden/EVTX-ATTACK-SAMPLES/blob/master/AutomatedTestingTools/PanacheSysmon_vs_AtomicRedTeam01.evtx`

$ `mv PanacheSysmon_vs_AtomicRedTeam01.evtx sysmon.evtx`

First thing we will do to start disecting the logs is to get some basic metrics to understand what system the logs came from, number of events, time range.

$ `hayabusa log-metrics --file sysmon.evtx`

<img width="1917" height="611" alt="image" src="https://github.com/user-attachments/assets/473ad610-410e-4f82-b7bd-1f6310fc7437" />
<br>The logs span about 30 minutes and there are only 565 events, small enough to dig manually but we will do it the smart way.<br>
Next let's see the Event ID Distribution to dentify common or suspicious Sysmon events, we are looking for **1**, **3**, **10**, **11** or even **8**

$ `hayabusa eid-metrics --file sysmon.evtx`

<img width="627" height="503" alt="image" src="https://github.com/user-attachments/assets/f8a12a53-889d-4dd3-af42-d992bf8ec41c" />





