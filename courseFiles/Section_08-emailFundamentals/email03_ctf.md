# CTF Challenge – Email Analysis 03

**File:** [email03.eml](./email03.eml)  
**Category:** Google Docs Notification / Email Header Forensics

## Questions


1. **Origin IP Identification**  
   Which IPv4 address appears in the earliest `Received:` header (the first hop visible)?  
   *Answer format:* IPv4 address

2. **DMARC Disposition**  
   What DMARC policy (`p=` tag) is indicated by the `ARC-Authentication-Results` header?  
   *Answer format:* policy value

3. **Google Redirect Unwrapping**  
   In the AMP HTML section, links are wrapped with `https://www.google.com/url?q=`. Identify the true target URL behind the redirect for the script link providing funds information.  
   *Answer format:* full unwrapped URL

4. **Mentioned Users Count**  
   How many distinct user email addresses are mentioned in the comment body (those prefixed with `@`)?  
   *Answer format:* number


5. **DynamicMail Comments Endpoint**  
   Extract the base hostname of the `src` URL used by the `<amp-list>` tag for dynamic mail comments (before any query string).  
   *Answer format:* hostname only (no protocol or path)

---

## Writeup and Solutions

### Q1: Origin IP Identification

- **Where to look:** `Received:` header near the top.  
- **Excerpt:**  
  ```
  Received: from mail-sor-f69.google.com (mail-sor-f69.google.com. [209.85.220.69])
  ```  
- **Answer:**  
  ```
  209.85.220.69
  ```

![](./attachments/email03/q1.png)

### Q2: DMARC Disposition

- **Where to look:** In `ARC-Authentication-Results`.  
- **Excerpt:**  
  ```
  dmarc=pass (p=REJECT sp=REJECT dis=NONE) header.from=docs.google.com
  ```  
- **Answer:**  
  ```
  REJECT
  ```

![](./attachments/email03/Q2.png)

### Q3: Google Redirect Unwrapping

- **Where to look:** AMP HTML contains links wrapped by Google’s redirect service.  
- **Excerpt (AMP HTML):**  
  ```html
  <a href="https://www.google.com/url?q=https://script.google.com/macros/s/AKfycbyB7w6WEN9rrfxrGUZR0uJSJf0977R5blfQ86VcyzfOeSLVl98FusGwC_-BEq_B87aIcA/exec?hjb62k0n81pw5bfhyri&amp;sa=D&amp;source=editors&amp;ust=...&amp;usg=...">
  ```  
- **Unwrapped URL:**  
  ```
  https://script.google.com/macros/s/AKfycbyB7w6WEN9rrfxrGUZR0uJSJf0977R5blfQ86VcyzfOeSLVl98FusGwC_-BEq_B87aIcA/exec?hjb62k0n81pw5bfhyri
  ```


![](./attachments/email03/q3.png)



>Ignore the `3D`

### Q4: Mentioned Users Count

- **Where to look:** Plain-text comment body lists `@email` mentions.  
- **Excerpt:**  
  ```
  @opoggenpeace@gmail.com  
  @sausagemafia@gmail.com  
  @morriscode@gmail.com  
  @ykudjawu@gmail.com  
  @creovex@gmail.com  
  @chappelle99@gmail.com
  ```  
- **Answer:**  
  ```
  6
  ```


![](./attachments/email03/q4.png)


### Q5: DynamicMail Comments Endpoint

- **Where to look:** The `src` attribute of the `<amp-list>` tag.  
- **Excerpt:**  
  ```html
  <amp-list ... src="https://docs.google.com/presentation/d/1jn0VoYpf9LR7qIBVQoUojAvVv3smQsnezp0f6k5Qfwo/dynamicmail/comments?emailToken=...">
  ```  
- **Answer:**  
  ```
  docs.google.com
  ```

![](./attachments/email03/q5.png)

---
