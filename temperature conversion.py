import tkinter as tk

def celsius_to_fahrenheit():
    celsius = float(celsius_entry.get())
    fahrenheit = (celsius * 9/5) + 32
    result_label.config(text=f"Fahrenheit: {fahrenheit:.2f}°F")

def fahrenheit_to_celsius():
    fahrenheit = float(fahrenheit_entry.get())
    celsius = (fahrenheit - 32) * 5/9
    result_label.config(text=f"Celsius: {celsius:.2f}°C")

def option1():
    result_label.config(text="You Selected Celsius to Fahrenheit")
    celsius_label = tk.Label(root, text="Enter Celsius:")
    celsius_label.pack()

    global celsius_entry
    celsius_entry = tk.Entry(root)
    celsius_entry.pack()

    celsius_to_fahrenheit_button = tk.Button(root, text="Convert to Fahrenheit", command=celsius_to_fahrenheit)
    celsius_to_fahrenheit_button.pack()

def option2():
    result_label.config(text="You selected Fahrenheit to Celsius")
    fahrenheit_label = tk.Label(root, text="Enter Fahrenheit:")
    fahrenheit_label.pack()

    global fahrenheit_entry
    fahrenheit_entry = tk.Entry(root)
    fahrenheit_entry.pack()

    fahrenheit_to_celsius_button = tk.Button(root, text="Convert to Celsius", command=fahrenheit_to_celsius)
    fahrenheit_to_celsius_button.pack()

root = tk.Tk()
root.title("Temperature Converter")
result_label = tk.Label(root, text="")
result_label.pack()

button1 = tk.Button(root, text="Celsius to Fahrenheit", command=option1)
button2 = tk.Button(root, text="Fahrenheit to Celsius", command=option2)
button1.pack()
button2.pack()


root.mainloop()