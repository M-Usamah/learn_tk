'''
Nine lesson
Creating  Farmes
'''

from tkinter import *
from PIL import Image, ImageTk

root = Tk()
frame = LabelFrame(root,  padx=50, pady=50)
button1 = Button(frame, text="Don't Click Here!")
button2 = Button(frame, text="Don't Click Here!")
frame.pack(padx=10, pady=10)
button1.grid(row=0, column=0)
button2.grid(row=1, column=1)

root.mainloop()