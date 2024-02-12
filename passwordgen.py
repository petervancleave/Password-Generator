import tkinter as tk
from tkinter import StringVar
import random
import string

class PasswordGenerator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Password Generator")

        self.generated_passwords = []

        self.upper_var = tk.IntVar()
        self.number_var = tk.IntVar()
        self.symbol_var = tk.IntVar()
        self.length_var = StringVar()
        self.length_var.set("10")

        self.password_label = tk.Label(self.root, text="Generated Passwords:")
        self.password_label.pack()

        self.password_listbox = tk.Listbox(self.root, height=5, width=40)
        self.password_listbox.pack()

        self.upper_checkbox = tk.Checkbutton(self.root, text="Uppercase", variable=self.upper_var)
        self.upper_checkbox.pack()

        self.number_checkbox = tk.Checkbutton(self.root, text="Numbers", variable=self.number_var)
        self.number_checkbox.pack()

        self.symbol_checkbox = tk.Checkbutton(self.root, text="Symbols", variable=self.symbol_var)
        self.symbol_checkbox.pack()

        self.length_label = tk.Label(self.root, text="Password Length:")
        self.length_label.pack()

        self.length_slider = tk.Scale(self.root, from_=5, to=30, orient=tk.HORIZONTAL, variable=self.length_var,
                                      label="Length")
        self.length_slider.pack()

        self.generate_button = tk.Button(self.root, text="Generate Password", command=self.generate_password)
        self.generate_button.pack()

    def generate_password(self):
        characters = string.ascii_lowercase
        if self.upper_var.get():
            characters += string.ascii_uppercase
        if self.number_var.get():
            characters += string.digits
        if self.symbol_var.get():
            characters += string.punctuation

        length = int(self.length_var.get())
        password = ''.join(random.choice(characters) for _ in range(length))

        self.generated_passwords.append(password)
        if len(self.generated_passwords) > 5:
            self.generated_passwords.pop(0)

        self.update_password_list()

    def update_password_list(self):
        self.password_listbox.delete(0, tk.END)
        for password in reversed(self.generated_passwords):
            self.password_listbox.insert(tk.END, password)

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    password_generator = PasswordGenerator()
    password_generator.run()
