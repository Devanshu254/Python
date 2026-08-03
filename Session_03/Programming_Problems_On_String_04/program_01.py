# Find the length of given string without using len() function.

s = input("Enter the string: ")

counter = 0 
for i in s:
    counter = counter + 1

print("Length of String is: ", counter)