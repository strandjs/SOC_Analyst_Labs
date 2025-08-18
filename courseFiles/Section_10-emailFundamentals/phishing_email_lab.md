## ⚠️ WARNING: This Lab Contains a Real Phishing Link

>[!WARNING]
>
> **Do NOT click** the link in the provided `.eml` file directly from a browser or email client. Always analyze it in a safe, controlled environment using tools like VirusTotal, URLScan, or PhishTank. This lab is for educational purposes only.

---

## Lab: Phishing Email Investigation – Header & Link Analysis


### Objective:

Simulate the role of a SOC Analyst investigating a **suspicious email report** from a user. You'll analyze the email's **headers**, **sender identity**, and **embedded link** to determine if it's malicious.

---

### Scenario:

> A user from the finance department reports receiving a suspicious email that appears to come from the company’s CEO. It includes an urgent payment request and a PDF invoice, along with a link to view payment instructions.

---

###  Materials:

-  [fake_ceo_request.eml](./fake_ceo_request.eml)
- Tools: Any of the following:
  - Python script (from your course)
  - [Sublime Analyzer](https://analyzer.sublime.security/)
  - Any other personal or public scripts/services
---

###  Instructions

#### Step 1: Open and Inspect the Email Header

Extract and interpret these fields:

- `From`
- `Return-Path`
- `Reply-To`
- `Authentication-Results` (SPF/DKIM/DMARC)



**Questions:**

1. Is the sender’s domain legitimate?
2. Does the display name match the domain?
3. What do SPF/DKIM/DMARC results say?
4. Is this a spoofing attempt?

####  Step 2: Analyze the Embedded Link

Extract the following URL from the message body:

```
http://evri.trackszc.live
```

**⚠️ WARNING: This is a real phishing domain. Do NOT click it. Use the tools below in isolated, analysis-only mode.**

**Instructions:** Use these tools to analyze the link:

- [URLScan.io](https://urlscan.io/)
- [VirusTotal](https://virustotal.com/)
- [PhishTank](https://www.phishtank.com/)





**Questions:**

1. What is the domain reputation?

2. What indicators suggest it may be phishing?

#### Step 3: Analyze the Social Engineering Tactics

Review the message content:

```
Hello John,

Please process the attached invoice urgently. We are closing the deal by EOD.

You can also view the payment instructions here:
http://evri.trackszc.live

Thanks,
John
CEO
```

**Questions:**

1. What psychological techniques are used (urgency, authority)?
2. Does the writing style match your CEO?
3. Is the message vague or overly generic?

####  Step 4: Write an Incident Summary

Fill out this incident response template:

| Field                                | Your Findings                                  |
| ------------------------------------ | ---------------------------------------------- |
| **Email Subject**                    |                                                |
| **From Address**                     |                                                |
| **Reply-To**                         |                                                |
| **SPF/DKIM/DMARC Pass?**             |                                                |
| **Suspicious Link?**                 |                                                |
| **Indicators of Phishing?**          |                                                |
| **Severity Level (Low/Medium/High)** |                                                |
| **Recommended Action**               | (e.g. block domain, warn user, report to CERT) |


---

Once you finish, go check out the [solution](./phishing_email_lab_solution.md).

---
[Back to the Section](/courseFiles/Section_08-emailFundamentals/emailFundamentals.md)
