
# GreenLink Simulation Platform

**Developed by SkillvenzA**  
Website: [www.skillvenza.com](https://www.skillvenza.com)

---

## 🎯 Purpose

GreenLink is an advanced, real-world cybersecurity simulation platform focused on phishing awareness, incident tracking, and red vs. blue team training.

---

## 📂 Project Structure

```
greenlink_simulation/
├── blue_team/
│   ├── incident_reports.json               # Stores all submitted incident reports
│   ├── reports_dashboard.py                # Unified dashboard (search, CSV, PDF)
│   ├── report_incident_form.py             # CLI-based report submission
│   ├── report_incident_form_web.py         # Web-based incident submission form
│   └── view_incident_reports.py (archived) # [Deleted in latest update]
├── red_team/
│   ├── steg_hide.py                        # Stego-based payload embedding
│   ├── payload_builder.py, qr_generator.py # [Optional tools]
├── phishing_server/
│   ├── app.py                              # Fake phishing landing page
│   ├── templates/thankyou.html             # Acknowledgement after capture
├── ai_agent/
│   ├── phishing_chat_agent.py              # Scripted phishing bot
│   └── phishing_chat_agent_gpt.py          # AI/GPT-simulated phishing convo
├── admin_dashboard/
│   ├── dashboard.py                        # Admin viewer for login logs
├── auth/
│   └── consent_form.txt                    # Authorization for simulation
├── assets/
│   └── UI elements, logos, media files
```

---

## 🧩 Key Functionalities

- **Web Dashboard**  
  View all reports, search them, export to CSV and PDF:  
  Run `reports_dashboard.py` → [http://localhost:5086](http://localhost:5086)

- **Incident Submission**  
  - CLI: `report_incident_form.py`  
  - Web: `report_incident_form_web.py`

- **Red Team Simulation**  
  - Hide payloads in images (`steg_hide.py`)
  - Host phishing pages with form captures

- **Blue Team Tools**  
  - Detect & view reports, log suspicious activity, simulate defense response

- **AI Simulations**  
  - Run human-like phishing conversations using preloaded GPT-styled agents

---

## 📦 Dependencies

Install with:
```bash
pip install Flask WeasyPrint
```

Optional:
```bash
pip install openai  # if GPT integration is activated
```

---

## 🧑‍💻 Credits

Developed by **SkillvenzA**  
© 2025 SkillvenzA. All rights reserved.  
For enterprise solutions and licenses, visit [www.skillvenza.com](https://www.skillvenza.com)

