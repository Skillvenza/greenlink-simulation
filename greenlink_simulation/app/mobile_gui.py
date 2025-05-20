
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
from app.extract_engine import extract_payload

LOG_FILE = "app/simulation_log.txt"
IMAGE_PATH = "app/image_preview.png"

def log_user_action(message):
    from datetime import datetime
    with open(LOG_FILE, "a") as log:
        log.write(f"{datetime.now()} — {message}\n")

def simulate_click():
    response = messagebox.askyesno("Simulated Action", "Do you want to view the delivery status?")
    if response:
        log_user_action("User clicked the image.")
        extract_payload(IMAGE_PATH)
    else:
        log_user_action("User ignored the phishing attempt.")

def main():
    app = tk.Tk()
    app.title("GreenLink: WhatsApp Phishing Simulation")
    app.geometry("375x667")
    app.configure(bg="white")

    header = tk.Label(app, text="🚚 Missed Delivery Notice", font=("Helvetica", 20, "bold"), bg="white", fg="#b7410e")
    header.pack(pady=30)

    if os.path.exists(IMAGE_PATH):
        img = Image.open(IMAGE_PATH)
        img = img.resize((320, 240))
        img_display = ImageTk.PhotoImage(img)
        img_label = tk.Label(app, image=img_display)
        img_label.image = img_display
        img_label.pack()
    else:
        img_label = tk.Label(app, text="Image not found.", font=("Helvetica", 14), bg="white", fg="red")
        img_label.pack(pady=20)

    btn = tk.Button(app, text="Tap to View", command=simulate_click, bg="#0A84FF", fg="white", font=("Helvetica", 14), width=20, height=2)
    btn.pack(pady=50)

    app.mainloop()

if __name__ == "__main__":
    main()
