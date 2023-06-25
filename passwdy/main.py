from tkinter import *
import json
from tkinter import messagebox
from passwd_generator import generate_passwd

# pyperclip for clipboard


def find_passwd():
    input_web = web_entry.get()

    try:
        with open("./passwdy/dragon.json", mode="r") as info:
            data = json.load(info)
            result = data[input_web.capitalize()]

    except FileNotFoundError and KeyError:
        messagebox.showerror(
            title="Error", message="The provided website was not found!"
        )
    else:
        messagebox.showinfo(
            title=input_web,
            message=f"Username => {result['username']}\n\nPassword => {result['password']}",
        )


def save_details():
    web = web_entry.get().capitalize()
    password = passwd_entry.get()
    user = user_entry.get()

    if not input_is_valid(web, password, user):
        return

    all_fine = messagebox.askokcancel(
        title="Confirmation",
        message=f"Confirm the details...\nWebsite => {web}\nUsername => {user}\nPassword => {password}",
    )

    if not all_fine:
        return

    new_info = {web: {"password": password, "username": user}}

    try:
        with open("./passwdy/dragon.json", mode="r") as info:
            read_info = json.load(info)

    except FileNotFoundError:
        with open("./passwdy/dragon.json", mode="w") as info:
            json.dump(new_info, info, indent=2)

    else:
        read_info.update(new_info)
        with open("./passwdy/dragon.json", mode="w") as info:
            json.dump(read_info, info, indent=2)

    finally:
        for entry in [web_entry, user_entry, passwd_entry]:
            entry.delete(0, END)

        messagebox.showinfo(title="Success ✅", message="Information recorded.")


def input_is_valid(web, password, user):
    for value in [web, password, user]:
        if len(value) == 0:
            messagebox.showinfo(
                title="There now 🙂...", message="Ensure all fields are filled"
            )
            return False
    return True


def create_passwd():
    passwd_entry.insert(0, generate_passwd())


window = Tk()
window.title("Passwd-y")
window.config(padx=30, pady=30)

website = Label(text="Website:")
website.grid(row=0, column=0)
web_entry = Entry(width=21)
web_entry.focus()
web_entry.grid(row=0, column=1)

search = Button(text="Search", width=15, command=find_passwd)
search.grid(row=0, column=2)

user_name = Label(text="Username:")
user_name.grid(row=1, column=0)
user_entry = Entry(width=40)
user_entry.insert(0, "hassanshakur.dev@gmail.com")
user_entry.grid(row=1, column=1, columnspan=2)

passwd = Label(text="Password:")
passwd.grid(row=2, column=0)
passwd_entry = Entry(width=21)
passwd_entry.grid(row=2, column=1)

gen_passwd = Button(text="Generate Password", command=create_passwd)
gen_passwd.grid(row=2, column=2)

save = Button(text="Save", width=33, command=save_details)
save.grid(row=3, column=1, columnspan=2)


window.mainloop()
