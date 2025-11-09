# CodSoft Internship Task 1: Simple Calculator
# Name: Harinishree
# Domain: Python Programming
# Batch: [October to November batch B57]
# Description: A simple calculator that performs basic arithmetic operations.
def calculator():
    print("===== Simple Calculator =====")
    print("Operations: +  -  *  /  %  **")
    print("=============================")

    # Taking user input
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Choose an operation (+, -, *, /, %, **): ")

        # Performing calculation
        if operation == '+':
            result = num1 + num2
            print(f"Result: {num1} + {num2} = {result}")
        elif operation == '-':
            result = num1 - num2
            print(f"Result: {num1} - {num2} = {result}")
        elif operation == '*':
            result = num1 * num2
            print(f"Result: {num1} * {num2} = {result}")
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
                print(f"Result: {num1} / {num2} = {result}")
            else:
                print("Error: Division by zero is not allowed.")
        elif operation == '%':
            result = num1 % num2
            print(f"Result: {num1} % {num2} = {result}")
        elif operation == '**':
            result = num1 ** num2
            print(f"Result: {num1} raised to the power {num2} = {result}")
        else:
            print("Invalid operation! Please choose a valid one.")

    except ValueError:
        print("Error: Please enter the valid numbers.")

# Run the calculator
calculator()
