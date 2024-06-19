'''Write a program that converts temperature from Celsius to Fahrenheit and vice versa based on user input'''

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit -32) * 5/9
    return celsius

celsius = int(input("Enter the temperature in celsius:"))
fahrenheit = int(input("Enter the temperature in fahrenheit:"))
converted_to_fahrenheit = celsius_to_fahrenheit(celsius)
converted_to_celsius = fahrenheit_to_celsius(fahrenheit)
print(celsius, "C", "is equal to", converted_to_fahrenheit, "F")
print(fahrenheit, "F", "is equal to", converted_to_celsius, "C")