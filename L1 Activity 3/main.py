from tkinter import *
from PIL import Image, ImageTk

window = Tk()
window.title('Image Display')
window.geometry('400x400')

limage = Image.open("L1 Activity 3/images.jpeg")

image_l = ImageTk.PhotoImage(limage)

label = Label(window, image=image_l, height=200, width=300)

button = Button(window, text="Click Here", bg="#BC544B")
textbox = Text(window)
textbox.insert(END, "This is how you do it!")

label.pack()
button.pack()
textbox.pack()

window.mainloop()
