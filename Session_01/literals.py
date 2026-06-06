# A literal is a fixed value written directly in the code.
name = "Devanshu"
age = 22
# "Devanshu" → string literal
# 22 → integer literal
# name aur age → identifiers (names)

a = 0b1010 #Binary Literals
b = 100 #Decimal Literal 
c = 0o310 #Octal Literal
d = 0x12c #Hexadecimal Literal

#Float Literal
float_1 = 10.5 
float_2 = 1.5e2 # 1.5 * 10^2
float_3 = 1.5e-3 # 1.5 * 10^-3

#Complex Literal 
x = 3.14j

print(a, b, c, d)
print(float_1, float_2,float_3)
print(x, x.imag, x.real)

# Complex
x = 2+3.14j
print(x.real, x)
print(x.imag)

# String literal in python.
string = 'This is Python'
strings = "This is Python"
char = "C"
multiline_str = """This is a multiline string with more than one line code."""
unicode = u"\U0001f600\U0001F606\U0001F923"
raw_str = r"raw \n string"

print(string)
print(strings)
print(char)
print(multiline_str)
print(unicode)
print(raw_str)

# Here True is 1 and False is 0.
a = True + 4 # Output: 5
b = False + 10 # Output: 10

# No value / absence of value / nothing assigned yet. None is a special value that represents "nothing".
k = None