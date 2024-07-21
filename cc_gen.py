import tkinter as tk
from tkinter import ttk
import random

def luhn_checksum(card_number):
    def digits_of(n):
        return [int(d) for d in str(n)]
    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d*2))
    return checksum % 10

def is_luhn_valid(card_number):
    return luhn_checksum(card_number) == 0

def generate_valid_credit_card():
    while True:
        card_number = [random.randint(0, 9) for _ in range(15)]
        card_number.append(0)
        checksum = luhn_checksum(int(''.join(map(str, card_number))))
        card_number[-1] = (10 - checksum) % 10
        card_number_str = ''.join(map(str, card_number))
        if is_luhn_valid(card_number_str):
            return card_number_str

def generate_cards():
    text_area.delete('1.0', tk.END)
    cards = [generate_valid_credit_card() for _ in range(20)]
    formatted_cards = ["{} {} {} {}".format(card[:4], card[4:8], card[8:12], card[12:]) for card in cards]
    for card in formatted_cards:
        text_area.insert(tk.END, card + "\n")
        text_area.tag_add("center", "1.0", "end")

def open_gen_cc_ui():
    global text_area

    gen_window = tk.Toplevel(root)
    gen_window.title("Credit Card Generator")
    gen_window.geometry("400x570")

    frame = ttk.Frame(gen_window, padding="20")
    frame.pack(fill="both", expand=True)

    text_area = tk.Text(frame, wrap="word", font=("Arial", 12), height=10, width=50)
    text_area.pack(pady=10, expand=True, fill="both")
    text_area.tag_configure("center", justify='center')

    generate_button = ttk.Button(frame, text="Generate", command=generate_cards)
    generate_button.pack(pady=20)

root = None
text_area = None