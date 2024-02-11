import random
import tkinter as tk
from tkinter import messagebox


def main():
    # Password generator
    def generate_password():
        password_entry.delete(0, tk.END)
        password = ""
        for _ in range(24):
            password += random.choice([
                chr(random.randint(65, 90)),
                chr(random.randint(97, 122)),
                str(random.randint(0, 9)),
                random.choice(
                    ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "=", "-", "<", ">", "?", "/", "|", "~",
                     "`"])
            ])
        password_entry.insert(0, password)
        password_entry.clipboard_clear()
        password_entry.clipboard_append(password)

        messagebox_gen = tk.messagebox
        messagebox_gen.showinfo("Password", "Password copied to clipboard")

    # Save password
    def save_password():
        messagebox_ask = tk.messagebox
        check = messagebox_ask.askokcancel("Password", "Do you want to save the password? (yes/no)"
                                                       "\n\nNote: Password will be saved in plain text."
                                                       "\nIt is recommended to use a proper password manager.")

        if check:
            if website_entry.get() == "" or email_entry.get() == "" or password_entry.get() == "":
                messagebox_save = tk.messagebox
                messagebox_save.showinfo("Password", "Please fill all the fields")
                return
            else:
                with open("day-29-passwords.txt", "a") as file:
                    file.write(f"{website_entry.get()} | {email_entry.get()} | {password_entry.get()}\n")
                website_entry.delete(0, tk.END)
                password_entry.delete(0, tk.END)

                messagebox_save = tk.messagebox
                messagebox_save.showinfo("Password", "Password saved")

    # Find password
    def find_password():
        with open("day-29-passwords.txt", "r") as file:
            for line in file:
                if website_entry.get() in line:
                    email, password = line.split(" | ")[1], line.split(" | ")[2]
                    email_entry.delete(0, tk.END)
                    email_entry.insert(0, email)
                    password_entry.delete(0, tk.END)
                    password_entry.insert(0, password)

                    messagebox_find = tk.messagebox
                    messagebox_find.showinfo("Password", f"Email: {email}\nPassword: {password}")
                    break
                else:
                    messagebox_find = tk.messagebox
                    messagebox_find.showinfo("Password", "Password not found")

    # UI setup
    window = tk.Tk()
    window.title("Password Manager")
    window.config(padx=30, pady=30)
    canvas = tk.Canvas(width=200, height=200)
    canvas.grid(row=0, column=1)

    # Logo
    logo = tk.PhotoImage(file="day-29-logo.png")
    logo_label = tk.Label(image=logo)
    logo_label.grid(row=0, column=1)

    # Labels
    website_label = tk.Label(text="Website:")
    website_label.grid(row=1, column=0)
    email_label = tk.Label(text="Email/Username:")
    email_label.grid(row=2, column=0)
    password_label = tk.Label(text="Password:")
    password_label.grid(row=3, column=0)

    # Entries
    website_entry = tk.Entry(width=35)
    website_entry.grid(row=1, column=1, columnspan=2)
    website_entry.focus()
    email_entry = tk.Entry(width=35)
    email_entry.grid(row=2, column=1, columnspan=2)
    password_entry = tk.Entry(width=35)
    password_entry.grid(row=3, column=1, columnspan=2)

    # Buttons
    generate_button = tk.Button(text="Generate Password", command=generate_password)
    generate_button.grid(row=3, column=2)
    add_button = tk.Button(text="Add", width=30, command=save_password)
    add_button.grid(row=4, column=1, columnspan=2)
    search_button = tk.Button(text="Search", width=15, command=find_password)
    search_button.grid(row=1, column=2)

    window.mainloop()


if __name__ == "__main__":
    main()
