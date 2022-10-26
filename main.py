from random import randint, shuffle, choice
import tkinter
from tkinter import messagebox
import pyperclip

PINK = "#e2979c"
RED = "#FF1E1E"
GREEN = "#54B435"
TEAL = "#00FFD1"
ORANGE = "#F77E21"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    l_arr = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q"]
    n_arr = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    s_arr = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "+"]

    password_letters = [choice(l_arr) for _ in range(randint(8, 10))]
    password_numbers = [choice(n_arr) for _ in range(randint(2, 4))]
    password_symbols = [choice(s_arr) for _ in range(randint(2, 4))]

    password_arr = password_letters + password_symbols + password_numbers
    shuffle(password_arr)

    new_password = "".join(password_arr)

    password_input.delete(0, tkinter.END)
    password_input.insert(0, new_password)
    pyperclip.copy(new_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website_value = website_input.get()
    email_value = email_input.get()
    password_value = password_input.get()

    if len(website_value) == 0 or password_value == 0:
        messagebox.showwarning(title="Oops", message="You've left some fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website_value,
                                       message=f"These are the details you entered: \nEmail: {email_value}\nPassword: {password_value}\nIs it ok to save?")

        if is_ok:
            with open("data.txt", mode="a") as file:
                data_to_add = f"{website_value} | {email_value} | {password_value}\n"
                file.write(data_to_add)

            website_input.delete(0, tkinter.END)
            password_input.delete(0, tkinter.END)
            messagebox.showinfo(title="Success", message="Your details have been added successfully")


# ---------------------------- UI SETUP ------------------------------- #
screen = tkinter.Tk()
screen.title("Password Manager")
screen.minsize(width=300, height=300)
screen.config(pady=20, padx=20)

canvas = tkinter.Canvas(width=200, height=200)
image = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)

website_label = tkinter.Label(text="Website: ")
website_label.grid(row=1, column=0)

website_input = tkinter.Entry(width=35)
website_input.focus()
website_input.grid(row=1, column=1, columnspan=2)

email_label = tkinter.Label(text="Email/Username: ")
email_label.grid(row=2, column=0)

email_input = tkinter.Entry(width=35)
email_input.grid(row=2, column=1, columnspan=2)

password_label = tkinter.Label(text="Password: ")
password_label.grid(row=3, column=0)

password_input = tkinter.Entry(width=21)
password_input.grid(row=3, column=1)

generate_btn = tkinter.Button(text="Generate Password", command=generate_password, bg=PINK)
generate_btn.grid(row=3, column=2)

add_btn = tkinter.Button(text="Add", width=36, command=save_password, bg=GREEN)
add_btn.grid(row=4, column=1, columnspan=2)

screen.mainloop()
