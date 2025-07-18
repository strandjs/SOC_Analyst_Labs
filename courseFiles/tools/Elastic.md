

### Let's go through downloading and installing it
1. **Install Java** - $`sudo dnf install java-21-openjdk -y`
2. **Add Elastic GPG Key and Repo**
- $`sudo rpm --import https://artifacts.elastic.co/GPG-KEY-elasticsearch`
- $<pre>cat <<EOF | sudo tee /etc/yum.repos.d/elastic.repo
[elastic-8.x]
name=Elastic repository for 8.x packages
baseurl=https://artifacts.elastic.co/packages/8.x/yum
gpgcheck=1
gpgkey=https://artifacts.elastic.co/GPG-KEY-elasticsearch
enabled=1
autorefresh=1
type=rpm-md
EOF</pre>
3. **Install Elasticsearch** - $`sudo dnf install elasticsearch -y`
4. **Enable and start elastic** - $`sudo systemctl enable --now elasticsearch`
5. **Install Kibana** - $`sudo dnf install kibana -y`
6. **Enable and start kibana** - $`sudo systemctl enable --now kibana` (Access via browser at: http://localhost:5601)
7. **Install Filebeat (for log forwarding)** - $`sudo dnf install filebeat -y`
8. **Enable and start filebeat** - $`sudo systemctl enable --now filebeat`

