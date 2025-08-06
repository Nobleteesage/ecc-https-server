# ECC-Based HTTPS Server using Python and OpenSSL

This project demonstrates how to run a secure HTTPS server using Python's built-in HTTP module and an ECC-based SSL certificate generated with OpenSSL.

## 🔐 What It Does
- Serves HTTPS locally on `https://localhost:4443`
- Uses ECC private key and self-signed certificate
- Ideal for cybersecurity learners and local dev environments

## 🛠️ How to Run

1. Generate the ECC private key:
   ```bash
   openssl ecparam -genkey -name prime256v1 -out ecc_private.key
**Step 2: Create `.gitignore` to protect sensitive files**

```bash
nano .gitignore
Paste:

markdown
Copy code
*.key
*.pem
*.csr
__pycache__/
