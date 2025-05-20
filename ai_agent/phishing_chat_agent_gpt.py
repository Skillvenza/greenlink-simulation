import os
import json
from datetime import datetime

chat_log_file = "ai_agent/ai_chat_log.json"

def ensure_log_file_exists():
    os.makedirs(os.path.dirname(chat_log_file), exist_ok=True)
    if not os.path.exists(chat_log_file):
        with open(chat_log_file, "w") as f:
            json.dump([], f)

def log_conversation(role, message):
    ensure_log_file_exists()
    timestamp = datetime.now().isoformat()
    entry = {"timestamp": timestamp, "role": role, "message": message}
    with open(chat_log_file, "r+") as f:
        data = json.load(f)
        data.append(entry)
        f.seek(0)
        json.dump(data, f, indent=4)

def mock_chatgpt_response(user_input):
    phishing_prompts = [
        "I understand. Just to confirm your bonus, click this HR link: http://127.0.0.1:5000",
        "Thanks for reaching out. We need to verify your credentials at this secure portal: http://127.0.0.1:5000",
        "No problem! For payroll updates, please log in using the HR gateway here: http://127.0.0.1:5000"
    ]
    return phishing_prompts[len(user_input) % len(phishing_prompts)]

def simulate_gpt_chat():
    print("--- ChatGPT-Simulated Phishing Chat ---")
    print("Attacker (AI): Hello, this is Sara from HR. We’re updating records for bonus allocation. How can I help you today?")
    log_conversation("attacker", "Hello, this is Sara from HR. We’re updating records for bonus allocation. How can I help you today?")

    while True:
        user_input = input("You: ")
        log_conversation("user", user_input)
        if user_input.lower() in ['exit', 'quit', 'no thanks']:
            response = "Alright, feel free to contact HR if you change your mind."
            print(f"Attacker (AI): {response}")
            log_conversation("attacker", response)
            break
        ai_response = mock_chatgpt_response(user_input)
        print(f"Attacker (AI): {ai_response}")
        log_conversation("attacker", ai_response)

if __name__ == "__main__":
    simulate_gpt_chat()
