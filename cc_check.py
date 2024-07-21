import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def valid_card(card):
    card_number = card.replace(' ', '')
    digits = [int(digit) for digit in card_number]

    for i in range(len(digits) - 2, -1, -2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] -= 9

    total = sum(digits)
    return total % 10 == 0

def check_card():
    card_number = entry.get()
    if valid_card(card_number):
        messagebox.showinfo("Result", "The credit card number is valid.")
    else:
        messagebox.showinfo("Result", "The credit card number is not valid.")

def open_check_cc_ui():
    check_window = tk.Toplevel(root)
    check_window.title("Credit Card Checker")
    check_window.geometry("400x200")

    frame = ttk.Frame(check_window, padding='20')
    frame.pack(fill="both", expand=True)

    label = ttk.Label(frame, text="Enter credit card number:", font=("Arial", 14))
    label.pack(pady=10)

    global entry
    entry = ttk.Entry(frame, width=30, font=("Arial", 12))
    entry.pack(pady=10)

    button = ttk.Button(frame, text="Check", command=check_card)
    button.pack(pady=20)

root = None
entry = None