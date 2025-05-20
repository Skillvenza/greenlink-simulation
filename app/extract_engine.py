
from stegano import lsb
import base64
import webbrowser
import os

def extract_payload(image_path):
    try:
        print(f"[*] Extracting payload from: {image_path}")
        encoded = lsb.reveal(image_path)
        if encoded:
            decoded = base64.b64decode(encoded).decode()
            print(f"[+] Decoded URL: {decoded}")
            webbrowser.open(decoded)
            log_event(f"Payload extracted and opened: {decoded}")
        else:
            print("[-] No payload found in the image.")
            log_event("Attempted extraction, but no payload found.")
    except Exception as e:
        print(f"[!] Extraction failed: {e}")
        log_event(f"Extraction failed with error: {e}")

def log_event(entry):
    from datetime import datetime
    log_file = "app/simulation_log.txt"
    with open(log_file, "a") as log:
        log.write(f"{datetime.now()} — {entry}\n")
