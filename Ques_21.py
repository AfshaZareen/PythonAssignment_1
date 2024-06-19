'''Write a python program that counts the occurrences of a specific element in a list.'''

list1 = [1,1,2,3,6,7,7,3,2,4,8,6,3,4,3]
element = int(input("Enter the specific element to be counted:"))
occurence = list1.count(element)
print('The occurence of', element, 'is:', occurence)