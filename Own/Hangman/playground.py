from tkinter import *

root = Tk()

e = Entry(root, width=50, borderwidth=5)
e.pack()
e.insert(0, "Enter Your letter")

def myClick():
    hello = "Your letter is: " + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()

myButton = Button(root, text="Enter Your Name!", command=myClick)
myButton.pack()

root.mainloop()

