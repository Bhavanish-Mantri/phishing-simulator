# phishing-simulator
⚙️ Project Structure

phishing-simulator/
├── phishdetect_app.py        # Main Flask application
├── requirement.txt           # List of Python dependencies
├── templates/                # Contains HTML templates (e.g. fake login page)
├── logs/                     # Stores captured credential logs

🛠️ Getting Started

Follow these steps to run the project locally on Kali Linux or any system with Python installed:
1. Clone the Repository

git clone https://github.com/Bhavanish-Mantri/phishing-simulator.git
cd phishing-simulator

2. Install Dependencies

Make sure Python and pip are installed. Then run:

pip install -r requirement.txt

3. Run the Flask Application

python phishdetect_app.py

The app will start running locally at http://127.0.0.1:5050.
4. Create a Public URL using Ngrok

Open a new terminal and run:

ngrok http 5050

Ngrok will provide a public link (e.g. https://xyz.ngrok.io) which you can use to test the phishing page from other devices.
🔐 Ethical Use Only

    ⚠️ This project is intended only for ethical hacking and educational purposes. Do not use it against real users without their informed consent. Phishing is illegal and unethical when done maliciously.

Always conduct tests in a controlled lab environment or with permission during awareness campaigns or security training sessions.
📄 License

This project is open-source and available under the MIT License.
🤝 Contributing

Pull requests and suggestions are welcome! If you'd like to improve the templates, add detection tools, or automate report generation, feel free to contribute.
