import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password():
    length = length_var.get()
    complexity = complexity_var.get()

    if not length.isdigit() or int(length) <= 0:
        messagebox.showerror("Invalid Input", "Please enter a valid positive integer for password length.")
        return

    length = int(length)

    if complexity == "Simple":
        characters = string.ascii_letters
    elif complexity == "Medium":
        characters = string.ascii_letters + string.digits
    else:
        characters = string.ascii_letters + string.digits + string.punctuation

    password = "".join(random.choice(characters) for _ in range(length))
    password_var.set(password)

def copy_to_clipboard():
    password = password_var.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")

def reset_password():
    password_var.set("")
    length_var.set("")
    complexity_var.set("Simple")  # Reset complexity to default

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x400")
root.configure(bg="#fffbf0")  # Change the background color for the root window to cream white

frame = tk.Frame(root, bg="#fffbf0")  # Change background color for the frame to cream white
frame.pack(pady=20)

greeting_label = tk.Label(frame, text="Random Password Generator", font=("Arial", 14, "bold"), bg="#fffbf0", fg="#333333")  # Change background color, font style, and text color
greeting_label.grid(row=0, columnspan=2)

tk.Label(frame, text="Password Length:", bg="#fffbf0", fg="#333333").grid(row=1, column=0)
length_var = tk.StringVar()
length_entry = tk.Entry(frame, textvariable=length_var, width=10)
length_entry.grid(row=1, column=1)

tk.Label(frame, text="Complexity:", bg="#fffbf0", fg="#333333").grid(row=2, column=0)
complexity_options = ["Simple", "Medium", "Strong"]
complexity_var = tk.StringVar()
complexity_menu = tk.OptionMenu(frame, complexity_var, *complexity_options)
complexity_menu.grid(row=2, column=1)

generate_button = tk.Button(root, text="Generate Password", command=generate_password, bg="#e84118", fg="white",
                            width=15, height=2, font=("Verdana", 12, "bold"))  # Change button size, font style, and colors
generate_button.pack()

password_frame = tk.Frame(root, bg="#fffbf0")
password_frame.pack(pady=10)

password_label = tk.Label(password_frame, text="Your Password:", bg="#fffbf0", fg="#333333")
password_label.pack()
password_var = tk.StringVar()
password_display = tk.Label(password_frame, textvariable=password_var, bg="#fffbf0", font=("Courier New", 12, "bold"), fg="#333333")  # Change font style and text color
password_display.pack(pady=5)

copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, bg="#0097e6", fg="white",
                        width=15, height=2, font=("Verdana", 12, "bold"))  # Change button size, font style, and colors
copy_button.pack()

reset_button = tk.Button(root, text="Reset", command=reset_password, bg="#dcdde1", fg="black",
                        width=15, height=2, font=("Verdana", 12, "bold"))  # Change button size, font style, and colors
reset_button.pack()

root.mainloop()
