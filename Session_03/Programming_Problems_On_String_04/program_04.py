"""
Write a program which can remove a particular character from string.
"""
s = input("enter the String: ")
term = input("What would you like to remove: ")

result = ''

for i in s:
    if i != term:
        result = result + i

print(result)