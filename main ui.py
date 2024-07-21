import tkinter as tk
from tkinter import ttk
import subprocess
import cc_check
import cc_gen

def run_cc_check():
    cc_check.root = root
    cc_check.open_check_cc_ui()

def run_cc_gen():
    cc_gen.root = root
    cc_gen.open_gen_cc_ui()

root = tk.Tk()
root.title("Credit Card Generator / Checker")
root.geometry("600x400")

frame = ttk.Frame(root, padding="20")
frame.pack(fill="both", expand=True)

explanation_text = (
    "Welcome to the Credit Card Generator / Checker!\n\n"
    "This tool allows you to generate valid credit card numbers using the Luhn algorithm "
    "or check if a given credit card number is valid.\n\n"
    "To get started, choose one of the options below:\n"
    "- Click 'Check CC' to verify a credit card number.\n"
    "- Click 'Generate CC' to generate valid credit card numbers."
)

label = ttk.Label(frame, text=explanation_text, font=("Arial", 14), wraplength=550, justify="center")
label.pack(pady=20)

button_frame = ttk.Frame(frame)
button_frame.pack(pady=50)

button_style = ttk.Style()
button_style.configure('TButton', font=('Arial', 14), padding=(20, 10))

check_button = ttk.Button(button_frame, text="Check CC", command=run_cc_check, style='TButton')
check_button.pack(side="left", padx=30, ipadx=30, ipady=20)

generate_button = ttk.Button(button_frame, text="Generate CC", command=run_cc_gen, style='TButton')
generate_button.pack(side="right", padx=30, ipadx=30, ipady=20)

root.style = ttk.Style(root)
root.style.theme_use('clam')

root.mainloop()