# Login program and indentation.
# email -> devanshujha8305@gmail.com
# password -> 1234

email = input("Enter the email: ")
password = input("Enter the password: ")

if email == 'devanshujha8305@gmail.com' and password == '1234':
    print("You are authorized")
elif email == 'devanshujha8305@gmail.com' and password != '1234':
    print("Password is wrong, please try again.")
    password = input("Enter the password again: ")
    if(password == '1234'):
        print("You are authorized")
    else:
        print("You have attempted wrong password 2 times.. Please try again later.")
else:
    print("You are not authorized")

"""
if condition:
    #code
else:
    #code
"""