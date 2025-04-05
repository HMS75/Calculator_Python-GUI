import tkinter as tk
import math

root = tk.Tk()
root.title("Enhanced Calculator")
root.geometry("320x450")
root.configure(bg="#2e2e2e")  
# Dark background

expression = ""
memory = ""

entry = tk.Entry(root, width=20, font=("Arial", 22), justify="right", bd=5, bg="#1e1e1e", fg="white")
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=12, pady=10)

def update_display(value):
    entry.delete(0, tk.END)
    entry.insert(0, value)

def num_handle(value):
    global expression
    expression += str(value)
    update_display(expression)

def op_handle(op_value):
    global expression
    if expression and expression[-1] not in "+-*/^%":
        expression += op_value
    update_display(expression)

def cl_handle():
    global expression
    expression = ""
    update_display("0")

def sqrt_handle():
    global expression
    try:
        result = str(math.sqrt(float(expression)))
        expression = result
        update_display(result)
    except:
        expression = ""
        update_display("Error!")

def pow_handle():
    global expression
    if expression and expression[-1].isdigit():
        expression += "**"
    update_display(expression)

def mod_handle():
    global expression
    if expression and expression[-1].isdigit():
        expression += "%"
    update_display(expression)

def eq_handle():
    global expression
    try:
        result = str(eval(expression))
        expression = result
        update_display(result)
    except ZeroDivisionError:
        expression = ""
        update_display("Error! ÷ by 0")
    except:
        expression = ""
        update_display("Invalid input")

def mem_save():
    global memory, expression
    memory = expression
    update_display("Saved")
    
def mem_recall():
    global expression
    expression += memory
    update_display(expression)
    
#adding buttons
buttons = [
    ('C', 1, 0), ('√', 1, 1), ('^', 1, 2), ('%', 1, 3),
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3),
    ('0', 5, 0), ('M+', 5, 1), ('MR', 5, 2), ('+', 5, 3),
    ('=', 6, 0, 4)
]

for btn in buttons:
    text = btn[0]
    row = btn[1]
    col = btn[2]
    colspan = btn[3] if len(btn) == 4 else 1

    if text.isdigit():
        action = lambda t=text: num_handle(t)
    elif text in "+-*/":
        action = lambda t=text: op_handle(t)
    elif text == "C":
        action = cl_handle
    elif text == "=":
        action = eq_handle
    elif text == "√":
        action = sqrt_handle
    elif text == "^":
        action = pow_handle
    elif text == "%":
        action = mod_handle
    elif text == "M+":
        action = mem_save
    elif text == "MR":
        action = mem_recall

    tk.Button(root, text=text, font=("Arial", 18), padx=10, pady=15, width=5, bg="#444", fg="white", command=action).grid(row=row, column=col, columnspan=colspan, sticky="nsew", padx=2, pady=2)

root.mainloop()
