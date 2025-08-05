# Deploying a JS Cloned Website CanaryToken



## Step 1: Create the CanaryToken

Go to:

[https://www.canarytokens.org/nest/](https://www.canarytokens.org/nest/)

Choose **JS Cloned Website**  

![JS Cloned Website](Pasted%20Graphic.png)

Enter a domain of your choosing, and the email and notification method you want to receive.  

![Configure Token](Pasted%20Graphic%201.png)

---

## Step 2: Set Up the Honeypot on MetaCTF Windows + Kali VM

Log into your Kali instance.  

![Log into Kali](Pasted%20Graphic%202.png)

Become root:
```bash
sudo su -
```

Navigate to the honeypot directory:
```bash
cd /opt/owa-honeypot
```
![owa-honeypot directory](425064687-85d0b4c0-b933-459f-8ca6-45ec5687acc6.png)

> **Note:** This directory contains the core components of the OWA honeypot.  
> `owa_pot.py` is the main Flask app that mimics an OWA login page and logs credentials.  
> `dumpass.log` stores login attempts (username, password, IP, and user-agent).  
> `requirements.txt` lists Flask as the only dependency.  
> `templates/` holds the fake login and error HTML pages.  
> `env/` is a virtual environment folder.  
> `instance/` is used by Flask for local configs.  
> `README.md` provides setup and usage details.

## Step 3: Inject the CanaryToken JavaScript

Change into the `templates` directory:
```bash
cd templates
```
![templates folder](Pasted%20Graphic%203.png)

Edit the `outlook_web.html` template using `nano`:
```bash
nano outlook_web.html
```

After the `<head>` tag, add a line with:
```html
<SCRIPT>
```

Then go back to your CanaryToken page and copy the JavaScript snippet.  

![Copy JS snippet](Pasted%20Graphic%204.png)

>[!IMPORTANT]
>
> ⚠️ **Do NOT close the CanaryToken page after copying the JavaScript!**

Paste the script into the `nano` editor.  

![Paste JS into nano](Pasted%20Graphic%205.png)

Then add the closing `</SCRIPT>` tag.  

![Close script tag](Pasted%20Graphic%206.png)

Save the file:

- Press `Ctrl + O`
- Hit `Enter`
- Exit with `Ctrl + X`

Navigate back to the previous directory:
```bash
cd ..
```
![Go back](Pasted%20Graphic%207.png)

Start the honeypot server:  

![Start honeypot](Pasted%20Graphic%208.png)

---

## Step 4: Monitor Token Activity

Return to the CanaryToken page. Scroll down and click on **Manage Canarytoken**. 

![Manage Token](Pasted%20Graphic%209.png)

You should see that the token has **not** yet been triggered. 

![Not triggered yet](Pasted%20Graphic%2010.png)

---

## Step 5: Trigger the Honeypot

Any good hacker will try and test their site.

Back on the Windows system, open a browser and visit the honeypot site.  
![Visit site](Pasted%20Graphic%2011.png)

Return to your CanaryToken management page and refresh it.

Your token should now be triggered!
 
![Token triggered](Pasted%20Graphic%2012.png)  

![Alert](Pasted%20Graphic%2013.png)

***
<b><i>Continuing the course?</b>
</br>
[Click here for the Next Lab](/courseFiles/Lab_08-emailFundamentals/emailFundamentals.md)</i>

<b><i>Want to go back?</b>
</br>
[Click here for the Previous Lab](/courseFiles/Lab_06-browserAndCloudSecurity/browserAndCloudSecurity.md)

<b><i>Looking for a different lab? </b></br>[Back to Lab Directory](/coursenavigation.md)</i>
