import tkinter

window = tkinter.Tk()
window.title("Tk Basics")
window.minsize(width=300, height=200)

label = tkinter.Label(text="Han", font=("Arial", 10, "italic"))
label.pack()

window.mainloop()
