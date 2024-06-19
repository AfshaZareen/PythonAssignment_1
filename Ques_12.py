'''Write a python program that calculates the sum of the digits of a given number.'''

number = int(input("Enter the number: "))
temp = number
lastDigit = 0
sum = 0
while (number > 0) :
    lastDigit = number % 10
    sum += lastDigit
    number //= 10
print("Sum of the", temp, " is:", sum) 