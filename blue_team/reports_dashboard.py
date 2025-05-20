
from flask import Flask, render_template_string, send_file, make_response
import os
import json
import csv
from datetime import datetime
from io import StringIO
from weasyprint import HTML

app = Flask(__name__)
REPORT_LOG = "blue_team/incident_reports.json"
PDF_EXPORT = "blue_team/incident_report_summary.pdf"

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Incident Reports Dashboard | SkillvenzA</title>
    <style>
        body {
            font-family: 'Segoe UI', sans-serif;
            background-color: #f7f9fa;
            padding: 30px;
        }
        header {
            text-align: center;
            margin-bottom: 20px;
        }
        header img {
            height: 50px;
            margin-bottom: 10px;
        }
        h1 {
            color: #b7410e;
        }
        .controls {
            text-align: center;
            margin-bottom: 20px;
        }
        input[type="text"] {
            width: 300px;
            padding: 10px;
            margin-right: 20px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        .button {
            background-color: #0A3161;
            color: white;
            padding: 10px 20px;
            text-decoration: none;
            font-weight: bold;
            border-radius: 5px;
            margin-right: 10px;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 10px;
            font-size: 13px;
        }
        th, td {
            padding: 10px;
            border: 1px solid #ccc;
            text-align: left;
            vertical-align: top;
        }
        th {
            background-color: #0A84FF;
            color: white;
        }
        tr:nth-child(even) {
            background-color: #f9f9f9;
        }
        .footer {
            margin-top: 30px;
            font-size: 11px;
            color: gray;
            text-align: center;
        }
    </style>
    <script>
        function filterReports() {
            const input = document.getElementById("searchInput").value.toLowerCase();
            const rows = document.querySelectorAll("tbody tr");

            rows.forEach(row => {
                const cells = row.querySelectorAll("td");
                const match = Array.from(cells).some(td => td.textContent.toLowerCase().includes(input));
                row.style.display = match ? "" : "none";
            });
        }
    </script>
</head>
<body>
    <header>
        <img src="https://skillvenza.com/wp-content/uploads/2025/05/cropped-Logo-4-300x240.png" alt="SkillvenzA Logo">
        <h1>Incident Reports Dashboard</h1>
    </header>
    <div class="controls">
        <input type="text" id="searchInput" placeholder="Search reports..." onkeyup="filterReports()" />
        <a href="/export-csv" class="button" target="_blank">Download CSV</a>
        <a href="/export-pdf" class="button" target="_blank">Download PDF</a>
    </div>
    <table>
        <thead>
            <tr>
                <th>Timestamp</th>
                <th>Reporter</th>
                <th>Department</th>
                <th>Email/User</th>
                <th>Type</th>
                <th>Description</th>
            </tr>
        </thead>
        <tbody>
            {% for r in reports %}
            <tr>
                <td>{{ r.timestamp }}</td>
                <td>{{ r.reporter }}</td>
                <td>{{ r.department }}</td>
                <td>{{ r.email_or_user }}</td>
                <td>{{ r.incident_type }}</td>
                <td>{{ r.description }}</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
    <div class="footer">
        Dashboard generated {{ generated }}<br>
        Developed by SkillvenzA | www.skillvenza.com<br>
        &copy; 2025 SkillvenzA. All rights reserved.
    </div>
</body>
</html>
"""

@app.route("/")
def dashboard():
    if os.path.exists(REPORT_LOG):
        with open(REPORT_LOG) as f:
            data = json.load(f)
    else:
        data = []
    return render_template_string(HTML_TEMPLATE, reports=data, generated=datetime.now().strftime("%Y-%m-%d %H:%M"))

@app.route("/export-csv")
def export_csv():
    if os.path.exists(REPORT_LOG):
        with open(REPORT_LOG) as f:
            data = json.load(f)
    else:
        data = []

    si = StringIO()
    writer = csv.DictWriter(si, fieldnames=["timestamp", "reporter", "department", "email_or_user", "incident_type", "description"])
    writer.writeheader()
    for row in data:
        writer.writerow(row)

    output = make_response(si.getvalue())
    output.headers["Content-Disposition"] = "attachment; filename=incident_report_summary.csv"
    output.headers["Content-type"] = "text/csv"
    return output

@app.route("/export-pdf")
def export_pdf():
    if os.path.exists(REPORT_LOG):
        with open(REPORT_LOG) as f:
            logs = json.load(f)
    else:
        logs = []
    html_content = render_template_string(HTML_TEMPLATE, reports=logs, generated=datetime.now().strftime("%Y-%m-%d %H:%M"))
    HTML(string=html_content).write_pdf(PDF_EXPORT)
    return send_file(PDF_EXPORT, as_attachment=True)

if __name__ == "__main__":
    app.run(port=5086, debug=True)
