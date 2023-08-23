import tkinter as tk
from tkinter import ttk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("400x600")
        self.root.configure(bg="#F2F3F4")  # Change the background color

        self.equation_text = ""
        self.equation_label = tk.StringVar()

        self.create_display()
        self.create_buttons()

    def create_display(self):
        font_style = ("Arial", 24)
        display_frame = tk.Frame(self.root, bg="#F2F3F4")  # Change the background color
        display_frame.pack(pady=20)

        self.equation_label.set("")
        label = tk.Label(
            display_frame,
            textvariable=self.equation_label,
            font=font_style,
            bg="#F2F3F4",  # Change the background color
            fg="#333333",  # Change the text color
            anchor="e",
            padx=20,
            pady=10,
        )
        label.pack(fill="both")

    def button_press(self, num):
        self.equation_text += str(num)
        self.equation_label.set(self.equation_text)

    def clear(self):
        self.equation_label.set("")
        self.equation_text = ""

    def calculate_result(self):
        try:
            total = str(eval(self.equation_text))
            self.equation_label.set(total)
            self.equation_text = total
        except SyntaxError:
            self.equation_label.set("Syntax Error")
            self.equation_text = ""
        except ZeroDivisionError:
            self.equation_label.set("Division by Zero!")
            self.equation_text = ""

    def create_buttons(self):
        button_frame = tk.Frame(self.root, bg="#F2F3F4")  # Change the background color
        button_frame.pack(padx=20, pady=20)

        button_rows = [
            ["7", "8", "9", "+"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "*"],
            ["0", ".", "=", "/"],
        ]

        button_colors = {
            "7": "#3498DB",
            "8": "#3498DB",
            "9": "#3498DB",
            "/": "#E74C3C",
            "4": "#3498DB",
            "5": "#3498DB",
            "6": "#3498DB",
            "*": "#E74C3C",
            "1": "#3498DB",
            "2": "#3498DB",
            "3": "#3498DB",
            "-": "#E74C3C",
            "0": "#3498DB",
            ".": "#3498DB",
            "=": "#27AE60",
            "+": "#E74C3C",
        }

        for i, row in enumerate(button_rows):
            for j, button_text in enumerate(row):
                button_color = button_colors[button_text]
                button = tk.Button(
                    button_frame,
                    text=button_text,
                    font=("Arial", 18),
                    bg=button_color,
                    fg="white",
                    padx=20,
                    pady=20,
                    bd=0,
                    relief="flat",
                    command=lambda text=button_text: self.button_press(text)
                    if text != "="
                    else self.calculate_result(),
                )
                button.grid(row=i, column=j, padx=5, pady=5, sticky="nsew")

        for i in range(4):
            button_frame.rowconfigure(i, weight=1)
            button_frame.columnconfigure(i, weight=1)

        clear_button = tk.Button(
            self.root,
            text="Clear",
            font=("Arial", 18),
            bg="#E74C3C",
            fg="white",
            padx=20,
            pady=10,
            bd=0,
            relief="flat",
            command=self.clear,
        )
        clear_button.pack(fill="both")


if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
