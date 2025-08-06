# Setup

- First things first, create an account here: https://azure.microsoft.com/en-us/pricing/free-services
- And get your sample logs from here: https://github.com/sbousseaden/EVTX-ATTACK-SAMPLES/blob/master/evtx_data.csv
- Search for "Log Analytics workspaces" and click `+ Create`
<img width="521" height="160" alt="image" src="https://github.com/user-attachments/assets/c3024add-1731-4f92-a65e-e43520750407" />

- Fill in:
1. Subscription
2. Resource Group(make a new one if you don't have one already)
3. Workspace Name (e.g., LogAnalysisLab)
4. Region (any nearby)
<img width="767" height="679" alt="image" src="https://github.com/user-attachments/assets/b978b97d-9ecf-4daf-8ddb-2ee2cfc1f3c7" />

- Hit `Review + Create` -> Create
- In the Azure Portal, search: `Azure Data Explorer Clusters` → `+ Create`
<img width="521" height="164" alt="image" src="https://github.com/user-attachments/assets/2ad46621-93a6-485d-a1f3-3f5da14b8d6a" />
<img width="762" height="808" alt="image" src="https://github.com/user-attachments/assets/f60e29b9-9b6b-4fca-b5aa-39cec4b248bf" />

- After it's deployed, click `Go to Resource`
- Inside it, create a Database (e.g., LogTrainingDB)
- Now going back to the **Cluster**

<img width="1270" height="632" alt="image" src="https://github.com/user-attachments/assets/81211f74-d8f6-4518-8279-c35b555d2646" />

- Go to **Overview** and copy your **Cluster URL**

<img width="541" height="32" alt="image" src="https://github.com/user-attachments/assets/8c1fd1f5-1fa9-45f9-82df-124e244c1b12" />

- Go to https://dataexplorer.azure.com and log in with you Azure account
- On top right click on your Profile Icon -> Change Directory

<img width="413" height="136" alt="image" src="https://github.com/user-attachments/assets/f8e0b4e7-fe56-4ae7-9226-03d7e235d6ad" />

- Select the one with `@outlook.onmicrosoft.com`
- On the left, select your **Dashboards** -> **Create new dashboard**
- Click **Add tile** -> **+ Data source**, add whatever name and your cluster URL that you copied earlier -> **Connect** -> choose your database -> **Create**
- Now go back again to your **Cluster Overview** on the azure portal and click on **Ingest data**

<img width="698" height="365" alt="image" src="https://github.com/user-attachments/assets/8c46c611-cab3-483e-af26-92a1d15dad72" />

- Add a new table and upload your logs -> **Next** -> **Finish** -> Wait for it to ingest then **Close**

<img width="1762" height="940" alt="image" src="https://github.com/user-attachments/assets/353a32f1-070c-4a85-8766-a21d0442583c" />

# Now you can FINALLY run queries! 
### My table name is "LabLogs", in the queries replace it with whatever you named it
- Let's see the first 100 logs

<pre>LabLogs
| take 100</pre>

<img width="1597" height="549" alt="image" src="https://github.com/user-attachments/assets/3dd7ac12-ac35-47b5-bb62-bf1b490d336c" />

- We can see on **Column 6** it's the EVTX Tactic, let's group the logs by it

<pre>LabLogs
| summarize Count = count() by Column6</pre>

<img width="420" height="270" alt="image" src="https://github.com/user-attachments/assets/8a40c440-b0a3-4506-9f4f-4fa2a0b37a68" />

- Also grouping them by column5(AKA EVTX_FileName) or column4(Computer) gives pretty interesting results
- Now that we know what is what, let's group **Lateral Movement** and **Privilege Escalation** by computer

<pre>LabLogs
| where Column6 in ("Lateral Movement", "Privilege Escalation")
| summarize Count = count() by Column4 // Computer</pre>

<img width="420" height="391" alt="image" src="https://github.com/user-attachments/assets/54637b21-69c9-4529-a408-45d099898f6e" />

- Now let's see the "noisiest" systems, ideal to demonstrate triage

<pre>LabLogs
| where Column6 != "EVTX_Tactic"
| summarize Count = count() by Computer = Column4
| top 10 by Count desc</pre>

<img width="333" height="292" alt="image" src="https://github.com/user-attachments/assets/58c7d10b-94e0-46a3-bfd5-9fd5f782b781" />

- You can also corellate the tactics to hosts

<pre>LabLogs
| where Column6 != "EVTX_Tactic"
| summarize Count = count() by Tactic = Column6, Host = Column4
| sort by Count desc</pre>

<img width="459" height="804" alt="image" src="https://github.com/user-attachments/assets/8cd45f1c-6a82-43f1-83c0-8006e966275e" />

## Now try to see what each of those queries do, and try to create some yourself now that you've got everything setup

<pre>LabLogs
| where Column6 != "EVTX_Tactic"
| extend Timestamp = todatetime(Column1)  // adjust to actual time column
| summarize Count = count() by bin(Timestamp, 1h), Tactic = Column6
| sort by Timestamp asc</pre>

<pre>LabLogs
| summarize Count = count() by File = Column5
| top 10 by Count desc
</pre>

<pre>LabLogs
| where Column6 in ("Persistence", "Privilege Escalation", "Credential Access")
| summarize Count = count() by Tactic = Column6, Computer = Column4</pre>


---
[Back to the Lab](/courseFiles/Lab_06-browserAndCloudSecurity/browserAndCloudSecurity.md)



