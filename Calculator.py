import tkinter as tk
import math

def on_click(symbol):
    entry_equation.insert(tk.END, symbol)

def clear_all():
    entry_equation.delete(0, tk.END)
    label_result.config(text="")

def calculate():
    try:
        expression = entry_equation.get()
        # Replace common math functions for evaluation
        expression = expression.replace('sin', 'math.sin')
        expression = expression.replace('cos', 'math.cos')
        expression = expression.replace('tan', 'math.tan')
        expression = expression.replace('sqrt', 'math.sqrt')
        expression = expression.replace('log', 'math.log10')
        expression = expression.replace('ln', 'math.log')
        expression = expression.replace('^', '**')
        expression = expression.replace('asin', 'math.asin')
        expression = expression.replace('acos', 'math.acos')
        expression = expression.replace('atan', 'math.atan')

        result = eval(expression)
        label_result.config(text="= " + str(result))
    except:
        label_result.config(text="Error ❌")

# Create the main window
root = tk.Tk()
root.title("Basic Calculator")
root.geometry("300x470")  # Increased height for better fit
root.resizable(False, False)

# Equation input field
entry_equation = tk.Entry(root, font=("Arial", 20), bd=2, relief=tk.RIDGE, justify='right')
entry_equation.pack(fill=tk.BOTH, ipadx=8, ipady=10, padx=10, pady=10)

# Result label
label_result = tk.Label(root, text="", font=("Arial", 18), anchor='e', bg='white', fg='blue', height=2)
label_result.pack(fill=tk.BOTH, padx=10, pady=(0, 10))

# Buttons
button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    ['sin', 'cos', 'tan', 'sqrt'],
    ['asin', 'acos', 'atan', '^'],
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', 'log', '+'],
    ['(', ')', 'C', '=']
]

for row in buttons:
    row_frame = tk.Frame(button_frame)
    row_frame.pack(expand=True, fill='both')
    for btn_text in row:
        if btn_text == '':
            tk.Label(row_frame, text="", width=7).pack(side=tk.LEFT, expand=True)
            continue
        if btn_text == '=':
            tk.Button(row_frame, text=btn_text, width=7, height=2, bg='green', fg='white',
                      command=calculate).pack(side=tk.LEFT, expand=True, padx=1, pady=1)
        elif btn_text == 'C':
            tk.Button(row_frame, text='C', width=7, height=2, bg='red', fg='white',
                      command=clear_all).pack(side=tk.LEFT, expand=True, padx=1, pady=1)
        elif btn_text == 'sqrt':
            tk.Button(row_frame, text='√', width=7, height=2,
                      command=lambda txt='sqrt': on_click(txt)).pack(side=tk.LEFT, expand=True, padx=1, pady=1)
        else:
            tk.Button(row_frame, text=btn_text, width=7, height=2,
                      command=lambda txt=btn_text: on_click(txt)).pack(side=tk.LEFT, expand=True, padx=1, pady=1)

root.mainloop()
