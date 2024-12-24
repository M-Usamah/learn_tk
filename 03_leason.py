'''
third lesson
Creating Buttons
'''

from tkinter import *

root = Tk()

def myClicl():
    myLabel = Label(root, text="Look! I clicked a Button!")
    myLabel.pack()

myButton = Button(root, text="Click Me!",padx=50,pady=20,command=myClicl)
myButton.pack()
root.mainloop()
