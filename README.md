# 🔐 Secure File Sharing System  
**Cyber Security Internship – Task 3 | Future Interns**

## 📌 Project Overview
This project is a **Secure File Sharing System** developed as part of the **Cyber Security Internship at Future Interns**.  
The system allows users to securely upload and download files using **AES encryption**, ensuring confidentiality, integrity, and controlled access to stored data.

Files are encrypted **before storage** and decrypted **only at the time of download**, preventing unauthorized access to sensitive data.

---

## 🎯 Objectives
- Build a secure web portal for file upload and download
- Implement strong encryption to protect files at rest
- Ensure decryption occurs only for authorized requests
- Apply basic key management best practices
- Test the system for security and file integrity
- Follow GitHub-ready secure coding practices

---

## 🛠️ Tech Stack
- **Backend:** Python, Flask  
- **Frontend:** HTML  
- **Cryptography:** AES (Advanced Encryption Standard – EAX Mode)  
- **Library:** PyCryptodome  
- **Version Control:** Git & GitHub  

---

## 🧩 Features
- Secure file upload interface
- AES-256 encryption before file storage
- Encrypted files stored with `.enc` extension
- Secure decryption only during download
- Protection against direct access to encrypted files
- Secure filename handling using `secure_filename()`
- Basic encryption key management
- File integrity verification during decryption
- GitHub-safe configuration using `.gitignore`

---



## 🔐 Encryption & Security Design

### 🔹 Encryption
- AES-256 encryption using **EAX mode**
- Files are encrypted immediately after upload
- Encrypted data includes:
  - Nonce
  - Authentication tag
  - Ciphertext

### 🔹 Decryption
- Decryption occurs only through a secure Flask route
- Integrity is verified using authentication tags
- Any tampered file fails decryption

### 🔹 Key Management
- AES key is generated once and stored locally in `secret.key`
- The key file is **excluded from GitHub** using `.gitignore`
- Prevents exposure of sensitive cryptographic material

### 🔹 Access Control
- Encrypted files directory is not exposed as a static route
- Files cannot be downloaded directly via URL
- Only authorized download routes allow decryption

---

## 🧪 Security Testing Performed
- ✅ Unauthorized direct access prevention test  
- ✅ File integrity verification using AES authentication tags  
- ✅ Secure key handling verification  
- ✅ Empty file and invalid request handling  
- ✅ Filename sanitization to prevent path traversal  

---

###conclusion
✅ Conclusion

The Secure File Sharing System developed in this project successfully demonstrates the practical application of cryptography and secure backend development principles. By implementing AES-256 encryption, files are protected before storage, ensuring data confidentiality and security at rest. Decryption is strictly performed only during authorized download requests, preventing unauthorized or direct access to sensitive data.

The project follows essential cyber security best practices, including secure filename handling, controlled access through backend routes, basic encryption key management, and exclusion of sensitive assets from version control. File integrity is verified during decryption, ensuring that any tampering or corruption is detected and blocked.

Through this task, I gained hands-on experience in secure file handling, encryption techniques, key management, and secure web application design. This project strengthened my understanding of how real-world systems protect data and enforce security controls, making it a valuable learning experience as part of the Cyber Security Internship at Future Interns.

Overall, this system provides a solid foundation for secure file sharing and can be further enhanced with user authentication, access control, and cloud deployment for real-world scalability.


LINKEDIN POST :- https://www.linkedin.com/posts/suman-karak-2851ba351_futureinterns-cybersecurity-securefilesharing-activity-7411035769152356352-GS-s?utm_source=share&utm_medium=member_desktop&rcm=ACoAAFfF3AUBoQq2ywWEIjyep_EkG3FjL-kz1CY

