# Documentation & Case Notes
Why does it matter
- **Auditability** – Incident records must be reproducible for compliance (e.g., ISO 27001, SOC 2)
- **Operational Continuity** – Night shift picks up where day shift left off
- **Evidence Trail** – Case notes may be used in legal proceedings or HR actions
- **Knowledge Base** – Patterns emerge from well-documented incidents, improving detection

Documentation types
| Type  | Purpose | Example |
| ------------- | ------------- | ------------ |
| Case Notes  | Running log of your findings/actions  | Notes in your SOAR tool |
| Incident Timeline  | 	Chronological record  | Used in after-action reports |
| Alert Triage Summary | Final write-up after triage | SOC ticket or escalation |
| Investigation Report | Full postmortem | Often created by Tier 2+ |

Bad Documentation Causes
- Missed hand-offs
- Incorrect escalation
- Slower containment
- Incomplete RCA (Root Cause Analysis)

## Case Notes - The Analyst’s Daily Log
Key Rules
1. **Start Immediately** – Begin documenting as soon as the alert is opened
2. **Be Objective** – Focus on what you observed, not assumptions
3. **Timestamp Everything** – Use UTC and standard formats (e.g., YYYY-MM-DD HH:MM UTC)
4. **Log Every Step** – Even “negative” findings (what you checked and ruled out)

Case Notes Structure
<pre>[2025-07-25 10:22 UTC] Alert triggered: Suspicious PowerShell execution on host WKS-204
[2025-07-25 10:24 UTC] Queried EDR logs – script matches encoded PowerShell from MITRE T1059.001
[2025-07-25 10:28 UTC] Queried Sysmon – found parent process was MS Word; likely macro
[2025-07-25 10:32 UTC] Informed Tier 2. Awaiting sandbox results</pre>

Tip - Always write as if someone unfamiliar with the case will read it next

## Writing an Incident Timeline
Purpose
- Summarizes all events in time order
- Required for formal reporting (incident response, regulatory)

## Writing an Alert Triage Summary

blah

blah

## Real-World Examples

blah

blah

***
<b><i>Continuing the course?</b>
</br>
[Click here for the Next Lab](/courseFiles/Lab_10-softSkills/softSkills.md)</i>

<b><i>Want to go back?</b>
</br>
[Click here for the Previous Lab](/courseFiles/Lab_08-emailFundamentals/emailFundamentals.md)

<b><i>Looking for a different lab? </b></br>[Back to Lab Directory](/coursenavigation.md)</i>
