"""
Extract username from given email.
"""

s = input("Enter the email: ")
pos = s.index('@')
print(s[0:pos])
