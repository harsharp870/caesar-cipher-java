import customtkinter as ctk
from tkinter import messagebox

# Theme settings
ctk.set_appearance_mode("white")
ctk.set_default_color_theme("red")

# Caesar Cipher Logic
def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

# Process input
def process_text():
    message = input_box.get("1.0", "end").strip()

    if not message or message == placeholder:
        messagebox.showerror("Error", "Please enter a valid message!")
        return

    try:
        shift = int(shift_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Shift must be a number!")
        return

    if mode.get() == "Encrypt":
        result = encrypt(message, shift)
    else:
        result = decrypt(message, shift)

    output_box.delete("1.0", "end")
    output_box.insert("1.0", result)

# Copy to clipboard
def copy_text():
    result = output_box.get("1.0", "end").strip()
    if not result:
        messagebox.showerror("Error", "Nothing to copy!")
        return

    app.clipboard_clear()
    app.clipboard_append(result)
    messagebox.showinfo("Copied", "Text copied successfully!")

# Placeholder handling
def add_placeholder():
    if input_box.get("1.0", "end").strip() == "":
        input_box.insert("1.0", placeholder)
        input_box.configure(text_color="gray")

def remove_placeholder(event):
    if input_box.get("1.0", "end").strip() == placeholder:
        input_box.delete("1.0", "end")
        input_box.configure(text_color="white")

# App UI
app = ctk.CTk()
app.title("Caesar Cipher Tool")
app.geometry("500x520")

# Title
title = ctk.CTkLabel(app, text="Caesar Cipher Tool", font=("Arial", 22, "bold"))
title.pack(pady=15)

# Input box
input_box = ctk.CTkTextbox(app, height=100, width=420)
input_box.pack(pady=10)

placeholder = "Enter your message here..."
add_placeholder()

input_box.bind("<FocusIn>", remove_placeholder)
input_box.bind("<FocusOut>", lambda e: add_placeholder())

# Shift input
shift_entry = ctk.CTkEntry(app, placeholder_text="Enter shift value")
shift_entry.pack(pady=10)

# Mode selection
mode = ctk.StringVar(value="Encrypt")

frame = ctk.CTkFrame(app)
frame.pack(pady=10)

ctk.CTkRadioButton(frame, text="Encrypt", variable=mode, value="Encrypt").pack(side="left", padx=10)
ctk.CTkRadioButton(frame, text="Decrypt", variable=mode, value="Decrypt").pack(side="left", padx=10)

# Buttons
btn_frame = ctk.CTkFrame(app)
btn_frame.pack(pady=15)

process_btn = ctk.CTkButton(btn_frame, text="Process", command=process_text)
process_btn.pack(side="left", padx=10)

copy_btn = ctk.CTkButton(btn_frame, text="Copy", command=copy_text)
copy_btn.pack(side="left", padx=10)

# Output box
output_box = ctk.CTkTextbox(app, height=100, width=420)
output_box.pack(pady=10)

# Run
app.mainloop()
