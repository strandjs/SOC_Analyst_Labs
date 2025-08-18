#  Lab Solution: Phishing Email Investigation – Header & Link Analysis

## Step-by-Step Answer Key

---

###  Step 1: Email Header Analysis

**Extracted Fields:**

- **From:** `CEO Mark <smtpfox-wu6ea@shrrutitapuria.com>`
- **Return-Path:** `<reply@paymemt-secure.com>`
- **Reply-To:** `reply@paymemt-secure.com`
- **Authentication-Results:**
  - `spf=fail` (domain does not designate permitted sender)
  - `dkim=fail`
  - `dmarc=fail`

**Sublime Analyzer results:**

![result Sublime Analyzer](https://i.ibb.co/DHDvMnc4/image.png)

>[!IMPORTANT]
>
>Sublime Analyzer detects the mail as malicious

![result Sublime Analyzer 2](https://i.ibb.co/LD8MrHWK/image.png)

![result Sublime Analyzer 3](https://i.ibb.co/LDWtWQCQ/image.png)

>[!IMPORTANT]
>
>Here are additional indicators that suggest this is a phishing email.

**Answers:**

1. ❌ The domain `shrrutitapuria.com` is unrelated to the company and suspicious.
2. ❌ The display name is “CEO Mark” but the email address clearly does not match a company domain.
3. ❌ SPF/DKIM/DMARC all failed → strong indicator of spoofing.
4. ✅ Yes, this is a spoofing attempt.

---

###  Step 2: Embedded Link Analysis

**Extracted URL:**

```
http://evri.trackszc.live
```

**Tool-based Results:**

- **VirusTotal:** Detected as phishing or suspicious by multiple engines.
- **PhishTank:** May appear as a reported phishing domain (check current status).
- **URLScan.io:** \`Reveals Google Safe Browsing\` sees it as \*\*Malicious\*\*

**Answers:**

1. ❌ The domain is unknown and not part of any official business infrastructure.

2. ✅ Use of `.live` TLD + suspicious path + urgency = classic phishing indicators.


**Tools results:**

- VirusTotal

![VirusTotal result](https://i.ibb.co/ksGHfxqW/Screenshot-2025-07-28-190557.png)

>VirusTotal detects the link as a phishing site.

- PhishTank

![PhishTank result](https://i.ibb.co/DDtNrsZH/image.png)

>PhishTank also detects the link as a phishing site.

- URLScan.io

![URLScan.io](https://i.ibb.co/1GHtjtGn/image.png)

>URLScan.io reports that the Google Safe Browsing result is `Malicious`.



---

###  Step 3: Social Engineering Tactics

**Message Text:**

```
Hello John,

Please process the attached invoice urgently. We are closing the deal by EOD.

You can also view the payment instructions here:
http://evri.trackszc.live

Thanks,
John
CEO
```

**Answers:**

1. **Urgency** is created by mentioning “EOD” and immediate action.
2. **Authority** is impersonated by posing as the CEO.
3. The message is short, vague, and lacks specifics (no invoice number, no context).


---

### Step 4: Sample Incident Report

| Field                                | Your Findings                                                                |
| ------------------------------------ | ---------------------------------------------------------------------------- |
| **Email Subject**                    | [URGENT] Invoice Payment Required Today                                      |
| **From Address**                     | [smtpfox-wu6ea@shrrutitapuria.com](mailto\:smtpfox-wu6ea@shrrutitapuria.com) |
| **Reply-To**                         | [reply@paymemt-secure.com](mailto\:reply@paymemt-secure.com)                 |
| **SPF/DKIM/DMARC Pass?**             | No – all failed                                                              |
| **Suspicious Link?**                 | Yes – domain is suspicious, phishing flagged on VirusTotal                   |
| **Indicators of Phishing?**          | Spoofed address, failed auth, urgency,  vague language                       |
| **Severity Level (Low/Medium/High)** | High – realistic spoof + phishing link + impersonation                       |
| **Recommended Action**               | Block domain, alert users, report to CERT, blacklist link                    |

---
[Back to the Section](/courseFiles/Section_08-emailFundamentals/emailFundamentals.md)
