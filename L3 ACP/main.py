from tkinter import *

def convert_length():
    try:
        length = float(length_entry.get())
        from_unit = from_unit_var.get()
        to_unit = to_unit_var.get()

        conversions = {
            "Meters": 1,
            "Kilometers": 1000,
            "Feet": 0.3048,
            "Miles": 1609.34,
        }

        result = length * conversions[from_unit] / conversions[to_unit]
        result_label.config(text=f"Converted Length: {result:.2f} {to_unit}")
    except ValueError:
        result_label.config(text="Enter a valid number.")

root = Tk()
root.title("Length Converter App")
root.geometry("400x400")

Label(root, text="Enter Length:").pack(pady=5)
length_entry = Entry(root)
length_entry.pack(pady=5)

from_unit_var = StringVar(value="Meters")
to_unit_var = StringVar(value="Meters")

Label(root, text="From Unit:").pack(pady=5)
OptionMenu(root, from_unit_var, "Meters", "Kilometers", "Feet", "Miles").pack(pady=5)

Label(root, text="To Unit:").pack(pady=5)
OptionMenu(root, to_unit_var, "Meters", "Kilometers", "Feet", "Miles").pack(pady=5)

Button(root, text="Convert", command=convert_length).pack(pady=10)

result_label = Label(root, text="")
result_label.pack(pady=5)

root.mainloop()
