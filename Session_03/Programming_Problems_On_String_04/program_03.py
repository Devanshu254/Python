"""
Count the frequency of a particular character in a provided string.
Eg: 'hello how are you' is a string, the frequency of h is 2.
"""

s = input("Enter the String: ")
term = input("What would you like to search for ?: ")

counter = 0
for i in s:
    if i == term:
        counter = counter + 1

print("Frequency ", counter)