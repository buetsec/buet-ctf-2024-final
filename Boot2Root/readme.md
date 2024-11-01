# Boot 2 Root Challenge Series

## Challenge 1: The Hacker's Note

*The Hacker's Note* is an online library for selling hacking-related books, currently under development. Your objective: perform a penetration test on the application and uncover its hidden treasure.

**Platform Link:** [BUET CTF THM](https://tryhackme.com/jr/buetctf24)  
**Author:** [0xf4h1m](https://www.linkedin.com/in/oxf4h1m)  
**Max Attempts:** 3  
**Points:** 100-150 (dynamic)  

**Flag:**  
`BUETCTF{ADM1N_P4N3L_T4K30V3R_0N_H4CK3RSN0T3_V14_VULN3R4BL3_3NDPO1NT_3SC4L4T10N_G41N3D_4DM1N_C0NTR0L}`

---

### Solution

1. **Create an Account**  
   - Register on the site to create an account.

2. **Access Profile Settings**  
   - Go to your profile settings and locate the "Change Password" feature.

3. **Intercept Change Password Request**  
   - Use Burp Suite to intercept the change password request.

4. **Bruteforce UID**  
   - Use Burp Suite's Intruder tool to brute-force UIDs from `1000` to `1055`.  
   - This should trigger an IDOR (Insecure Direct Object Reference) vulnerability, allowing the Admin password to be changed.

5. **Retrieve Admin Email**  
   - Log out and navigate to the "Contact Us" page, where you’ll find the Admin's email address.

6. **Login with Admin Credentials**  
   - Use the Admin email and the new password to log in and capture the flag.





## Challenge 2: The Developer

Can you gain access to the Developer’s account?

**Platform Link:** [BUET CTF THM](https://tryhackme.com/jr/buetctf24)  
**Author:** [0xf4h1m](https://www.linkedin.com/in/oxf4h1m)  
**Max Attempts:** 3  
**Points:** 200-300 (dynamic)  
**Prerequisites:** Challenge 1  

**Flag:**  
`BUETCTF{CR3D3NT14L_L34K_V14_ST3GO_1M4G3_L3D_T0_PR1V_ESC4L4T10N_UNC0V3R3D_H1DD3N_D4T4_4ND_G41N3D_OR3k1_ACC3SS}`

---

### Solution

A file upload vulnerability exists in the "Add Book" feature in admin panel, allowing for the upload of a webshell or reverse shell.

1. **Upload Webshell**  
   - Exploit the vulnerability by uploading a webshell or reverse shell to gain access.

2. **Explore Directory**  
   - Run `ls -laR /home/or3k1` to list files.  
   - Locate a `my_password.txt` file within a confidential folder, containing a hint:  
     > “I like to store my password in the deep surface of the seas because I can't memorize password after password.”

3. **Locate Password Image**  
   - In the image folder, find `Password.jpg`.  
   - Download the image and scan the embedded QR code to retrieve a Wi-Fi password.

4. **Extract Hidden Data**  
   - Use the Wi-Fi password to unlock hidden information:  
     ```bash
     steghide extract -sf Password.jpg
     ```
   - This reveals the actual password.

5. **Access SSH**  
   - Use the retrieved password to SSH into the `or3k1` account and access `user.txt` to capture the flag.


## Challenge 3: The Super Admin

Can you compromise the Super Admin’s account?

**Platform Link:** [BUET CTF THM](https://tryhackme.com/jr/buetctf24)  
**Author:** [0xf4h1m](https://www.linkedin.com/in/oxf4h1m)  
**Max Attempts:** 3  
**Points:** 200-300 (dynamic)  
**Prerequisites:** Challenge 2  

**Flag:**  
`BUETCTF{G41N3D_R00T_4CC3SS_V14_NODE_JS_C4PABILITIES_ESCAL4TION_3XPLO1T_BYP4SS3D_R35TRICT10NS_F0R_3LEVATED_PRIVS}`

---

### Solution

1. **Run Linpeas**  
   - Execute `linpeas.sh` to scan for privilege escalation opportunities.
   - Linpeas will reveal capabilities for `/usr/bin/node`.

2. **Privilege Escalation Using Node.js**  
   - Use the following payload to escalate privileges to root:
     ```bash
     node -e 'process.setuid(0); require("child_process").spawn("/bin/sh", {stdio: [0, 1, 2]})'
     ```

3. **Capture the Flag**  
   - After gaining root access, retrieve `root.txt` to capture the flag.



## Challenge 4: The Bonus Flag

Discover a hidden Bonus Flag buried deep within the system.

**Platform Link:** [BUET CTF THM](https://tryhackme.com/jr/buetctf24)  
**Author:** [0xf4h1m](https://www.linkedin.com/in/oxf4h1m)  
**Max Attempts:** 3  
**Points:** 200-300 (dynamic)  
**Prerequisites:** Challenge 3  

**Flag:**  
`BUETCTF{Unch3ck3d_F1le_Upl04d_L3ads_t0_RCE_P4wn!_F1lter_Byp@ss_F0r_Web_3xploit_W1ns_Th3_Flag!}`

### Solution 

MySQL will help you to find this flag. xD