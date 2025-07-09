# 🎣 Phishing Simulator (Educational Use Only)

This is a lightweight phishing simulation project built with **Python Flask**, designed to demonstrate how phishing attacks work — **strictly for educational and awareness training purposes**.

---

## 📁 Project Structure

phishing-simulator/
├── phishdetect_app.py # Main Flask application
├── requirement.txt # Python dependencies
├── templates/ # HTML templates (e.g. fake login page)
├── logs/ # Captured credential logs


---

## 🛠️ Getting Started

Follow the steps below to run the project on **Kali Linux** or any system with Python installed.

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Bhavanish-Mantri/phishing-simulator.git
cd phishing-simulator

2️⃣ Install Dependencies

Make sure Python 3 and pip are installed:

pip install -r requirement.txt

3️⃣ Run the Flask Application

python phishdetect_app.py

By default, the app will run locally at:

http://127.0.0.1:5050

4️⃣ Create a Public URL using Ngrok

In a new terminal window, run:

ngrok http 5050

Ngrok will generate a secure public URL like:

https://random-id.ngrok.io

Use this link to test the phishing page externally (on another device, browser, or network).
🔐 Ethical Use Only

    ⚠️ Disclaimer:
    This project is intended strictly for ethical hacking, cybersecurity education, and awareness training.
    Do not use this tool on real users without explicit permission.

Phishing is illegal when done maliciously. Always use in a controlled lab or for authorized training only.
📄 License

This project is licensed under the MIT License.
🤝 Contributing

Pull requests and suggestions are welcome!

Feel free to contribute if you'd like to:

    Add better templates 💻

    Improve logging/reporting 📝

    Automate phishing detection 🔍

    Enhance security & tracking 🔐

🙋‍♂️ Maintainer

Bhavanish Mantri
🔗 GitHub Profile
