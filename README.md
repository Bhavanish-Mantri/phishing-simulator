# Phishing Simulator (Educational Use Only)

A lightweight phishing simulation tool built with **Python** and **Flask** to demonstrate how phishing attacks work — strictly for **cybersecurity awareness and education**.

---

## 📌 Project Overview

This project simulates a phishing page that captures submitted credentials to help learners understand how phishing attacks collect sensitive information. The tool is intended for **ethical training, awareness, and controlled lab environments only**. :contentReference[oaicite:2]{index=2}

---

## 📁 Project Structure
```
phishing-simulator/
├── phishdetect_app.py # Main Flask application
├── requirement.txt # Python dependencies
├── templates/ # HTML templates (e.g., fake login page)
├── logs/ # Captured credential logs
├── .gitignore
└── README.md
```

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Bhavanish-Mantri/phishing-simulator.git
cd phishing-simulator
```
## 2️⃣ Install Dependencies

Ensure you have **Python 3** and **pip** installed, then run:

```bash
pip install -r requirement.txt
```
## 3️⃣ Run the Flask Application

Start the phishing simulator:
```
python phishdetect_app.py
```
By default, the application runs locally at:
```
http://127.0.0.1:5050
```
## 🎯 Features

- 🪪 Simulates phishing through a fake login interface  
- 📥 Logs captured credentials for demonstration purposes  
- 🚿 Flask-powered web backend  
- 🌐 Optional public access via ngrok  
- ❗ Focused on ethical hacking and security training  

---

## 🔐 Ethical Use Only

⚠️ This project is intended **strictly for ethical hacking, cybersecurity education, and awareness training**.  
Using phishing tools on real users **without explicit permission** is illegal and unethical.  
Always operate in a controlled environment with proper consent.

---

## 🙌 Contributing

Contributions and improvements are welcome! You can:

- 💡 Add improved phishing templates  
- 🔐 Enhance credential logging and reporting  
- 📊 Automate analysis and tracking  
- 🛡 Implement defenses or detection mechanisms  

Submit a **pull request** or open an **issue** to get started.

---

## 📜 License

MIT License © 2026
