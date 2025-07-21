# Basic Calculator

A simple calculator built with Python and Tkinter. This calculator supports basic arithmetic operations as well as scientific functions such as trigonometric, logarithmic, and square root calculations.

## Features
- Basic arithmetic: `+`, `-`, `*`, `/`, `^`
- Trigonometric functions: `sin`, `cos`, `tan`, `asin`, `acos`, `atan`
- Logarithmic functions: `log` (base 10), `ln` (natural log)
- Square root: `√`
- Parentheses for grouping
- Clear (`C`) and equals (`=`) buttons
- User-friendly GUI

## Layout
```
['sin', 'cos', 'tan', '√']
['asin', 'acos', 'atan', '^']
['7', '8', '9', '/']
['4', '5', '6', '*']
['1', '2', '3', '-']
['0', '.', 'log', '+']
['(', ')', 'C', '=']
```

## How to Run
1. Make sure you have Python 3 installed.
2. Clone this repository:
   ```sh
   git clone https://github.com/hyprpranav/codsoft_tasks.git
   ```
3. Navigate to the project directory:
   ```sh
   cd codsoft_tasks
   ```
4. Run the calculator:
   ```sh
   python Calculator.py
   ```

## Notes
- This calculator uses Python's `eval()` for expression evaluation. Avoid entering arbitrary code for security reasons.
- The square root button is labeled as `√` but internally uses `sqrt` in the expression.

## License
This project is for educational purposes.
