'''Write a python program that checks if two strings are anagrams of each other.'''

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
# sorting the strings
# sorted(string_name) -> return sorted list
list1 = sorted (str1.upper())
list2 = sorted(str2.upper())
# converting list back to string
# ''.join(list_name) -> convert list into string with no space between characters 
sorted_str1 = ''.join(list1)
sorted_str2 = ''.join(list2)
if (sorted_str1 == sorted_str2):
    print(str1, "and", str2, "are anagrams")

else:
    print(str1, "and", str2, "are not anagrams")