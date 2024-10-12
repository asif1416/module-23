from tkinter import *

def calculate_interest():
    try:
        principal = float(principal_entry.get())
        time = float(time_entry.get())
        rate = float(rate_entry.get())

        simple_interest = (principal * rate * time) / 100

        compound_interest = principal * (1 + rate / 100) ** time - principal

        simple_interest_label.config(text=f"Simple Interest: {simple_interest:.2f}")
        compound_interest_label.config(text=f"Compound Interest: {compound_interest:.2f}")
    except ValueError:
        simple_interest_label.config(text="Enter valid numbers.")
        compound_interest_label.config(text="")

root = Tk()
root.title("Age Calculator App")
root.geometry("400x400")

frame = Frame(root)
frame.pack(pady=20)

Label(frame, text="Principal:").grid(row=0, column=0, padx=10, pady=10)
principal_entry = Entry(frame)
principal_entry.grid(row=0, column=1, padx=10, pady=10)

Label(frame, text="Time (years):").grid(row=1, column=0, padx=10, pady=10)
time_entry = Entry(frame)
time_entry.grid(row=1, column=1, padx=10, pady=10)

Label(frame, text="Rate (%):").grid(row=2, column=0, padx=10, pady=10)
rate_entry = Entry(frame)
rate_entry.grid(row=2, column=1, padx=10, pady=10)

# Calculate button
calculate_button = Button(root, text="Calculate", command=calculate_interest)
calculate_button.pack(pady=20)

# Result labels
simple_interest_label = Label(root, text="")
simple_interest_label.pack(pady=5)

compound_interest_label = Label(root, text="")
compound_interest_label.pack(pady=5)

root.mainloop()
