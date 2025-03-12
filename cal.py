#Calculator

import tkinter as tk
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

entry = tk.Entry(root, width=15, font=("Arial", 20), justify="right")
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8)

"""b7 = tk.Button(root, text="7")
b7.grid(row=1, column=0, padx=10, pady=5)
b8 = tk.Button(root, text="8")
b8.grid(row=1, column=1, padx=10, pady=5)
b9= tk.Button(root, text="9")
b9.grid(row=1, column=2, padx=10, pady=5)
b4 = tk.Button(root, text="4")
b4.grid(row=2, column=0, padx=10, pady=5)
b5 = tk.Button(root, text="5")
b5.grid(row=2, column=1, padx=10, pady=5)
b6 = tk.Button(root, text="6")
b6.grid(row=2, column=2, padx=10, pady=5)
b1 = tk.Button(root, text="1")
b1.grid(row=3, column=0, padx=10, pady=5)
b2 = tk.Button(root, text="2")
b2.grid(row=3, column=1, padx=10, pady=5)
b3 = tk.Button(root, text="3")
b3.grid(row=3, column=2, padx=10, pady=5)
b0 = tk.Button(root, text=0)
b0.grid(row=4, column=1, padx=10, pady=5)
ba = tk.Button(root, text="+")
ba.grid(row=4, column=3, padx=10, pady=5)
bs = tk.Button(root, text="-")
bs.grid(row=3, column=3, padx=10, pady=5)
bm = tk.Button(root, text="*")
bm.grid(row=2, column=3, padx=10, pady=5)
bd = tk.Button(root, text="/")
bd.grid(row=1, column=3, padx=10, pady=5)
be = tk.Button(root, text="=")
be.grid(row=4, column=2, padx=10, pady=5)
bc = tk.Button(root, text="C")
bc.grid(row=4, column=0, padx=10, pady=5)"""

expression=""

def num_handle(value):
    global expression
    expression+=str(value)
    update_display(expression)
    
def op_handle(op_value):
    global expression
    if expression != "" and expression[-1] not in "+-*/":
        expression += op_value
    update_display(expression)
    
def eq_handle():
    global expression
    try:
        result= str(eval(expression))
        expression=result
        update_display(expression)
    except ZeroDivisionError:
        expression=""
        update_display("Error! denominator is 0")
    except:
        expression=""
        update_display("Error!")
        
def cl_handle():
    global expression
    expression=""
    update_display("0")
    
def update_display(value):
    entry.delete(0, tk.END)  # Clear previous display
    entry.insert(0, value)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 1), ('C', 4, 0), ('=', 4, 2), ('+', 4, 3)
]

for (text, row, col) in buttons:
    if text.isdigit():  # If button is a number
        action = lambda t=text: num_handle(t)
    elif text in "+-*/":  # If button is an operator
        action = lambda t=text: op_handle(t)
    elif text == "=":  # If button is "="
        action = eq_handle
    else:  # If button is "C" (Clear)
        action = cl_handle
    tk.Button(root, text=text, font=("Arial", 20), padx=20, pady=20, command=action).grid(row=row, column=col, sticky="nsew")

root.mainloop()