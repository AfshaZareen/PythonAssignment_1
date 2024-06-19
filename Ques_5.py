'''Write a program that takes a string input from the user and writes it to a text file.'''

input = input("enter the input: ")
fileObj = open(r"C:\Users\HP\Downloads\Python ML IGDTUW\Demo File.txt", 'w')
print(input, file = fileObj)
