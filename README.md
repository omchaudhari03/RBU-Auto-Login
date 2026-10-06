# RBU Auto Login

A lightweight Python automation tool that automatically logs into the RBU network captive portal and continuously monitors internet connectivity.

The project uses **Playwright** to automate the browser-based login process and **Python Requests** to periodically verify whether internet access is available.

---

## 🚀 Features

- Automatic login to the RBU network captive portal
- Secure credential management using `.env`
- Headless Chromium browser automation
- Automatic internet connectivity checking
- Automatically attempts login when internet access is unavailable
- Runs continuously in the background
- Configurable monitoring interval
- Simple and lightweight Python implementation

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Playwright | Browser automation |
| Chromium | Headless browser used by Playwright |
| Requests | Internet connectivity checking |
| python-dotenv | Loading credentials from `.env` |
| Git/GitHub | Version control |

---

## 📁 Project Structure

```text
RBU-Auto-Login/
│
├── login.py
├── monitor.py
├── requirements.txt
├── .gitignore
├── .env
└── README.md
