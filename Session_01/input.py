# Static Software: They are just used to give information to user like Calender,blog and Clock it's not interacting with user.
# Dynamic Software: Here user talks. Youtube, Ola, Zomato, Swiggy. 

# name = input("Please enter your name: ")
# print("Hello", name)

# Program to add two numbers.
first_num = input("Please enter first number: ")
second_num = input("Please enter second number: ")
print(type(first_num), type(second_num)) # input() returns a string because keyboard input is received as text (sequence of characters). Python leaves type conversion to the programmer to avoid ambiguity and provide flexibility.
result = int(first_num) + int(second_num)
print(result)
print(type(first_num)) # Still the value is string.

# Type conversion - Implicit Vs Explicit
# Implicit: Type conversion means where interpreter do conversion automatically.
print(5+5.6) # Example of Implicit type conversion.
# Explicit: Type conversion means 

# Better way to write above program.
num1 = int(input("Enter the number 1: "))
num2 = int(input("Enter the number 2: "))
print(num1+num2)