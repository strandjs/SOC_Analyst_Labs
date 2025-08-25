[Part 1](/courseFiles/Section_05-networkingAndTelemetry/rita_lab/ritaLab1.md) [Part 2](/courseFiles/Section_05-networkingAndTelemetry/rita_lab/ritaLab2.md) [Part 3](/courseFiles/Section_05-networkingAndTelemetry/rita_lab/ritaLab3.md) [Part 4](/courseFiles/Section_05-networkingAndTelemetry/rita_lab/ritaLab4.md) [Part 5](/courseFiles/Section_05-networkingAndTelemetry/rita_lab/ritaLab5.md) [Part 6](/courseFiles/Section_05-networkingAndTelemetry/rita_lab/ritaLab6.md) [Part 7](/courseFiles/Section_05-networkingAndTelemetry/rita_lab/ritaLab7.md)



**Dataset:** TeamViewer — Egress via TCP 443


1. Which internal host is flagged Critical for TeamViewer activity in teamviewer_view.csv

**Answer:** 192.168.99.52
 
2. How many connections are recorded for the Critical TeamViewer entry

**Answer:** 51
 
3. How many total kilobytes are reported for the Critical TeamViewer entry

**Answer:** 875.5
 
4. What is the exact Port:Proto:Service string for the Critical TeamViewer entry

**Answer:** 443:tcp:ssl
 
5. RITA also shows a High-severity flow from the same host to a public IP over TeamViewer’s well-known port with a 0% beacon score. What destination IP and port are used in that entry

**Answer:** 52.117.209.74:5938
 
6. How many total megabytes moved over that TeamViewer port (from Q5) in that single entry

**Answer:** 796.2


Continue with [Part 6](/courseFiles/Section_05-networkingAndTelemetry/rita_lab/ritaLab6.md)

---
[Back to the section](/courseFiles/Section_05-networkingAndTelemetry/networkingAndTelemetry.md)
