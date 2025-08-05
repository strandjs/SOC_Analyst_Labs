# Lab: LDAP Traffic Analysis Solution

**PCAP File:** `dns.pcap` // [click me for pcap file](./dns.pcap)

---

## Lab Instructions

This guide walks you through analyzing LDAP traffic step by step. You’ll use Wireshark (GUI) or tcpdump (CLI), apply filters, inspect packet details, and answer key questions.

---

### 1. Load the PCAP

**Objective:** Open the capture file to begin analysis.

**Wireshark (GUI):**

1. Launch Wireshark.
2. Click **File → Open**.
3. Select **dns.pcap** and click **Open**.
4. Observe the full packet list.

![pcap loading](https://i.ibb.co/0jPWPS9X/image.png)

**tcpdump (CLI):**

```bash
$ tcpdump -r dns.pcap tcp port 389
```

- **-r dns.pcap**: Read from the file.
- **tcp port 389**: Only display LDAP traffic.

>[!TIP]
> 
> tcpdump shows raw bytes; prefer Wireshark for LDAP protocol decoding.

---

### 2. Identify LDAP Traffic

**Objective:** Filter out irrelevant packets.

**Wireshark display filter:**

```
ldap or tcp.port == 389
```

![ldap or tcp.port == 389 filter results](https://i.ibb.co/N6R6FXP0/image.png)

- **ldap**: Decoded LDAP messages.
- **tcp.port == 389**: Any TCP packet on port 389.

**tcpdump filter:**

```bash
$ tcpdump -r dns.pcap tcp port 389
```

![tcpdump filter](https://i.ibb.co/qYtpgMkD/image.png)

---

### 3. Count Packets

**Objective:** Determine total LDAP messages exchanged (requests + responses).

1. Apply the filter `ldap`, check Wireshark’s status bar for **Displayed: 14 (7.7%)**.
2. **Answer:** 14 LDAP messages.

> _Why it matters:_ Knowing volume helps assess session complexity.

![packets count](https://i.ibb.co/TBWvDWB4/image.png)

---

### 4. Analyze LDAP Simple Binds

**Objective:** Examine the authentication bind operation.

#### 4.1 Locate bindRequest

- **Filter:**
  ```
  ldap.messageID == 3 && ldap.bindRequest_element
  ```
- **Result:** Two packets 

![bind request](https://i.ibb.co/TBy3wkqK/image.png)

#### 4.2 Extract bindRequest details

| **Field**          | **Value**            | **Description**                                   |
| ------------------ | -------------------- | ------------------------------------------------- |
| Client IP:Port     | 192.168.122.190:51635 | Source endpoint initiating bind                   |
| Server IP:Port     | 192.168.122.189:389  | LDAP server endpoint                              |
| LDAP Version       | 3                    | Protocol version                                 |
| Bind DN            | `<MISSING>`          | Absent for SASL; simple binds would list DN      |
| Auth Type          | SASL (3)             | SASL indicates advanced mechanism; simple=0       |
| SASL Mechanism     | GSS-SPNEGO         | Kerberos-based secure authentication negotiation       |


In **LDAP**, the **Bind DN (Distinguished Name)** identifies the client attempting to authenticate.

- For **Simple Binds**, the client typically provides a plain-text DN (e.g., `cn=admin,dc=example,dc=com`) along with a password.
  
- For **SASL Binds**, the authentication mechanism is more complex (e.g., **Kerberos**, **DIGEST-MD5**, etc.) and may not require the DN to be explicitly provided in the Bind Request.

In this case, the **Bind DN is absent** because the client used **SASL authentication**, which negotiates credentials differently and often does **not include a DN** in the initial request. This is **expected behavior** for SASL binds.

![bindRequest details](https://i.ibb.co/Gf9B0SJn/image.png)

#### 4.3 Inspect bindResponse

- **Filter:**
  ```
  ldap.messageID == 3 && ldap.bindResponse_element
  ```
- **Result:** Two packets labeled **Bind Response**:

| **Field**       | **Value**              | **Explanation**                                 |
| --------------- | ---------------------- | ----------------------------------------------- |
| Result Code     | saslBindInProgress(14) | SASL exchange ongoing; not final success/fail   |

**Answer to Question 2**

> **What DN did the client bind as, and was authentication successful?(may be a tricky question)**
>
> - **Bind DN:** _Not present_ (SASL bind hides DN)
> - **Authentication:** In progress (saslBindInProgress **14**). Look for a later bindResponse code **0** (success) or **49** (invalidCredentials) to conclude. //Check package no. 159

![Q2](https://i.ibb.co/21h5bpBY/image.png)
---

### 5. Analyze LDAP Search Operations

**Objective:** Examine directory search requests and results.

#### 5.1 Locate searchRequest packets

- **Filter alternatives:**
  ```
  ldap.searchRequest_element
  ```
  or by ID:
  ```
  ldap.messageID == 1 && ldap.searchRequest_element
  ldap.messageID == 2 && ldap.searchRequest_element
  ```


![search result searchRequest](https://i.ibb.co/DfhDJnrY/image.png)

#### 5.2 searchRequest details(here are the searchRequest details for messageID == 1 only)

| **Field**       | **Value**           | **Description**                                        |
| --------------- | ------------------- | ------------------------------------------------------ |
| Message ID      | 1             | Correlates request ↔ response                          |
| Base DN         | `<MISSING>`         | Empty means root DSE (directory service entry)         |
| Scope           | baseObject (0)      | Only the base entry, no children (shallow search)      |
| Filter          | (objectClass=*)     | Matches all objects under Base DN                      |

![searchRequest details](https://i.ibb.co/B5Xp3ZMt/image.png)

#### 5.3 Count search results

- **Filter responses:**
  ```
  ldap.messageID == 1 && ldap.searchResEntry_element
  ldap.messageID == 1 && ldap.searchResDone_element
  ldap.messageID == 2 && ldap.searchResEntry_element
  ldap.messageID == 2 && ldap.searchResDone_element
  ```
- **Entries returned:**
  - ID 1: 2 entries
  - ID 2: 2 entries
- **Result code (searchResDone):** success (0)

![result code searchResDone](https://i.ibb.co/JYjYdFk/image.png)

**Answer to Questions 3 & 4**

> **What Base DN was used, and how many entries returned?**
>
> - **Base DN:** Root DSE (empty / _<MISSING>_)
> - **Entries:** 2 per search (IDs 1 & 2)
>
> **What scope was used in search requests?**
>
> - **Scope:** baseObject (0) — only the specified entry.

---

### 6. Analyze LDAP Unbind

**Objective:** Confirm session closure.

#### 6.1 Locate unbindRequest

- **Filter:**
  ```
  ldap.unbindRequest_element
  ```
- **Result:** Two packets (messageID 4).

![unbindRequest filter](https://i.ibb.co/3YRShsxF/image.png)

#### 6.2 Verify TCP teardown

1. Right-click → **Follow → TCP Stream**.

![follow tcp stream](https://i.ibb.co/VcM5fjyX/image.png)

2. After unbindRequest observe:
   - Client → Server: **FIN, ACK**
   - Server → Client: **FIN, ACK**
   - Client → Server: **ACK**

**Answer to Question 5**

> **List the TCP flags observed during session establishment and teardown:**
>
> - **Establishment (3‑way handshake):**
>   1. SYN
>   2. SYN, ACK
>   3. ACK
>
> - **Teardown:**
>   1. FIN, ACK (client)
>   2. FIN, ACK (server)
>   3. ACK (client)


![Q5 TCP flags](https://i.ibb.co/LdJTsrcb/image.png)
---

### 7. Answer Questions


#### Q1: How many LDAP operations (requests) did the client perform?
- **Count method:** 
  ```
  ldap
  ```
  count individual operations by messageID (IDs 1, 2, 3, 4).
- **Result:**
  - **Bind Request:** 2x2 (ID 3)
  - **Search Requests:** 4x2 (IDs 1 & 2)
  - **Unbind Request:** 1x2 (ID 4)
  - **Total Requests:** **7x2** 



---

#### Q2: What DN did the client bind as, and was authentication successful?
- **Bind DN:** *Not present* in the packet because it’s a SASL bind. Simple binds would display a DN such as `cn=admin,dc=example,dc=com` here.
- **Authentication Status:**
  - **Result Code:** saslBindInProgress (14)
  - **Interpretation:** SASL handshake is ongoing; no final success/failure in this capture.
  - **To confirm success/failure:** look for a later **bindResponse** with code **0** (success) or **49** (invalidCredentials). //in our case code **0** (success)

>[!TIP]
>
> *Educational tip:* SASL binds are multi-step—Wireshark may show subsequent packets labeled **LDAP: primary message** with EXTERNAL/GSSAPI tokens.

---

#### Q3: What Base DN was used for search, and how many entries returned per operation?
- **Base DN:** Root DSE (empty string, displayed as _<MISSING>_). The root of the directory.
- **Entries Returned:** 2 entries for each of the two searches (IDs 1 & 2).

>[!TIP]
>
> *Why it matters:* Understanding Base DN and result size helps identify scope of directory enumeration.

---

#### Q4: What scope was used in search requests?
- **Scope:** baseObject (0)
- **Meaning:** Only the specified Base DN entry itself is examined, not its children.

>[!TIP]
>
> *Tip:* Other scopes include singleLevel (1) and wholeSubtree (2).

---

#### Q5: List the TCP flags observed during session establishment and teardown.
- **Establishment (3‑way handshake):** SYN → SYN, ACK → ACK
- **Teardown:** FIN, ACK (client) → FIN, ACK (server) → ACK (client)

>[!TIP]
>
> *Insight:* Confirming proper TCP teardown ensures sessions aren’t orphaned, which can be a sign of abnormal termination.

---

#### Q6: Write a Snort/Suricata rule to detect LDAP simple bind attempts.
```snort
alert tcp any any -> any 389 (
  msg:"LDAP Simple Bind Attempt";
  content:"|60|";    # LDAP BindRequest tag (ASN.1 SEQUENCE)
  depth:1;
  content:"|80|";    # simpleAuth [0] tag indicates simple bind
  offset:5;
  classtype:attempted-admin;
  sid:1000001;
  rev:1;
)
```

- **Explanation:**
  - `|60|` is the ASN.1 tag for an LDAP BindRequest.
  - `|80|` at offset 5 matches the simple authentication tag.
  - Adjust `sid` and `classtype` per your policy.

---

## Resources for Studying

- https://cloudshark.org/captures/59ea342b5a13/download
- https://en.wikipedia.org/wiki/Lightweight_Directory_Access_Protocol
- https://www.okta.com/identity-101/what-is-ldap/