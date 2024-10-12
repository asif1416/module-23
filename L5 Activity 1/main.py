# Import necessary libraries
from tkinter import *

# Setting up Main Window
root = Tk()
root.geometry("400x300")
root.title("Main Window")

# Function to open New (Top Level) Window
def topwin():
    # Setting up Top Window
    top = Toplevel()
    top.geometry("180x100")
    top.title("Top Level Window")
    # Adding a label widget to Top Window
    l2 = Label(top, text="This is the top-level window")
    l2.pack()

# Adding a label and button Widget to Root (Main) Window
l = Label(root, text="This is the root window")
btn = Button(root, text="Click here to open another window", command=topwin)

# Arranging widgets
l.pack(pady=10)
btn.pack(pady=10)

# Run the application
root.mainloop()
