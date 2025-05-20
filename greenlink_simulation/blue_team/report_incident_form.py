
import os
import json
from datetime import datetime

REPORT_LOG = "blue_team/incident_reports.json"

def ensure_log():
    os.makedirs(os.path.dirname(REPORT_LOG), exist_ok=True)
    if not os.path.exists(REPORT_LOG):
        with open(REPORT_LOG, "w") as f:
            json.dump([], f)

def log_report(report):
    ensure_log()
    with open(REPORT_LOG, "r+") as f:
        data = json.load(f)
        data.append(report)
        f.seek(0)
        json.dump(data, f, indent=4)

def collect_report():
    print("=== 🛡️ Incident Report Form ===")
    name = input("Your Name: ").strip()
    dept = input("Department: ").strip()
    email = input("Email or Username involved: ").strip()
    incident_type = input("Type of Suspicious Activity (e.g., Phishing, Unauthorized Access): ").strip()
    description = input("Describe what happened (who, what, where, when): ").strip()

    report = {
        "timestamp": datetime.now().isoformat(),
        "reporter": name,
        "department": dept,
        "email_or_user": email,
        "incident_type": incident_type,
        "description": description
    }

    log_report(report)
    print("\n✅ Report logged successfully. Your team will review it shortly.")

if __name__ == "__main__":
    collect_report()
