

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
4. **Enable and start the service** - $`sudo systemctl enable --now elasticsearch`
