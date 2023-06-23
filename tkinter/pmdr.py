from tkinter import *

window = Tk()
window.title("Pomodoro")
window.config(bg="white", padx=20, pady=20)

# Load image
canvas = Canvas(width=314, height=210, highlightthickness=0)
# home_img = PhotoImage(file="home.jpg")

# canvas.create_image(157, 105, image=home_img)
# canvas.pack()

# edit an item in the canvas
canvas.itemconfig('itemTarget', text="new val")


# Repeat an activity at an interval
def do_something(p1, p2):
    print(p1, p2)


window.after(1000, do_something, "param1", "param2")

window.mainloop()
