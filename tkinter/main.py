from tkinter import *

# Window
window = Tk()
window.title("Tk Basics")
window.minsize(width=300, height=200)

# Padding
window.config(padx=10, pady=10)

# Label
label = Label(text="Han", font=("Arial", 10, "italic"))
label.pack()


# Button
def btn_click_handler():
    # Edit text in a label with the value from the input.get()
    label.config(text=input.get())


# Event listner using command
btn = Button(text="Click", command=btn_click_handler)
btn.pack()

# Imput
input = Entry(width=20)

# Include placeholder value
input.insert(END, "Placeholder")
input.pack()

# Textbox
txt_box = Text(width=30, height=4)
txt_box.focus()

# Get text in text box from line 1, char 0 to the end
txt_box.get("1.0", END)
txt_box.pack()

# Num input
spinbox = Spinbox(from_=0, to=20, width=10)
spinbox.pack()

# Scale
scale = Scale(from_=0, to=100)
scale.pack()

# Checkbox
is_checked = IntVar()
checkbx = Checkbutton(text="Agree?", variable=is_checked)

# Get checked state
is_checked.get()
checkbx.pack()


window.mainloop()
