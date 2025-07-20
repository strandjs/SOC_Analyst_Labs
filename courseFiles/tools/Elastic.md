Elasticsearch is a distributed search and analytics engine, scalable data store, and vector database built on Apache Lucene. It’s optimized for speed and relevance on production-scale workloads. Use Elasticsearch to search, index, store, and analyze data of all shapes and sizes in near real time. Kibana is the graphical user interface for Elasticsearch. It’s a powerful tool for visualizing and analyzing your data, and for managing and monitoring the Elastic Stack.

Elasticsearch is the heart of the Elastic Stack. Combined with Kibana, it powers these Elastic solutions and use cases:
- **Elasticsearch** - Build powerful search and RAG applications using Elasticsearch's vector database, AI toolkit, and advanced retrieval capabilities
- **Observability** - Resolve problems with open, flexible, and unified observability powered by advanced machine learning and analytics
- **Security** - Detect, investigate, and respond to threats with AI-driven security analytics to protect your organization at scale

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

<br><br>
9. **Configuring**

- $`sudo /usr/share/elasticsearch/bin/elasticsearch-reset-password -u elastic` - get password for **elastic**, make sure to save it
- $`sudo /usr/share/elasticsearch/bin/elasticsearch-reset-password -u kibana_system` - get password for **kibana**, make sure to save it as well
- $`sudo nano /etc/elasticsearch/elasticsearch.yml` - make sure this line is present and not commented: `xpack.security.enabled: true` and `xpack.security.enrollment.enabled: true`
- $`sudo systemctl restart elasticsearch`
- $`sudo nano /etc/kibana/kibana.yml` - make sure these line are present:

<pre>elasticsearch.hosts: ['https://localhost:9200']
logging.appenders.file.type: file
logging.appenders.file.fileName: /var/log/kibana/kibana.log
logging.appenders.file.layout.type: json
logging.root.appenders: [default, file]
pid.file: /run/kibana/kibana.pid
elasticsearch.username: kibana_system
elasticsearch.password: "thePasswordForKibana(should already be filled automatically)"
elasticsearch.ssl.certificateAuthorities: [/var/lib/kibana/ca_1753032225222.crt]
xpack.fleet.outputs: [{id: fleet-default-output, name: default, is_default: true, is_default_monitoring: true, type: elasticsearch, hosts: ['https://localhost:9200'], ca_trusted_fingerprint: 9749ae879836f843f9cf>
xpack.encryptedSavedObjects.encryptionKey: "whatever32characterKeyYouWant"
</pre>

- $`sudo systemctl restart kibana` 
- $`sudo nano /etc/filebeat/filebeat.yml` - make sure you have these:

<pre>output.elasticsearch:
  hosts: ["https://localhost:9200"]
  username: "elastic"
  password: "your_elastic_password_here"
  ssl.certificate_authorities: ["/etc/elasticsearch/certs/http_ca.crt"]  # path to your CA cert
</pre>
<pre>setup.kibana:
  host: "http://localhost:5601"
  ssl.certificate_authorities: ["/etc/elasticsearch/certs/http_ca.crt"]
</pre>
- $`sudo find / -name "http_ca.crt" 2>/dev/null` (just in case you don't find your certificate)
- $`sudo filebeat setup`
- $`sudo systemctl restart filebeat`

### If filebeat doesn't send the logs over or errors because of system do this, else skip to next step
- $`sudo filebeat modules enable system`
- $`sudo nano /etc/filebeat/modules.d/system.yml` - make sure you have something like this:

<pre>
module: system
  syslog:
    enabled: true
  auth:
    enabled: true</pre>

- $`sudo systemctl restart filebeat` & verify $`sudo systemctl status filebeat`

## Let's finally open Kibana at <pre>http://localhost:5601</pre>
<img width="489" height="688" alt="image" src="https://github.com/user-attachments/assets/58a0ecf5-f920-497d-be13-f9456e9eef4b" />

- Let's choose `Explore on my own` and `Configure Manually`
- Let's login to **kibana**, user: `kibana_system` , pass: `<your_saved_password>`
<img width="604" height="903" alt="image" src="https://github.com/user-attachments/assets/eb7266d9-cd80-4d4b-8615-696fc4c5613d" />
<br><br>

- Now for the verification code use: $`sudo journalctl -u kibana | grep verification` and get it from there
<img width="624" height="402" alt="image" src="https://github.com/user-attachments/assets/08b55d8d-e10c-4656-85a6-8670b1161ef7" />
<br><br>

- Sign in into elastic and that's it! user: `elastic` , pass: `<your_saved_password>`
<img width="473" height="509" alt="image" src="https://github.com/user-attachments/assets/69809bd7-4de6-4682-b8c3-c93b653235f8" />

- As a continuation, take onto the hands-on lab for [Elastic](/courseFiles/Lab_02-toolsAndPlatforms/elasticLab.md)



