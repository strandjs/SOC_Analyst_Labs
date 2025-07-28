# Soft Skills
Soft skills are what will make you stand out as a SOC analyst, even while technical skills are what got you in. Developing the mentality, communication patterns, and teamwork that increase your efficacy in a real-world Security Operations Center is the main goal of this session. Asking more intelligent questions, outlining your research in detail, recording your findings, and making a significant contribution to your team are all skills you will acquire. You'll not only develop more quickly, but you'll also aid in the growth of those around you by forming the habits of curiosity, clarity, and constant learning.

## Ask Questions
### Why does it matter
SOC work is a mess, you may encounter log entries, notifications, or tools that you don't entirely understand

What distinguishes true analysts from button-pushers is curiosity.

### How to practice
When reviewing logs, pause and ask yourself
- What is this log source?
- What process generated this?
- Is this normal for this user/system?

Dig deeper instead of just closing an alert, ask why it happened, not just what happened

### For Example
You see this log line from an EDR:
<pre>powershell.exe -nop -w hidden -encodedCommand JABX...</pre>
Bad analysts ignore it, curious analysts
- Ask: “Why is PowerShell running encoded commands?”
- Look up: `-nop`, `-w hidden`, `-encodedCommandv`
- Investigate the decoded string
- Research the user and host behavior history

### Tools to assist
- MITRE ATT&CK for technique mapping
- `CyberChef` to decode strings



## Explain Your Process
### Why does it matter
You’ll frequently need to explain what you did — during handoffs, retrospectives, or escalations, being clear = being trusted

### How to practice
- Narrate during investigations on Zoom/Teams.
- Try structured thinking (like `What did I see?`, `What did I check?`, `What did I find?`, `What’s my conclusion?`)

### For Example


### Tools to assist




## Start a Blog
### Why does it matter


### How to practice


### For Example


### Tools to assist



## Learn & Teach
### Why does it matter


### How to practice


### For Example


### Tools to assist



***
<b><i>Want to go back?</b>
</br>
[Click here for the Previous Lab](/courseFiles/Lab_09-documentationAndCaseNotes/documentationAndCaseNotes.md)

<b><i>Looking for a different lab? </b></br>[Back to Lab Directory](/coursenavigation.md)</i>
