### In this lab we will
- Observe how it captures malicious connection attempts
- View logs and captured malware samples
- Understand its modular architecture

# Let's start

- $`sudo dionaea` - To start it up
<img width="1526" height="472" alt="image" src="https://github.com/user-attachments/assets/2aa46b95-be12-4086-8efd-f4721b27861b" />

<br>

Let's see it's true power, see what ports it is listening on
- $`sudo netstat -tulnp | grep dionaea`

<img width="1023" height="772" alt="image" src="https://github.com/user-attachments/assets/8e01732a-c6d4-4ee9-8fdb-123875bab14f" />

We can see it's listening on lots of ports (FTP, HTTP, SMB, MONGO, MSSQL, SIP, and more)

Let's simulate and FTP bruteforce attack
- $`sudo apt install -y hydra`
- $`curl -LO https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt`
- On another terminal tail the logs $`sudo tail -f /usr/local/var/log/dionaea/dionaea.log`
- $`hydra -l admin -P rockyou.txt localhost ftp -V`
We can see all perspectives, the one of the attacker, it is saying that it found passwords, despite it being false to simulate a vulnerable service
<img width="1141" height="900" alt="image" src="https://github.com/user-attachments/assets/8cfc1445-67d6-456d-ae6b-a2d21ff03c95" />

<br><br>

And the one of the SOC Analyst, where we see the logs and the credentials used
<img width="1849" height="952" alt="image" src="https://github.com/user-attachments/assets/6dfa629a-207e-4927-a948-3dd2cab8621b" />




