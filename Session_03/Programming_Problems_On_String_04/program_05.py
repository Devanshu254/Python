"""
Check whether a given string is palindrome or not.
abba == abba
"""
s = input("Please enter the string: ")
r = s[::-1]
if s == r:
    print("String is palindrome!")
else:
    print("not")