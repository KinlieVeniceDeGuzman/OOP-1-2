# Problem 2

from tkinter import *

window = Tk()

window.title("Special Midterm Exam in OOP")
window.geometry("500x400+20+10")

def activebackground():
    btn.configure(bg="yellow", fg="black")

# Insert button widget
btn = Button(window, text = "Click to Change Color", command=activebackground)
btn.place(x=190, y=170)


window.mainloop()