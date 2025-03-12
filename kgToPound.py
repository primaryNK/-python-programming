import tkinter
from tkinter import ttk
import time
import random

main_window = tkinter.Tk()
main_window.title("kg to pound")

tab = ttk.Notebook(main_window)

main_tab = ttk.Frame(tab)
tab.add(main_tab, text="kg to pound")

lable1 = ttk.Label(main_tab, text="Enter kg:")
lable1.grid(row=0, column=0)

entry = ttk.Entry(main_tab)
entry.grid(row=1, column=0)

label2 = ttk.Label(main_tab, text="result")
label2.grid(row=2, column=0, columnspan=2)

result_label = ttk.Label(main_tab, text="")
result_label.grid(row=3, column=0, columnspan=2)

def convert():
    input = entry.get()
    if input == "hi" or input == "hello":
        result_label.config(text="Hello")
        return
    elif input == "bye":
        main_window.destroy()
        return
    else:
        try:
            if random.randint(0, 5) == 0:
                result_label.config(text="WTF IS KILLOGRAM 🦅")
                return
            else:
                kg = float(input)
                pound = kg * 2.20462
                result_label.config(text=f"{pound:.2f} pounds")
                return
        except ValueError:
            result_label.config(text="Value Error")

convert_button = ttk.Button(main_tab, text="Convert", command=convert)
convert_button.grid(row=4, column=0, columnspan=2)

main_window.bind("<Return>", lambda event: convert())

tab.pack(expand=1, fill="both")

main_window.mainloop()