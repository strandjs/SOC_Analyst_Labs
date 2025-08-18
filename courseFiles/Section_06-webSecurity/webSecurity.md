# Web Security
### Overview
Web applications are one of the biggest attack surfaces in any organization

For SOC analysts, understanding web security means knowing how attacks look in logs, alerts, and network traffic

The [OWASP Top 10](https://owasp.org/Top10/) is the industry standard for the most critical risks in web apps

Key aspects
- Most attacks target weak input validation, authentication flaws, and misconfigurations
- SOC analysts must know how these appear in alerts (e.g., WAF blocks, IDS rules, or abnormal log entries)

### Types of Attacks
- **Input Validation Attacks** -> [SQL Injection](https://portswigger.net/web-security/sql-injection), [XSS](https://owasp.org/www-community/attacks/xss/)
- **Authentication/Session Attacks** -> Credential stuffing, session hijacking
- **Access Control Attacks** -> [IDOR](https://portswigger.net/web-security/access-control/idor), privilege escalation
- **Server-Side Attacks** -> [RCE](https://www.imperva.com/learn/application-security/remote-code-execution/), [SSRF](https://portswigger.net/web-security/ssrf), deserialization
- **Client-Side Attacks** -> [XSS](https://owasp.org/www-community/attacks/xss/), [CSRF](https://owasp.org/www-community/attacks/csrf), malicious scripts
