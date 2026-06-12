# Write program to sum a 3 digit number given by user.

num = int(input("Enter the number: "))
last_digit = int()
sum = int()
while(num != 0):
    last_digit = num%10
    sum = sum  + last_digit
    num = num//10

print(sum)