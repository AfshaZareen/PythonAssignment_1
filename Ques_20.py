'''Write a python program that takes a list of numbers and returns their sum'''

str = input("Enter list of numbers: ")
list1 = str.split(",")
sum = 0
for i in list1:
    sum += int(i)
print(sum)