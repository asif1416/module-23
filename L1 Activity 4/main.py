from tkinter import *

# Create Window
root = Tk()
root.title('Getting Started with Widgets')
root.geometry('400x300')

# Add widgets
# Add Labels
lbl1 = Label(root, text="Full Name", bg="#3895D3", fg='white')
lbl2 = Label(root, text="Email Id", bg="#3895D3", fg='white')
lbl3 = Label(root, text="Enter Password", bg="#3895D3", fg='white')

# Use Entry Widget to create a text box for user to enter details
name_entry = Entry(root)
email_entry = Entry(root)
pass_entry = Entry(root, show="*")

# Function to display message
def display():
    name = name_entry.get()
    greet = "Hey " + name
    message = "\nCongratulations on your new account!"
    
    # Clear the textbox before inserting new message
    textbox.delete(1.0, END)
    
    textbox.insert(END, greet)
    textbox.insert(END, message)

# Textbox to display message
textbox = Text(root, bg="#BEBEBE", fg="black", height=5, width=40)

# Add Button, when pressed, message will be displayed
btn = Button(root, text="Create Account", command=display)

# Arrange all widgets with padding
lbl1.pack(pady=(10, 0))  # Top padding
name_entry.pack(pady=5)
lbl2.pack(pady=(10, 0))
email_entry.pack(pady=5)
lbl3.pack(pady=(10, 0))
pass_entry.pack(pady=5)
btn.pack(pady=(10, 5))  # Bottom padding
textbox.pack(pady=(10, 10))  # Add padding around the textbox

# Run the Tkinter event loop
root.mainloop()
