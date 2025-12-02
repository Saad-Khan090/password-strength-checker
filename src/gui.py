import os
import sys
import random
import string

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

import tkinter.messagebox as messagebox
import customtkinter as ctk
from src.checker import check_password_strength
from src.rules import rule_get_missing



def main():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("green")


    root = ctk.CTk()
    root.title("Password Strength Checker")
    root.geometry("400x350")

    label = ctk.CTkLabel(root, text="Enter password:", font=("Arial", 18))
    label.pack(pady=10)

    entry = ctk.CTkEntry(root, width=250, placeholder_text="Type here...", show="*")
    entry.pack(pady=5)

    result_label = ctk.CTkLabel(root, text="", font=("Arial", 16))
    result_label.pack(pady=10)

    missing_label = ctk.CTkLabel(root, text="", font=("Arial", 14))
    missing_label.pack()

    def toggle_password():
        if entry.cget("show") == "*":
            entry.configure(show="") #show acctual text
            toggle_btn.configure(text="Hide 🙈")
        else:
            entry.configure(show="*") #hide text
            toggle_btn.configure(text="Show 👁️")
    toggle_btn = ctk.CTkButton(root, text="Show 👁️", width=120,font=("Arial", 16), command=toggle_password)
    toggle_btn.pack(pady=5)

    def copy_password():
        password = entry.get()
        if not password:
            messagebox.showwarning('warning: ', "Enter password first! ")
            return
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("copied","password copied to clipboard!")
    copy_btn = ctk.CTkButton(root, text="Copy 📋",font=("Arial", 16), width=120, command=copy_password)
    copy_btn.pack(pady=5)
    
    def generate_password():
        length = 12
        # Must include character
        lower = random.choice(string.ascii_lowercase)
        upper = random.choice(string.ascii_uppercase)
        digit = random.choice(string.digits)
        symbol = random.choice(string.punctuation)

        remaining = length - 4
        all_char = string.ascii_letters + string.digits + string.punctuation
        password_list = [lower, upper, digit, symbol]+[random.choice(all_char) for _ in range(remaining)]
        random.shuffle(password_list)
        password = "".join(password_list)
        entry.delete(0, "end")
        entry.insert(0, password)

        update_live(None)
    generate_btn = ctk.CTkButton(root, text="Generate 🔄",font=('Arial',16), width=120, command=generate_password)
    generate_btn.pack(pady=5)

    def update_live(event):
        password = entry.get()
    
        if not password:
            result_label.configure(text="")
            missing_label.configure(text="")
            return
        status = check_password_strength(password)
        missing = rule_get_missing(password)
        if status == "Very Strong":
            color = "green"
        elif status == "Strong":
            color = "blue"
        elif status == "Medium":
            color = "orange"
        else:
            color = "red"
        result_label.configure(text=f"Password Strength: {status}", text_color= color)
        if missing:
            missing_label.configure(text="Missing:\n"+"\n".join(missing))
        else:
            missing_label.configure(text="")
    entry.bind("<KeyRelease>", update_live)  # type: ignore

    root.mainloop()


if __name__ == '__main__':
    main()
