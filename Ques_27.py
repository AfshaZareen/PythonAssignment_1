'''Write a program in python that converts a string into a list of its characters'''

str = input("Enter the string:")
list_char = []
for i in str:
    list_char.append(i)
print("List of characters of", str, ":", list_char)