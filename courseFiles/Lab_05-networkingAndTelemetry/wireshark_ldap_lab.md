#  Lab: LDAP Traffic Analysis (`dns.pcap`)

**PCAP File:** `dns.pcap` (contains LDAP over TCP traffic) // [Click here to download](./dns.pcap)

##  Objective

Analyze the provided PCAP to investigate LDAP operations between a client and server. You will filter LDAP traffic, reconstruct search and bind operations, and interpret LDAP messages—a key skill for SOC investigations involving directory service abuse or enumeration.

---

## Tools & Setup

- **Wireshark** (GUI) or **tcpdump** (CLI)
- PCAP: `dns.pcap` (located in current directory)  // [Click here to download](./dns.pcap)

---

## Lab Instructions

### 1. Load the PCAP

- **Wireshark**: File → Open → select `dns.pcap`

![pcap loading](https://i.ibb.co/0jPWPS9X/image.png)

- **tcpdump**:
  ```bash
  tcpdump -r dns.pcap tcp port 389
  ```

### 2. Identify LDAP Traffic

- **Wireshark Display Filter**: `ldap` or `tcp.port == 389`

![ldap filter](https://i.ibb.co/Rp6tDvH5/image.png)

- **tcpdump Filter**:
  ```bash
  tcpdump -r dns.pcap tcp port 389
  ```

### 3. Count Packets

- How many LDAP messages (requests + responses) are exchanged?

### 4. Analyze LDAP Simple Binds

- Locate the `bindRequest` (operation ID 3)

![bindRequest package](https://i.ibb.co/RkSFNv56/image.png)

- Identify:

  - **Client IP & Port**
  - **LDAP version**
  - **Bind DN (Distinguished Name)**
  - **Authentication type** (ex: SASL)

- Locate the matching `bindResponse`

  - **Result code** (ex: `success`, `invalidCredentials`)

### 5. Analyze LDAP Search Operations

- Find each `searchRequest` (operation IDs 1 and 2)

- For each, record:

  - **Base DN** (ex: `<ROOT>`)
  - **Scope** (baseObject, singleLevel, wholeSubtree)
  - **Filter** (ex: `(objectClass=*)` if shown)

- Locate corresponding `searchResEntry` and `searchResDone`

  - **Number of entries returned**
  - **Result code** (could be `success`... or not)

### 6. Analyze LDAP Unbind

- Identify the `unbindRequest`
- Confirm session teardown with subsequent TCP FINs

### 7. Answer Questions

1. How many LDAP operations (requests) did the client perform?
2. What DN did the client bind as, and was authentication successful?(may be a tricky question)
3. What Base DN was used for search, and how many entries returned per operation?
4. What scope was used in search requests?
5. List the TCP flags observed during session establishment and teardown.
6. Write a Snort/Suricata rule to detect LDAP simple bind attempts.

---

## Completion Criteria

- Accurate packet counts for LDAP operations
- Detailed LDAP bind and search metadata
- Understanding of LDAP message structure
- Basic detection rule for LDAP binds

---

## Background

LDAP (Lightweight Directory Access Protocol) on TCP port 389 is used by Active Directory and other directory services. Monitoring LDAP can reveal authentication attempts, directory enumeration, and reconnaissance.

---

When you're done, check out the **step-by-step solution** [here](./wireshark_ldap_lab_solution.md)

---

## Resources for Studying

- https://cloudshark.org/captures/59ea342b5a13/download
- https://en.wikipedia.org/wiki/Lightweight_Directory_Access_Protocol
- https://www.okta.com/identity-101/what-is-ldap/
