'''Write a python program that calculates the factorial of a given number.'''

number = int(input("Enter the number: "))
factorial = 1
originalNo = number
while(number > 1) :
    factorial *= number
    number -= 1
print("Factorial of", number, "is:", factorial)