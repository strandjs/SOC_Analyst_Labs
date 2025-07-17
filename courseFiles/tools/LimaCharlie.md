LimaCharlie is a cloud-native cybersecurity operations platform that provides capabilities like EDR, telemetry, detection engineering, and automation in a scalable, API-first model. It is designed for modern SOCs that want agility, transparency, and the ability to engineer their security stack like software.

### Why we use it
- Real-time visibility into endpoints and activities
- Rapid detection and response capabilities
- Built-in automation for triage and investigation
- Detection-as-code simplifies rule management and collaboration

### What can it do
- Telemetry collection (process, file, network, registry, etc)
- Threat detection via customizable rules
- Remote incident response (kill processes, collect memory, isolate hosts)
- Integration with other tools (SIEMs, SOARs, Slack, AWS, etc)

### Architecture
Sensors and Endpoints
- LimaCharlie uses lightweight endpoint sensors compatible with Windows, macOS, and Linux
- Sensors transmit detailed telemetry back to the cloud

Cloud-Based Backend
- Centralized data processing, detection engine, and storage
- Analysts interact via the LimaCharlie web interface, CLI, or APIs

Integration Points
- SIEM
- SOAR
- Webhooks, Slack, email, and more

<img width="1911" height="324" alt="image" src="https://github.com/user-attachments/assets/92ba514e-3a84-453d-b02b-c6c7da735859" />

