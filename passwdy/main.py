from tkinter import *
from tkinter import messagebox
from passwd_generator import generate_passwd

# pyperclip for clipboard
# pass generator


def save_details():
    web = web_entry.get()
    password = passwd_entry.get()
    user = user_entry.get()

    validate_input(web, password, user)

    all_fine = messagebox.askokcancel(
        title="Confirmation",
        message=f"Confirm the details...\n\nWebsite => {web}\nUsername => {user}\nPassword => {password}",
    )

    if not all_fine:
        return

    with open("./passwdy/dragon.txt", mode="a") as info:
        info.write(f"{web} | {user} | {password}\n")

    for entry in [web_entry, user_entry, passwd_entry]:
        entry.delete(0, END)

    messagebox.showinfo(title="Success ✅", message="Information recorded.")


def validate_input(web, password, user):
    for value in [web, password, user]:
        if len(value) == 0:
            return messagebox.showinfo(
                title="There now 🙂...", message="Ensure all fields are filled"
            )


def create_passwd():
    passwd_entry.insert(0, generate_passwd())


window = Tk()
window.title("Passwd-y")
window.config(padx=30, pady=30)

website = Label(text="Website:")
website.grid(row=0, column=0)
web_entry = Entry(width=40)
web_entry.focus()
web_entry.grid(row=0, column=1, columnspan=2)

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
