import tkinter
from tkinter import ttk
import re

main_window = tkinter.Tk()
main_window.title("Gauss Addition")

tab = ttk.Notebook(main_window)

main_tab = ttk.Frame(tab)
tab.add(main_tab, text="Gauss Addition")

label1 =  ttk.Label(main_tab, text="Select input: ")
label1.grid(row=0, column=0)

selection = ttk.Combobox(main_tab, values=["입력한 수식 계산", "입력한 두 수 사이의 합계"])
selection.grid(row=0, column=1)

label2 = ttk.Label(main_tab, text="수식을 입력하세요: ")
entry1 = ttk.Entry(main_tab)
label3 = ttk.Label(main_tab, text="첫번째 숫자를 입력하세요: ")
entry2 = ttk.Entry(main_tab)
label4 = ttk.Label(main_tab, text="두번째 숫자를 입력하세요: ")
entry3 = ttk.Entry(main_tab)
result_label = ttk.Label(main_tab, text="")
result_label.grid(row=4, column=0, columnspan=2)

def select():
    selected = selection.get()
    if selected == "입력한 수식 계산":        
        label3.grid_forget()
        entry2.grid_forget()
        label4.grid_forget()
        entry3.grid_forget()
        result_label.config(text="")
        label2.grid(row=2, column=0)
        entry1.grid(row=2, column=1)
        
    elif selected == "입력한 두 수 사이의 합계":
        label2.grid_forget()
        entry1.grid_forget()
        result_label.config(text="")
        label3.grid(row=2, column=0)
        entry2.grid(row=2, column=1)
        label4.grid(row=3, column=0)
        entry3.grid(row=3, column=1)

def safe_eval(input):
    if re.match(r'^[0-9\+\-\*\/\(\)]+$', input):
        try:
            return eval(input, {"__builtins__": None}, {})
        except:
            return None
    else:
        return "no input"
    
def fomula():
    try:
        fomula = entry1.get()
        result = safe_eval(fomula)
        result_label.config(text=f"{fomula}의 결과는 {result} 입니다")
    except:
        result_label.config(text="수식을 입력하세요")

def sum():
    try:
        num1 = int(entry2.get())
        num2 = int(entry3.get())
        if (num1 > num2):
            num1, num2 = num2, num1
        result = 0
        result = (num1 + num2)/2 * (num2 - num1 + 1)
        result = int(result)
        result_label.config(text=f"{num1} + .... + {num2} 의 결과는 {result} 입니다")
    except:
        result_label.config(text="숫자를 입력하세요")
        
def controllfunction():
    selected = selection.get()
    if selected == "입력한 수식 계산":
        fomula()
    elif selected == "입력한 두 수 사이의 합계":
        sum()

selection.bind("<<ComboboxSelected>>", lambda event: select())

main_window.bind("<Return>", lambda event: controllfunction())

tab.pack(expand=0, fill="both")

main_window.mainloop()