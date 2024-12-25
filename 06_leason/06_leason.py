'''
Six lesson
Creating images, Icons, Exit
'''

from tkinter import *
from tkinter import PhotoImage
from PIL import Image, ImageTk

root = Tk()
# root.iconbitmap('icon.png') # for windows
root.iconbitmap('@icon.xbm') # for linux
e = Entry(root)
"""
# only work with png not with jpg
image = PhotoImage(file='icon.png')
label_img = Label(root, image=image)
label_img.pack()
"""

# for jpg
my_img = ImageTk.PhotoImage(Image.open('icon.jpg'))
label_img = Label(root, image=my_img)
label_img.pack()


button_quit = Button(root, text="Exit", command=root.quit)
button_quit.pack()

root.mainloop()
