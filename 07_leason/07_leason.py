'''
Seven lesson
Creating  Image Viewer App
'''

from tkinter import *
from tkinter import PhotoImage
from PIL import Image, ImageTk

root = Tk()

# for jpg
my_img1 = ImageTk.PhotoImage(Image.open('icon1.jpg'))
my_img2 = ImageTk.PhotoImage(Image.open('icon2.jpg'))
my_img3 = ImageTk.PhotoImage(Image.open('icon3.jpg'))
my_img4 = ImageTk.PhotoImage(Image.open('icon4.jpg'))

image_list = [my_img1, my_img2, my_img3, my_img4]

my_img = image_list[0]


label_img = Label(root, image=my_img)
label_img.grid(row=0, column=0, columnspan=3)


def forward(image_number):
    global label_img
    global button_next
    global button_back
    
    label_img.grid_forget()
    label_img = Label(root, image=image_list[image_number-1])
    button_next = Button(root, text=">>",command=lambda: forward(image_number+1))
    button_back = Button(root, text="<<",command=lambda: back(image_number-1))
    
    if image_number == len(image_list):
        button_next = Button(root, text=">>", state=DISABLED)
    
    label_img.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_next.grid(row=1, column=2)

def back(image_number):
    global label_img
    global button_next
    global button_back
    
    label_img.grid_forget()
    label_img = Label(root, image=my_img)
    label_img.grid(row=0, column=0, columnspan=3)
    
    label_img.grid_forget()
    label_img = Label(root, image=image_list[image_number-1])
    button_next = Button(root, text=">>",command=lambda: forward(image_number+1))
    button_back = Button(root, text="<<",command=lambda: back(image_number-1))
    if image_number == 1:
        button_back = Button(root, text="<<", state=DISABLED)
    
    label_img.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_next.grid(row=1, column=2)


button_back = Button(root, text="<<",command=lambda: back(2),state=DISABLED)
button_quit = Button(root, text="Exit", command=root.quit)
button_next = Button(root, text=">>",command=lambda: forward(2))

button_back.grid(row=1, column=0)
button_quit.grid(row=1, column=1)
button_next.grid(row=1, column=2)

root.mainloop()
