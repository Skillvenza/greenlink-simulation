
from flask import Flask, render_template_string, request, redirect
import os
import json
from datetime import datetime

app = Flask(__name__)
REPORT_LOG = "blue_team/incident_reports.json"

TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Report an Incident | SkillvenzA Blue Team</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f2f2f2;
            padding: 40px;
        }
        .form-container {
            background: white;
            padding: 30px;
            max-width: 600px;
            margin: auto;
            border-radius: 10px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.2);
        }
        h2 {
            color: #b7410e;
        }
        input, textarea {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        input[type=submit] {
            background-color: #0A84FF;
            color: white;
            font-weight: bold;
            cursor: pointer;
        }
        .footer {
            text-align: center;
            font-size: 13px;
            color: gray;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <div class="form-container">
        <h2>Incident Report Form</h2>
        <form method='POST'>
            <label>Your Name</label>
            <input type='text' name='name' required>

            <label>Department</label>
            <input type='text' name='dept' required>

            <label>Email or Username Involved</label>
            <input type='text' name='email' required>

            <label>Type of Suspicious Activity</label>
            <input type='text' name='incident_type' required>

            <label>Incident Description</label>
            <textarea name='description' rows='5' required></textarea>

            <input type='submit' value='Submit Report'>
        </form>
        <div class="footer">Powered by SkillvenzA | www.skillvenza.com</div>
    </div>
</body>
</html>
"""

def ensure_log():
    os.makedirs(os.path.dirname(REPORT_LOG), exist_ok=True)
    if not os.path.exists(REPORT_LOG):
        with open(REPORT_LOG, "w") as f:
            json.dump([], f)

@app.route("/", methods=["GET", "POST"])
def report_form():
    if request.method == "POST":
        report = {
            "timestamp": datetime.now().isoformat(),
            "reporter": request.form.get("name"),
            "department": request.form.get("dept"),
            "email_or_user": request.form.get("email"),
            "incident_type": request.form.get("incident_type"),
            "description": request.form.get("description")
        }
        ensure_log()
        with open(REPORT_LOG, "r+") as f:
            data = json.load(f)
            data.append(report)
            f.seek(0)
            json.dump(data, f, indent=4)
        return redirect("/")
    return render_template_string(TEMPLATE)

if __name__ == "__main__":
    app.run(port=5080, debug=True)
