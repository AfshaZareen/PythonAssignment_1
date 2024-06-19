'''Write a python program that returns the minimum and maximum values in a list of numbers.'''

list1 = [7,8,99,33,100,9,2]
max = list1[0]
min = list1[0]
for i in list1:
    if (i > max):
        max = i
    else:
        min = i
print("Maximum element is:", max)
print("Minimum element is:", min)