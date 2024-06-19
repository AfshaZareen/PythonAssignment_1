'''Write a program in python that counts the frequency of each character in a string'''

str = input("Enter the string: ")
dict = {}
for i in range(len(str)):
    freq = 0
    for j in range(len(str)):
        if (str[i] == str[j]):
            freq = freq + 1
    dict[str[i]] = freq
print("The frequency of characters in", str, "is:", dict)


# another method
str = input("Enter the string: ")
freq_dict = {}
for char in str:
    if char in freq_dict:
        freq_dict[char] += 1
    else:
        freq_dict[char] = 1
print("The frequency of characters in", str, "is:", freq_dict)
