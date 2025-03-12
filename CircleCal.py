import tkinter
from tkinter import ttk
import math
import time

main_window = tkinter.Tk()
main_window.title("circle calculator")

tab = ttk.Notebook(main_window)

main_tab = ttk.Frame(tab)
tab.add(main_tab, text="CIIIRRRCLLLLEE")

lable1 = ttk.Label(main_tab, text="Enter radiation:")
lable1.grid(row=0, column=0)

entry = ttk.Entry(main_tab)
entry.grid(row=1, column=0)

label2 = ttk.Label(main_tab, text="circumference")
label2.grid(row=2, column=0, columnspan=2)

label3 = ttk.Label(main_tab, text="extent")
label3.grid(row=2, column=2, columnspan=2)

result_circumference_label = ttk.Label(main_tab, text="")
result_circumference_label.grid(row=3, column=0, columnspan=2)

result_extent_label = ttk.Label(main_tab, text="")
result_extent_label.grid(row=3, column=2, columnspan=2)

def convert():
    input = entry.get()
    if input == "hi" or input == "hello":
        result_circumference_label.config(text="Hello")
        return
    elif input == "bye":
        main_window.destroy()
        return
    else:
        try:
            radiation = float(input)
            circumference = radiation * math.pi * 2
            extent = radiation ** 2 * math.pi
            result_circumference_label.config(text=f"{circumference:.2f} ")
            result_extent_label.config(text=f"{extent:.2f} ")
            return

        except ValueError:
            entry.config(text="Value Error")

convert_button = ttk.Button(main_tab, text="Convert", command=convert)
convert_button.grid(row=4, column=0, columnspan=2)

main_window.bind("<Return>", lambda event: convert())

tab.pack(expand=1, fill="both")

main_window.mainloop()