### We have **4 routes**:
- ``/`` - Vulnerable login
- ``/secure`` - Secure login
- ``/logs`` - View the lab's access logs
- ``/init`` - Reset DB

### Going into Microsoft Edge you can navigate to to http://10.10.119.212:8000
- You can enter whatever username and password you want and it will fail since there is no instance of that in the DB
<img width="444" height="445" alt="image" src="https://github.com/user-attachments/assets/94f196fc-54e3-4815-98c4-5b4e7d21b6bf" />

- However... If we use ``' OR '1'='1' --`` as our username and whatever password it will bypass any other checks!
<img width="417" height="462" alt="image" src="https://github.com/user-attachments/assets/a5042ca5-e8b3-46b3-a6d9-655df8660c98" />

- We can now see the logs at ``http://10.10.119.212:8000/logs`` as well as the flask logs in the terminal
<img width="1465" height="94" alt="image" src="https://github.com/user-attachments/assets/2703d3b0-704e-4671-b630-9c95b8e3b547" />

<img width="601" height="36" alt="image" src="https://github.com/user-attachments/assets/98b899d5-211d-4b83-8569-c957567b92cc" />

- A SOC analyst seeing this will instantly think of SQLi, let's go review the source code that I have you in the [Part 1](/courseFiles/Section_06-webSecurity/webLabPart1.md)

- In the vulnerable code, this query is sent:

<pre>SELECT * FROM users
WHERE username = '<USER_INPUT>' AND password = '<USER_INPUT>';</pre>

**Why is this bad?**

Because the database doesn’t know where “data” ends and “SQL syntax” begins

If the input contains quotes, operators, or comments, it can change the meaning of the query

A **before** and **after** would look like this for the query

``SELECT * FROM users WHERE username='admin' AND password='secret';`` - **Intended**

``SELECT * FROM users WHERE username='' OR '1'='1' -- ' AND password='';`` - **With Payload**

**Result:** ``WHERE`` clause becomes always true -> first row returned -> login succeeds


