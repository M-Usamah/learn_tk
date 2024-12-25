'''
Four lesson
Creating input fields
'''

from tkinter import *

root = Tk()

e = Entry(root)
e.pack()
e.insert(0, "Enter Your Name: ")

def myClicl():
    myLabel = Label(root, text=e.get())
    myLabel.pack()

myButton = Button(root, text="Click Me!",padx=50,pady=20,command=myClicl)
myButton.pack()

root.mainloop()
