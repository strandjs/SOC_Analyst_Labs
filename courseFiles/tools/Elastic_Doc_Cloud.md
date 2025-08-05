Elasticsearch is a distributed search and analytics engine, scalable data store, and vector database built on Apache Lucene. It’s optimized for speed and relevance on production-scale workloads. Use Elasticsearch to search, index, store, and analyze data of all shapes and sizes in near real time. Kibana is the graphical user interface for Elasticsearch. It’s a powerful tool for visualizing and analyzing your data, and for managing and monitoring the Elastic Stack.

Elasticsearch is the heart of the Elastic Stack. Combined with Kibana, it powers these Elastic solutions and use cases:
- **Elasticsearch** - Build powerful search and RAG applications using Elasticsearch's vector database, AI toolkit, and advanced retrieval capabilities
- **Observability** - Resolve problems with open, flexible, and unified observability powered by advanced machine learning and analytics
- **Security** - Detect, investigate, and respond to threats with AI-driven security analytics to protect your organization at scale

### Let's go through setting it all up
1. **Make an account** - [Here](https://cloud.elastic.co/registration?fromURI=%2Fhome) , You can start a free trial for 14 days to experiment and learn this tool, you also don't need a credit card to get started

<img width="882" height="589" alt="image" src="https://github.com/user-attachments/assets/8592f4aa-8211-40d3-945e-08fd93883d6f" />

2. Insert your name and you can leave a `-` in the Company field

<img width="497" height="417" alt="image" src="https://github.com/user-attachments/assets/fb524685-bdf0-4d1e-9795-b20f46e51cac" />

3. Select **I am new to Elastic**

<img width="497" height="417" alt="image" src="https://github.com/user-attachments/assets/cab56c51-285e-491a-bb96-363aa51bd295" />

4. Select **Considering Elastic Cloud subscription for production / proof of concept**

<img width="536" height="457" alt="image" src="https://github.com/user-attachments/assets/8779f808-0a4e-4041-96ee-bf103f618fa8" />

5. 3


6. Download Sysmon from [Microsoft Sysinternals](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon) and extract it into downloads

<img width="1129" height="635" alt="image" src="https://github.com/user-attachments/assets/5718f61f-1d01-4557-ad0a-1f7904ce2803" />


3. **In powershell run** - $`cd C:\Users\Administrator\Downloads\Sysmon\` + $`.\Sysmon64.exe -accepteula -i`
4. To set up the Elastic Agent on the machine go to **Management -> Integrations**

<img width="251" height="236" alt="image" src="https://github.com/user-attachments/assets/5f43c7de-7dbc-4119-b428-07ba5cbea1f0" />

5. Search for **Windows** and select **Custom Windows Event Logs**

<img width="1673" height="1005" alt="image" src="https://github.com/user-attachments/assets/a8e15d44-1731-472d-a5ca-be4929f045de" />

6. Now click on **Add Custom Windows Event Logs**

<img width="1386" height="542" alt="image" src="https://github.com/user-attachments/assets/3f04a237-1072-4123-89ba-2e2465a2aec6" />

7. Now press on the **Install Elastic Agent** on the popup in the lower middle part of the screen

<img width="819" height="73" alt="image" src="https://github.com/user-attachments/assets/3ff9ff70-0009-4735-b3e0-fe737e046774" />

8. Select **Windows** and run that command in powershell to install the agent, then go back in the browser

<img width="1162" height="1006" alt="image" src="https://github.com/user-attachments/assets/74810255-b48a-4487-b1dc-9cbf4767af2f" />

9. Do as in the image below

<img width="1162" height="1006" alt="image" src="https://github.com/user-attachments/assets/39739bbd-ba30-4ed5-8280-cfcd201fa173" />

10. Click **Confirm incoming data**, you should see a preview of incoming data

<img width="1162" height="1006" alt="image" src="https://github.com/user-attachments/assets/ccbc1101-4749-496b-8604-046dc8664a26" />

<br><br>

## That's it!

As a continuation, take onto the hands-on lab for [Elastic](/courseFiles/Lab_02-toolsAndPlatforms/elasticLabCloud.md)



