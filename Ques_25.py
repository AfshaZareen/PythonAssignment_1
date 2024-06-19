'''Write a program that copies the contents of one text file to another.'''

obj1 = open(r"C:\Users\HP\Downloads\Python ML IGDTUW\fileText_1.txt", 'r')
content = obj1.read()
obj2 = open(r"C:\Users\HP\Downloads\Python ML IGDTUW\fileText_2.txt", 'w')
obj2.write(content)