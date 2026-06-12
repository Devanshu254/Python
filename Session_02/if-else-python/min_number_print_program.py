# Print the min of three numbers.

a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
c = int(input("Enter number 3 "))

if a<b and a<c:
    print("a is min", a)
elif b<a and b<c:
    print("b is min", b)
elif c<a and c<b:
    print("c is min ", c)
else:
    print("All are equal")