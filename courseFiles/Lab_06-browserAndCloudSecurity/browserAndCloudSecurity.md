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
  - 

## Browser Extension Attacks

blah

blah

## OAuth & SSO Attacks
blah

blah

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
