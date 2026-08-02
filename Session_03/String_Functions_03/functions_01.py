"""
Common Functions:
1. len 
2. max   
3. min
4. sorted
"""
print(len('hello world')) # 11
print(max('hello world')) # Max value based on ASCII -> w
print(min('hello world')) # Min value based on ASCII -> space
print(sorted('hello world')) # Sorted based on ASCII -> Ascending order
# [' ', 'd', 'e', 'h', 'l', 'l', 'l', 'o', 'o', 'r', 'w']
print(sorted('hello world', reverse=True))
# ['w', 'r', 'o', 'o', 'l', 'l', 'l', 'h', 'e', 'd', ' ']