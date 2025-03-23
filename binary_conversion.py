import tkinter
from tkinter import ttk

# 급하게 작성하느라 자동완성의 도움을 많이 받았습니다... 죄송합니다 교수님

main_window = tkinter.Tk()
main_window.title("Binary Conversion")

tab = ttk.Notebook(main_window)

main_tab = ttk.Frame(tab)
tab.add(main_tab, text="Converter")

label0 = ttk.Label(main_tab, text="Select input binary: ")
label0.grid(row=0, column=0)

selection = ttk.Combobox(main_tab, values=["HEX(16)", "DEC(10)", "OCT(8)", "BIN(2)"])
selection.grid(row=0, column=1)

lable1 = ttk.Label(main_tab, text="Enter number:")
lable1.grid(row=1, column=0)

entry = ttk.Entry(main_tab)
entry.grid(row=1, column=1)

def division():
    custom_binary = selection.get()
    if custom_binary == "HEX(16)":
        Hex_converter(entry.get())
    elif custom_binary == "DEC(10)":
        Dec_converter(entry.get())
    elif custom_binary == "OCT(8)":
        Oct_converter(entry.get())
    elif custom_binary == "BIN(2)":
        Bin_converter(entry.get())
    else:
        Value_error()

convert_button = ttk.Button(main_tab, text="Convert", command = division)
convert_button.grid(row=2, column=0, columnspan=2)

result_label1 = ttk.Label(main_tab, text="16진수 ==>")
result_label1.grid(row=3, column=0, columnspan=2)

result_label2 = ttk.Label(main_tab, text="10진수 ==>")
result_label2.grid(row=4, column=0, columnspan=2)

result_label3 = ttk.Label(main_tab, text="8진수 ==>")
result_label3.grid(row=5, column=0, columnspan=2)

result_label4 = ttk.Label(main_tab, text="2진수 ==>")
result_label4.grid(row=6, column=0, columnspan=2)


def Hex_converter(hex_):
    try:
        dec_ = int(hex_, 16)
        hex_ = hex(dec_)
        oct_ = oct(dec_)
        bin_ = bin(dec_)
        result_label1.config(text="16진수 ==> "  + str(hex_))
        result_label2.config(text="10진수 ==> " + str(dec_))
        result_label3.config(text="8진수 ==> " + str(oct_))
        result_label4.config(text="2진수 ==> " + str(bin_))
    except ValueError:
        Value_error()


def Dec_converter(dec_):
    try:
        dec_ = int(dec_, 10)
        hex_ = hex(dec_)
        oct_ = oct(dec_)
        bin_ = bin(dec_)
        result_label1.config(text="16진수 ==> " + str(hex_))
        result_label2.config(text="10진수 ==> " + str(dec_))
        result_label3.config(text="8진수 ==> " + str(oct_))
        result_label4.config(text="2진수 ==> " + str(bin_))
    except ValueError:
        Value_error()

def Oct_converter(oct_):
    try:
        dec_ = int(oct_, 8)
        hex_ = hex(dec_)
        oct_ = oct(dec_)
        bin_ = bin(dec_)
        result_label1.config(text="16진수 ==> " + str(hex_))
        result_label2.config(text="10진수 ==> " + str(dec_))
        result_label3.config(text="8진수 ==> " + str(oct_))
        result_label4.config(text="2진수 ==> " + str(bin_))
    except ValueError:
        Value_error()

def Bin_converter(bin_):
    try:
        dec_ = int(bin_, 2)
        hex_ = hex(dec_)
        oct_ = oct(dec_)
        bin_ = bin(dec_)
        result_label1.config(text="16진수 ==> " + str(hex_))
        result_label2.config(text="10진수 ==> " + str(dec_))
        result_label3.config(text="8진수 ==> " + str(oct_))
        result_label4.config(text="2진수 ==> " + str(bin_))
    except ValueError:
        Value_error()

def Value_error():
    result_label1.config(text="16진수 ==> ")
    result_label2.config(text="10진수 ==> ")
    result_label3.config(text="8진수 ==> ")
    result_label4.config(text="2진수 ==> ")

selection.bind("<<ComboboxSelected>>", lambda event: division())

main_window.bind("<Return>", lambda event: division())

tab.pack(expand=1, fill="both")

main_window.mainloop()