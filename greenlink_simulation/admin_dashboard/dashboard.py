
from flask import Flask, render_template_string, send_file
import json
import os
from datetime import datetime
from weasyprint import HTML

app = Flask(__name__)
LOG_FILE = "phishing_server/logs/attempts.json"
PDF_EXPORT = "admin_dashboard/simulation_report.pdf"
SKILLVENZA_LOGO = "https://skillvenza.com/wp-content/uploads/2025/05/cropped-Logo-4-300x240.png"

HTML_TEMPLATE = f"""
<!DOCTYPE html>
<html>
<head>
    <title>GreenLink Admin Dashboard | SkillvenzA</title>
    <style>
        body {{
            font-family: 'Segoe UI', sans-serif;
            background-color: #f7f9fa;
            margin: 0;
            padding: 0;
        }}
        header {{
            background-color: #ffffff;
            color: #0A3161;
            padding: 20px;
            text-align: center;
            border-bottom: 2px solid #b7410e;
        }}
        header img {{
            height: 50px;
            vertical-align: middle;
            margin-right: 10px;
        }}
        h1 {{
            display: inline;
            font-size: 24px;
            vertical-align: middle;
            color: #0A3161;
        }}
        main {{
            padding: 30px;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }}
        th, td {{
            padding: 12px;
            border: 1px solid #ccc;
            text-align: left;
        }}
        th {{
            background-color: #0A84FF;
            color: white;
        }}
        tr:nth-child(even) {{
            background-color: #f2f2f2;
        }}
        .note {{
            margin-top: 30px;
            font-size: 13px;
            color: gray;
            text-align: center;
        }}
        .export {{
            margin: 10px auto;
            text-align: center;
        }}
        .export a {{
            background-color: #0A3161;
            color: white;
            padding: 10px 20px;
            text-decoration: none;
            border-radius: 5px;
            font-size: 14px;
        }}
    </style>
</head>
<body>
    <header>
        <img src='{SKILLVENZA_LOGO}' alt='SkillvenzA Logo'>
        <h1>GreenLink Simulation Logs</h1>
    </header>
    <main>
        <div class="export">
            <a href="/export" target="_blank">Download PDF Report</a>
        </div>
        <table>
            <tr>
                <th>Email</th>
                <th>IP Address</th>
                <th>Timestamp</th>
            </tr>
            {{% for log in logs %}}
            <tr>
                <td>{{{{ log.email }}}}</td>
                <td>{{{{ log.ip }}}}</td>
                <td>{{{{ log.timestamp }}}}</td>
            </tr>
            {{% endfor %}}
        </table>
        <div class="note">Powered by SkillvenzA | www.skillvenza.com</div>
    </main>
</body>
</html>
"""

@app.route("/")
def dashboard():
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE) as f:
            data = json.load(f)
    else:
        data = []
    return render_template_string(HTML_TEMPLATE, logs=data)

@app.route("/export")
def export_pdf():
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE) as f:
            logs = json.load(f)
    else:
        logs = []
    html_content = render_template_string(HTML_TEMPLATE, logs=logs)
    HTML(string=html_content).write_pdf(PDF_EXPORT)
    return send_file(PDF_EXPORT, as_attachment=True)

if __name__ == "__main__":
    app.run(port=5050, debug=True)
