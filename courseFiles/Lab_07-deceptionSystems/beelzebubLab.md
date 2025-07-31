Beelzebub is an advanced honeypot framework designed to provide a highly secure environment for detecting and analyzing cyber attacks. It offers a low code approach for easy implementation and uses AI to mimic the behavior of a high-interaction honeypot

You can find the original GitHub of at [Beelzebub Repo](https://github.com/mariocandela/beelzebub)

# Setup
Participants will deploy and monitor an AI-powered SSH honeypot (Beelzebub) to detect and analyze attacker behavior in real time

- $`sudo su -`
- $`apt update && apt upgrade -y`
- $`systemctl enable --now docker`
- $`cd /opt`
- $`git clone https://github.com/mariocandela/beelzebub.git`

### Get the ChatGPT Api Key
- Go to [ChatGPT](https://chatgpt.com/) and create an account if you don’t have one
- Make sure you have credits or a payment method at [Billing Setting](https://platform.openai.com/settings/organization/billing/overview)
- Go to [API Keys](https://platform.openai.com/api-keys) and create a new key
- Save this key as you will only see it once!

### Deployment
- Make sure you are into **/opt/beelzebub/**
- $`nano docker-compose.yml` - Put your key here
<img width="446" height="71" alt="image" src="https://github.com/user-attachments/assets/5f407ef9-759e-4eec-8d97-98ef396dc30d" />

- Comment the **Default SSH Mapping**(ssh 22 port)
<img width="202" height="84" alt="image" src="https://github.com/user-attachments/assets/4375696b-89c3-45a6-afd9-d2f5a549168e" />



