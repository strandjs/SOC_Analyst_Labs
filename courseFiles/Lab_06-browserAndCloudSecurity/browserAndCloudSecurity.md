# Browser & Cloud Security Fundamentals
### Why Browser and Cloud Security Matters for SOC Analysts
1. **Modern Attack Surfaces**
  - Most enterprise activity now happens in the browser — accessing email, internal apps, collaboration platforms, cloud consoles, etc
  - Cloud platforms (e.g., Microsoft 365, Google Workspace, Azure) have replaced traditional infrastructure for identity, storage, and communication
  - This shift expands the attack surface outside traditional network and endpoint perimeters
2. **Common Trends in Attacks**
  - Phishing and social engineering now often target **OAuth** and **SSO** flows
  - Malware and spyware increasingly propagate through **browser extensions**
  - Cloud-native persistence techniques (e.g., app consent abuse, identity federation attacks) are more common

### Key Concepts for Analysts to Understand
1. **Cloud Identity & Access Management (IAM)**
  - Understand how roles, tokens, and scopes work in platforms like **Azure AD** and **Google IAM**
  - Familiarity with authentication protocols (**OAuth 2.0**, **SAML**, **OpenID** Connect)
2. **Browser Behavior & Risks**
  - Browsers are gateways — they cache tokens, hold session cookies, and run active content (JS, extensions)
  - Extensions can introduce risks similar to traditional malware but are harder to detect and may be user-installed
3. **Logging & Monitoring in the Cloud**
  - In the absence of full endpoint telemetry, logs from Azure and Microsoft 365 are critical to incident detection
  - Analysts must understand how to read, filter, and correlate these logs

### The SOC Analyst's Role in Cloud & Browser Security
1. **Visibility Gaps**
  - You can't defend what you can't see, SOC analysts should advocate for better logging and browser visibility tools
  - Browser-level telemetry often requires special tooling (e.g., Chrome enterprise reporting, Defender for Endpoint)
2. **Threat Hunting & Response**
  - Be proactive in hunting cloud-specific attack patterns
  - Respond quickly to signals from user behavior analytics (e.g., impossible travel, OAuth token replay, suspicious app consent)

## Browser Extension Attacks
# AKA - T1176.001 
[Mitre link](https://attack.mitre.org/techniques/T1176/001/)

"Attackers may abuse internet browser extensions to establish persistent access to victim systems. Browser extensions or plugins are small programs that can add functionality to and customize aspects of internet browsers. They can be installed directly via a local file or custom URL or through a browser's app store - an official online platform where users can browse, install, and manage extensions for a specific web browser. Extensions generally inherit the web browser's permissions previously granted."

# How attackers abuse browser extensions
- Malicious extensions: masquerading as utilities (e.g., ad blockers, PDF tools)
- Legitimate extensions that get hijacked or bought and updated maliciously
- Data exfiltration via background scripts and access to DOM/local storage

# TTPs (Tactics, Techniques, and Procedures)
- Accessing cookies, tokens, sessionStorage, localStorage
- Keylogging via injected scripts
- Redirecting traffic or injecting ads/malware

# Detection tips
- Monitor unusual extension installations via endpoint telemetry
- Watch for abnormal web traffic patterns (e.g., unexpected destinations)
- Use EDR/browser visibility tools (like Chrome Enterprise reports or Microsoft Defender for Endpoint)

<img width="1389" height="469" alt="image" src="https://github.com/user-attachments/assets/3dd81109-d746-4850-bb21-ee1ff95d1589" />
<br><br>

## OAuth & SSO Attacks
## OAuth Attacks
OAuth 2.0 is a protocol that allows third-party applications to request limited access to a user’s cloud data without exposing their password.

OAuth is a commonly used authorization framework that enables websites and web applications to request limited access to a user's account on another application. Crucially, OAuth allows the user to grant this access without exposing their login credentials to the requesting application. This means users can fine-tune which data they want to share rather than having to hand over full control of their account to a third party.

The basic OAuth process is widely used to integrate third-party functionality that requires access to certain data from a user's account. For example, an application might use OAuth to request access to your email contacts list so that it can suggest people to connect with. However, the same mechanism is also used to provide third-party authentication services, allowing users to log in with an account that they have with a different website. 

### Common Attack Vectors
1. Consent Phishing / Illicit Consent Grants
  - Attackers create an app and trick users into granting it permissions (read email, access files)
  - No password stolen, no MFA bypassed — user voluntarily authorizes access
2. Token Theft & Replay
  - Stealing access/refresh tokens from local storage, browser cache, or insecure apps
  - Reuse tokens on attacker-controlled devices without MFA
3. Overprivileged Scopes
  - Apps request more access than they need ("read and write" instead of "read only")
  - Attackers exploit these to elevate access or exfiltrate more data

### Tips for detection and prevention
- Look for unfamiliar app consents in M365 or Google Admin audit logs
- Alert on creation of OAuth apps with elevated scopes
- Use UBA to detect changes in user behavior following OAuth token use
- Restrict app consents (admin consent only or limited scopes)
- Use Conditional Access with app enforcement
- Token binding or short token lifetimes

## SSO (Single Sign-On) Attacks



## Azure Logs
blah

blah

## M365 Audit Logs
blah

blah

***

<b><i>Continuing the course?</b>
</br>
[Click here for the Next Lab](/courseFiles/Lab_07-deceptionSystems/deceptionSystems.md)</i>

<b><i>Want to go back?</b>
</br>
[Click here for the Previous Lab](/courseFiles/Lab_05-networkingAndTelemetry/networkingAndTelemetry.md)

<b><i>Looking for a different lab? </b></br>[Back to Lab Directory](/coursenavigation.md)</i>
