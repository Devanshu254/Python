# Menu driven calculator

fnum = int(input("Enter the number 1: "))
snum = int(input("Enter the number 2: "))

op = input("Enter the operation: ")

if op == '+':
    print(fnum + snum)
elif op == '-':
    print(fnum - snum)
elif op == '*':
    print(fnum * snum)
else:
    print(fnum/snum)