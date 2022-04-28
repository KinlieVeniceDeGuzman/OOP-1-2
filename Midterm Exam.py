from tkinter import *
from tkinter import ttk
def demoColorChange(): btn.configure(bg="yellow", fg="black")
window = Tk()

window.title("Special Midterm Exam in OOP")
window.geometry("500x400+20+10")

# Insert button widget
btn = Button(window, text = "Click to Change Color", command=demoColorChange)
btn.place(x=190, y=170)


window.mainloop()