### Now that we have set up **Elastic**, **Kibana** and **Filebeat**, we can finally get our hands dirty and learn how a SOC analysts deals with logs in Elastic

## GOAL
- Set up and use Elastic SIEM on your system
- Learn how to ingest logs and visualize them
- Learn how to use SIEM (Hosts, Users, Alerts)
- Learn how to create basic detection rules

1. Head over to Analytics -> Discover and see your logs flowing from filebeat

- On the left side you can see, add, or remove data fields and data views ↓↓↓

<img width="322" height="953" alt="image" src="https://github.com/user-attachments/assets/79b057a4-2d9d-4fff-be15-c6a494802ce4" />

- On the middle and right side you will see the logs flowing in, you can explore them and try to make out where each one came from, you can also search and sort them ↓↓↓

<img width="1589" height="680" alt="image" src="https://github.com/user-attachments/assets/95da8151-bb72-478c-811e-50ca8d18de50" />

- On the upper side you can see the traffic density on a specific timeling and a way to filter your logs, say you want to only see the logs coming from syslog, you would want to filter like this `event.dataset: "system.syslog"` since we are using filebeat, it's really easy and intuitive to make whatever filters you want ↓↓↓

<img width="1594" height="267" alt="image" src="https://github.com/user-attachments/assets/02cab47d-9b34-4af7-b4b5-19423754ca74" />
<br><br>

2. Now go to Security -> Explore, here we can see

- **Hosts** - Check user logins, uptime, etc.
- **Users** - Auth activity
- **Network** - IP traffic

<img width="1290" height="892" alt="image" src="https://github.com/user-attachments/assets/5ca936bd-6e06-46d7-921c-889d3b75e6d1" />

For now head over to **Users** 

Run &`sudo -k && sudo ls` on your system and enter wrong password and see it appear on elastic after you refresh, you should see something like this

<img width="1309" height="89" alt="image" src="https://github.com/user-attachments/assets/91f012e0-1a02-406f-802c-9c4c0b867f76" />


If nothing happens restart filebeat and try again $`sudo systemctl restart filebeat`

3. Create a Basic Detection Rule
- Click on Security -> Rules -> Detection Rules
<img width="1918" height="943" alt="image" src="https://github.com/user-attachments/assets/f0907037-a1a1-49fc-a06b-74057038b98a" />

- Create new rule -> **Select** Custom Query
- Index patterns: `filebeat-*`
- Custom query: `message:*root* AND message:*session opened* AND event.dataset:system.auth` - Continue
- Name: `Root Shell Activity Detected`
- Description: `My first rule`
- Default Severity: `Medium`
- Default risk score: `50` - Continue
- Runs every: `1 Minutes` - Continue -> Create & enable rule
<br><br>

Now if you go over to alerts you can see your Rule's work!
<img width="1918" height="943" alt="image" src="https://github.com/user-attachments/assets/a4ef29c3-c888-464f-baa7-231fb828b0af" />
<br><br>

4. Let's now try to **Investigate Alerts with Timelines**
- Go to Security -> Alerts
- Click an alert from your detection rule (e.g. Root Shell Detected)
- Click “Investigate in timeline” (second button)
 <img width="158" height="32" alt="image" src="https://github.com/user-attachments/assets/5e9cb2c4-9505-495b-961b-71158b101e5f" />

###You can:
- See logs from before and after the alert
- Use the filter bar to expand your view (e.g. user.name:root)
- Drag in fields like event.dataset, message, host.name
- Click the 💾 Save icon to save it
<img width="1918" height="943" alt="image" src="https://github.com/user-attachments/assets/a6cf43b8-dd9b-4506-9d9e-74a72fb0bdfd" />
<br><br>

## Try to add more rules by yourself or even simulate attacks to better understand the perspectives of both an attacker and a SOC analyst 








