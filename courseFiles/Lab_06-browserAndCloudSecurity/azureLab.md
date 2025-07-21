# Setup

- First things first, create an account here: https://azure.microsoft.com/en-us/pricing/free-services
- And get your sample logs from here: https://github.com/Azure/Azure-Sentinel/blob/master/Sample%20Data/SecurityEvent/SecurityEvent-WindowsFileAuditing-4663.csv
- Or use $`wget https://github.com/Azure/Azure-Sentinel/blob/master/Sample%20Data/SecurityEvent/SecurityEvent-WindowsFileAuditing-4663.csv`
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
- Go to https://dataexplorer.azure.com and log in with you Azure account
- On the left, select your cluster + database
- Click “Ingest data” > Choose CSV file
- Upload our logs
- Choose a table name (e.g., SecurityEvents4663)



# Let's start
### Scenario: A finance folder has sensitive spreadsheets. You suspect unauthorized access
### Goal: Analyze file access patterns, identify anomalies (e.g., non-HR users accessing HR files)
