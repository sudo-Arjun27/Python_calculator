import tkinter as tk

# Function to perform the calculation
def calculate(operation):
    try:
        a = float(entry1.get())  # Get the first number
        b = float(entry2.get())  # Get the second number
        
        if operation == "+":
            result.set(f"Result: {a + b}")
        elif operation == "-":
            result.set(f"Result: {a - b}")
        elif operation == "*":
            result.set(f"Result: {a * b}")
        elif operation == "/":
            if b != 0:
                result.set(f"Result: {a / b}")
            else:
                result.set("Error: Division by zero")
        elif operation == "%":
            result.set(f"Result: {a % b}")
    except ValueError:
        result.set("Invalid input! Please enter numbers.")

# Function to clear all inputs
def clear():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    result.set("")

# Create the main window
root = tk.Tk()
root.title("Basic Calculator")
root.geometry("300x300")

# Create input fields
tk.Label(root, text="Enter the first number:").grid(row=0, column=0, padx=10, pady=5)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Enter the second number:").grid(row=1, column=0, padx=10, pady=5)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, padx=10, pady=5)

# Buttons for operations
tk.Button(root, text="+", width=5, command=lambda: calculate("+")).grid(row=2, column=0, padx=5, pady=5)
tk.Button(root, text="-", width=5, command=lambda: calculate("-")).grid(row=2, column=1, padx=5, pady=5)
tk.Button(root, text="*", width=5, command=lambda: calculate("*")).grid(row=3, column=0, padx=5, pady=5)
tk.Button(root, text="/", width=5, command=lambda: calculate("/")).grid(row=3, column=1, padx=5, pady=5)
tk.Button(root, text="%", width=5, command=lambda: calculate("%")).grid(row=4, column=0, padx=5, pady=5)

# Clear button
tk.Button(root, text="Clear", width=10, command=clear).grid(row=4, column=1, padx=5, pady=5)

# Label to display the result
result = tk.StringVar()
tk.Label(root, textvariable=result).grid(row=5, column=0, columnspan=2, pady=10)

# Run the main loop
root.mainloop()
