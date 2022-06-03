from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

YELLOW = "#e7c36d"
BLUE = "#6d91e7"
WHITE = "#ffffff"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# Password Generator Project

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
           'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
           'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def gen_password():

    pass_entry.delete(0, END)

    letters_list = [choice(letters) for _ in range(randint(8, 10))]

    numbers_list = [choice(numbers) for _ in range(randint(2, 4))]

    symbols_list = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = letters_list + numbers_list + symbols_list

    shuffle(password_list)

    password = "".join(password_list)

    pass_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_data():

    website = website_entry.get()
    email_user = email_user_entry.get()
    password = pass_entry.get()

    if len(website) == 0 or len(email_user) == 0 or len(password) == 0:
        messagebox.showinfo(message="Please complete all fields")
    else:

        is_ok = messagebox.askokcancel(title=website, message=f"These are the details you have entered: "
                                                          f"\nWebsite: {website}"
                                                          f"\nEmail: {email_user} "
                                                          f"\nPassword: {password} "
                                                          f"\nClick ok to save")
        if is_ok:
            with open("pass_data.txt", "a") as f:
                f.write(f"{website} | {email_user} | {password} \n")

        pyperclip.copy(password)

        messagebox.showinfo(message="The last password has been copied to your clipboard.")

    website_entry.delete(0, END)
    pass_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Generator")
window.config(padx=40, pady=40, bg=BLUE)

canvas = Canvas(width=100, height=158, highlightthickness=0, bg=BLUE)
lock = PhotoImage(file='logo.gif')
canvas.create_image(50, 80, image=lock)
canvas.grid(column=0, row=0, columnspan=3, pady=(0, 10))

website_label = Label(text="website", font=("Arial", 14), bg=BLUE, fg=WHITE)
website_label.grid(column=0, row=1)

website_entry = Entry(width=38, highlightbackground=BLUE)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_user_label = Label(text="email/user name", font=("Arial", 14), bg=BLUE, fg=WHITE)
email_user_label.grid(column=0, row=2)

email_user_entry = Entry(width=38, highlightbackground=BLUE)
email_user_entry.grid(column=1, row=2, columnspan=2)
email_user_entry.insert(0, "")

pass_label = Label(text="password", font=("Arial", 14), bg=BLUE, fg=WHITE)
pass_label.grid(column=0, row=3)

pass_entry = Entry(width=17, highlightbackground=BLUE)
pass_entry.grid(column=1, row=3)

pass_generator = Button(text="Generate password", font=("Arial", 14), width=17, highlightbackground=BLUE,
                        command=gen_password)
pass_generator.grid(column=2, row=3)

add_button = Button(text="Add password", font=("Arial", 14), width=36, highlightbackground=BLUE,
                    command=add_data)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()