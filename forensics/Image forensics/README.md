# BUET CTF 2024 - Image Forensics Challenges

## **Challenge 1: Credentials**
### 📜 Scenario:
A suspected internal threat actor, **Mehedi**, an IT technician at **Pixel LTD**, was recently apprehended under suspicion of data exfiltration and other crimes. His company-issued devices and digital accounts were seized as evidence. Initial analysis indicates that Mehedi may have connected with an unknown entity and attempted unauthorized access to sensitive company information, likely in exchange for financial gain.
You have access to an image of Mehedi's seized device. Your task is to investigate and uncover evidence of his activities, interactions, and potential data leaks.

>  📝 Note: All memory forensics challenges use the same image file. Virtual Machine (VM) is recommended to perform the forensic analysis.
> Attachment: [image_dump.7z](https://drive.google.com/file/d/1uUyXE5qoP8XMAXiuOWjDBDO37bx5Zfo8/view?usp=sharing)
   - **Challenge Description: Identify the user's username and password used to log into the system.**
   - **Difficulty:** Easy   
   - **Flag Format:** `BUETCTF{user_password}`
   - **Author: or3ki_01xs**
   
### **Flag 🚩:** `BUETCTF{mehedi_abracadabra}`
  
#### Solution: 
Perform SAM dump using the SYSTEM and SAM files, then decrypt the NTLM hash. You can use tools like John the Ripper, Hashcat, or online resources such as CrackStation or Hashes to assist with cracking the hash.
  
---

## **Challenge 2: Missing Assets**
   - **Challenge Description: How many company assets might he have sold?**
   - **Difficulty:** Easy
   - **Author: or3ki_01xs**   

### **Flag 🚩:** `BUETCTF{6}` 

#### Soltution:
Examine the emails for evidence of conversations where individuals inquired about the prices or availability of products. Specifically, look for mentions of 3 hard disks, 1 computer desk, 1 laptop, and 1 rehal in the email exchanges.

---

## **Challenge 3: Encrypted Identity**
   - **Challenge Description: What is the DOB of the user?**  
   - **Difficulty:** Medium   
   - **Hint:** TrueCrypt file – something is there!  
   - **Flag Format:** `BUETCTF{01_Jan_1799}`
   - **Author: or3ki_01xs**
  
### **Flag 🚩:** `BUETCTF{20_May_1995}`  

#### Solution:
Recover the TrueCrypt password for the file nothing.txt. The password is 'sunshine'. First, use truecrypt2john to extract the hash, then decrypt it using John the Ripper with the command:
```
truecrypt2john nothing.txt > hash
john -w /usr/share/wordlists/rockyou.txt --format=tc_aes_xts hash
```
This will reveal a Google Drive link containing a picture of the user's ID.

---

## **Challenge 4: Installation Discovery**
   - **Challenge Description: Find out the name of the software used to encrypt the file and the installation completion time.**  
   - **Difficulty:** Easy  
   - **Flag Format:** `BUETCTF{software_XX/XX/XXXX XX:XX:XX}`
   - **Author: or3ki_01xs**  

### **Flag 🚩:** `BUETCTF{truecrypt_07/12/2024 03:53:02}`  

#### Solution:
Check the file located at Windows/appcompat/Programs/Install/INSTALL_ffff_9fe25cdb-7ef3-44fe-86f6-7c4bf5b12805.xml to find the program name and installation time.

---

## **Challenge 5: Hidden mails**
   - **Challenge Description: What is the hidden flag of the email?**  
   - **Difficulty:** Hard   
   - **Hint:** Look for email attachments  
   - **Flag Format:** `BUETCTF{s0m3_t3xt}`
   - **Author: or3ki_01xs**   

### **Flag 🚩:** `BUETCTF{h1d1nG_mEsSageS_1s_an_AR7}`  

#### Solution:
1. Use `eml-extractor` or similar tool to extract the attachment from the email, target file `Steg test.eml`:
```
eml-extractor -f "Steg test.eml"
```
2. Extract the zip file to find a folder called `flag` containing multiple images. Then use `exiftool` on the image named `#382c18-#eae52d-#392011.png`:
```
exiftool \#382c18-\#eae52d-\#392011.png
```
3. Optionally, use the strings command to scan through images for more clues:
```
strings * | sort -u
```

---

## **Challenge 6: Footprints**
   - **Challenge Description: What is the name of the infamous search engine the user used, and what is the name of the forum that the threat actor may have used?**  
   - **Difficulty:** Easy  
   - **Hint:** Check the browser histories  
   - **Flag Format:** `BUETCTF{url_forum name}`  
   - **Author: or3ki_01xs**
     
### **Flag 🚩:** `BUETCTF{https://ahmia.fi_dread}`
  
#### Solution:
Analyze the Microsoft Edge browser history using FTK Forensics or Autopsy. Look for entries that point to the search engine Ahmia. Check the search results for a link to the Dread forum.
The combined flag will be in the format: BUETCTF{https://ahmia.fi_dread}

  ---
   
## **Challenge 7: Space secrets**
   - **Challenge Description: Extract the message from a confidential file that is linked to another email attachment.**  
   - **Difficulty:** Hard  
   - **Hint:** Look for an email attachment `free`; consider whitespace steganography `paid`  
   - **Flag Format:** `BUETCTF{s0m3_t3xt}`
   - **Author: or3ki_01xs**

### **Flag 🚩:** `BUETCTF{C0Nf1d3n714l_D0cuM3N75_6e6f74616e796d6f7265}`  
#### Solution:
Extract the email attachment from the file named 'winter is comming.eml' using eml-extractor or through manual extraction if necessary.
```
eml-extractor -f "winter is somming.eml"
```
or 
```
echo 'Q2hlY2sgdGhpcyBvbmU6IGh0dHBzOi8vbWVnYS5uei9maWxlL0x5SVFESXpECSAgICAgCSAJICAgCS
AgICAgICAKICAgIAkgICAgIAkgICAgICAJICAgIAkgICAJICAgICAgCQkgICAgICAJICAgCSAgICAg
IAoJICAgICAgIAkgICAgCSAgIAkgCSAgIAkgICAJICAJCSAgCiAgICAgICAJIAkgICAgICAJICAgCS
AgIAkgIAkgCSAgCSAgICAgIAkgIAogICAgICAJICAJICAgICAgIAkgICAgIAkgICAgICAJICAgICAJ
ICAJIAkgICAgICAgCSAgICAgCiAgCSAJICAgICAJICAgIAkgIAkgICAJCSAgICAgIAkgICAgICAJIC
AgICAKICAgIAkgIAkJICAgICAJICAgICAgIAkgICAgICAgCSAgICAgIAkJICAgICAgIAoJIAkgICAg
ICAgCSAgICAJICAgICAgCSAgICAgCSAgCSAgCSAgICAJICAgCiAgICAgCSAgIAkgCSAgICAJICAJIC
AgICAgIAkgICAgIAkgICAgCSAgCSAgCiAgICAgICAJICAgICAgCQkJICAgICAgCSAgICAgCSAJICAg
CSAgIAkgICAKICAgIAkJICAgICAgCSAgICAgCSAJICAgICAgCSAgCSAJIAkgICAgCiAgICAgIAkgIC
AgICAgCSAgCSAJICAgICAgIAkgIAkgICAJICAgICAgCSAgCSAgCgkgICAJICAgICAgIAkgICAgIAkg
ICAgICAJIAkgIAkgICAgICAgCSAgICAgIAkgICAKICAgCSAgICAgCSAgICAJIAkgICAgICAJICAgIA
kgIAkgICAgICAJICAgIAo=' | base64 -d > message.txt
stegsnow -C message.txt
```
This will help to recover this full url: `https://mega.nz/file/LyIQDIzD/2nikUrVaFJg9qhePmSggsx7gyiHWiCa0-RH0uTwBze8`

Extract the zip file, then change the font color of `non-disclosure-agreement.docx`. The hidden message can be found on the last page of the document.

---
