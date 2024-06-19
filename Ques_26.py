'''Write a program in python that checks if a string starts with a given prefix or ends with a given suffix.'''

def check_prefix_suffix(prefix, suffix, str):
    isprefix = str.startswith(prefix)
    issuffix = str.endswith(suffix)
    return (isprefix | issuffix)

str = input("Enter the string:")
prefix = input("Enter the prefix:")
suffix = input("Enter the suffix:")
print("Does the string starts with", prefix, "or ends with", suffix, ":", check_prefix_suffix(prefix, suffix, str))
