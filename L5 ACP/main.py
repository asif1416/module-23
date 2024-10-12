# Import necessary libraries
from tkinter import *

# Function to check password strength based on length
def check_strength():
    password = entry.get()
    length = len(password)
    
    if length <= 5:
        result_label.config(text="Weak", fg="Red")
    elif 6 <= length <= 8:
        result_label.config(text="Medium", fg="Yellow")
    elif 9 <= length <= 12:
        result_label.config(text="Strong", fg="Light Green")
    else:
        result_label.config(text="Very Strong", fg="Dark Green")

# Setting up Main Window
root = Tk()
root.geometry("400x400")
root.title("Length Converter App")

# Label to prompt user to enter a password
label = Label(root, text="Enter Password:")
label.pack(pady=20)

# Entry widget to input the password
entry = Entry(root, show="*")
entry.pack(pady=10)

# Button to trigger the password strength check
btn = Button(root, text="Check Strength", command=check_strength)
btn.pack(pady=10)

# Label to display the strength result
result_label = Label(root, text="", font=('Helvetica', 14))
result_label.pack(pady=20)

# Run the application
root.mainloop()
