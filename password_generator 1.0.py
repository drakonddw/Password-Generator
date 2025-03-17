import random
import string
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")
root.resizable(False, False)

def generate_password():
    length = length_var.get()
    if length < 4:
        messagebox.showwarning("Warning", "Password length should be at least 4!")
        return
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    
    password_var.set(password)

# Label
tk.Label(root, text="Enter Password Length:", font=("Arial", 12)).pack(pady=10)

# Input Box
length_var = tk.IntVar(value=12)  # Default value
length_entry = tk.Entry(root, textvariable=length_var, font=("Arial", 12), width=5)
length_entry.pack()

# Generate Button
generate_btn = tk.Button(root, text="Generate Password", command=generate_password, font=("Arial", 12), bg="blue", fg="white")
generate_btn.pack(pady=10)

# Output Field
password_var = tk.StringVar()
password_entry = tk.Entry(root, textvariable=password_var, font=("Arial", 12), width=25, state="readonly")
password_entry.pack()

# Copy Button
def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(password_var.get())
    root.update()
    messagebox.showinfo("Copied", "Password copied to clipboard!")

copy_btn = tk.Button(root, text="Copy", command=copy_to_clipboard, font=("Arial", 12))
copy_btn.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
