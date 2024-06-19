'''Write a python program that removes all punctuation from a given string.'''  

import string
# string.punctuation -> list all punctuation characters
punctuation_char = string.punctuation
str = input("Enter the string: ")
list1 = []
for i in range(len(str)):
    if str[i] not in punctuation_char:
        list1.append(str[i])
updated_str = "".join(list1)
print(updated_str)