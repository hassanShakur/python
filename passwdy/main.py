from tkinter import *


def collect_details():
    with open("./passwdy/dragon.txt", mode="a") as info:
        info.write(f"{web_entry.get()} | {user_entry.get()} | {passwd_entry.get()}\n")

    for entry in [web_entry, user_entry, passwd_entry]:
        entry.delete(0, END)


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

gen_passwd = Button(text="Generate Password")
gen_passwd.grid(row=2, column=2)

save = Button(text="Save", width=33, command=collect_details)
save.grid(row=3, column=1, columnspan=2)


window.mainloop()
