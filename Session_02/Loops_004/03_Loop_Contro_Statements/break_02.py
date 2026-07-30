"""
Question: User will give us a range. We need to print prime numbers in between of that range.
Prime number is a number which has only two factors, one which of its own and another is 1. Others are composite number which are having more than one factor.
"""
lower = int(input("Enter the lower range: "))
upper = int(input("Enter an upper range: "))

for i in range(lower, upper+1):
    for j in range(2, i):
        if i%j == 0:
            break
    else:
        print(i)
