# How to access substrings from string.

# # Positive Indexing.
# s = 'hello world'
# print(s[6])

# # Negative Indexing.
# s = 'hello world'
# print(s[-1])

# Slicing.
s = 'hello world'
print(s[0:4])
print(s[1:]) # Going from 1st to last.
print(s[:5]) # Going from fist to 5th.
print(s[:]) # Print complete string.
# Stepsize.
print(s[0:6:2])
# We can use negative indexing as well.
print(s[-1:-6:-1])
print(s[6:0:-1])

# Reverse a given string.
print(s[::-1])