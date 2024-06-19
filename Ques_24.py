'''Write a program that acts as a simple calculator. It should take two numbers and an operator (+, -, *, /) as input and print the result.'''

def calculator(num1, num2, operator):
    if operator == "+":
        print("Sum of numbers:", num1 + num2)
    elif operator == "-":
        print("Subtraction of two numbers:", num1 - num2)
    elif operator == "*":
        print("Multiplication of numbers:", num1 * num2)
    elif operator == "/":
        print("Division of numbers:", num1 / num2)
    else:
        print("Enter a valid operator.")
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
operator = input("Enter the operator:")
calculator(num1, num2, operator)