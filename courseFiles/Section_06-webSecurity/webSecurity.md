# Web Security
## Overview
Web applications are one of the biggest attack surfaces in any organization

For SOC analysts, understanding web security means knowing how attacks look in logs, alerts, and network traffic

The [OWASP Top 10](https://owasp.org/Top10/) is the industry standard for the most critical risks in web apps

Key aspects
- Most attacks target weak input validation, authentication flaws, and misconfigurations
- SOC analysts must know how these appear in alerts (e.g., WAF blocks, IDS rules, or abnormal log entries)

## Types of Attacks
- **Input Validation Attacks** -> [SQL Injection](https://owasp.org/www-community/attacks/SQL_Injection), [XSS](https://owasp.org/www-community/attacks/xss/)
- **Authentication/Session Attacks** -> Credential stuffing, session hijacking
- **Access Control Attacks** -> [IDOR](https://portswigger.net/web-security/access-control/idor), privilege escalation
- **Server-Side Attacks** -> [RCE](https://owasp.org/www-community/vulnerabilities/Deserialization_of_untrusted_data), [SSRF](https://owasp.org/www-community/attacks/Server_Side_Request_Forgery), deserialization
- **Client-Side Attacks** -> [XSS](https://owasp.org/www-community/attacks/xss/), [CSRF](https://owasp.org/www-community/attacks/csrf), malicious scripts

## Common Web Attacks
1. **SQL Injection (SQLi)**

**What it is:** Attacker injects malicious SQL into queries to read/modify DB data

**Example:** ``OR '1'='1' --`` in login fields

**Impact:** Credential theft, DB dumps, account takeover

**Detection:**
<pre>Web server logs with suspicious strings (' OR 1=1, UNION SELECT, --)

WAF/IDS alerts (rules for sqlmap user-agent)

Prevention: Use parameterized queries, ORM, and DB least privilege</pre>

### Try this SQL Injection [Hands-on Lab](/courseFiles/Section_06-webSecurity/webLabPart1.md)

---

2. **Cross-Site Scripting (XSS)**

**What it is:** Attacker injects JavaScript into a web page, which runs in the victim’s browser

**Types:** Reflected (in URL), Stored (in DB), DOM-based

**Impact:** Session hijacking, credential theft, phishing

**Detection:**
<pre>Logs with <script>, onerror=, alert(1)

Multiple failed WAF blocks from same IP

Prevention: Output encoding, Content Security Policy (CSP)</pre>

---

3. **Cross-Site Request Forgery (CSRF)**

**What it is:** Attacker tricks victim’s browser into sending malicious requests while logged in

**Impact:** Funds transfer, account modifications

**Detection:** 
<pre>Harder for SOC — look for unusual actions from same session cookie but different IP

Prevention: Anti-CSRF tokens, SameSite cookies</pre>

---

4. **Authentication & Session Attacks**

**Examples:**
- Brute force/credential stuffing
- Session fixation
- Weak password resets

**Detection:**
<pre>Repeated failed logins from same IP

Impossible travel logins

Session reuse from multiple IPs</pre>

[Owasp Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)

---

5. **File Upload Vulnerabilities**

**What it is:** Attacker uploads malicious files (e.g., .php shell disguised as .jpg)

**Impact:** Remote code execution, malware hosting

**Detection:**
<pre>Web logs with suspicious uploads (.php, .jsp, .exe)

Antivirus alerts on uploaded files</pre>

**Prevention:** File type validation, AV scanning, store files outside webroot

[Owasp File Upload Risks](https://owasp.org/www-community/vulnerabilities/Unrestricted_File_Upload)

---

6. **Insecure Direct Object References (IDOR)**

**What it is:** Accessing data by modifying IDs in URLs (/user?id=123 → /user?id=124).

**Impact:** Unauthorized data exposure.

**Detection:** 
<pre>Log anomalies (same user accessing multiple IDs quickly)</pre>

**Prevention:** Enforce access controls at server side.

---

7. **Remote Code Execution (RCE) & Deserialization**

**RCE:** Attacker executes arbitrary commands on server

**Deserialization attacks:** Exploiting unsafe object parsing

**Impact:** Full system takeover (Log4Shell example)

**Detection:** 
<pre>Logs with suspicious process executions, unusual outbound connections</pre>

**Prevention:** Input sanitization, safe libraries, timely patching

---

8. **Server-Side Request Forgery (SSRF)**

**What it is:** Attacker makes server send requests to internal/external systems

**Impact:** Data theft (e.g., AWS metadata service)

**Detection:** 
<pre>Logs with unusual internal IP requests (e.g., 169.254.169.254)</pre>

**Prevention:** Network segmentation, allowlists(never rely only on denylists)

## Browser malware
Check it out and do the lab for it [Here](/courseFiles/Section_06-webSecurity/browser_malware.md)


***

<b><i>Continuing the course?</b>
</br>
[Click here for the Next Section](/courseFiles/Section_07-browserAndCloudSecurity/browserAndCloudSecurity.md)</i>

<b><i>Want to go back?</b>
</br>
[Click here for the Previous Section](/courseFiles/Section_05-networkingAndTelemetry/networkingAndTelemetry.md)

<b><i>Looking for a different Section? </b></br>[Back to Section Directory](/coursenavigation.md)</i>
