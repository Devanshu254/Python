# Module is a python file in which some functions are writtern, we can import those modules in our program so that we can use someone' else's function in our code.
# Principle: Code Reusability.

# math
# keyword
# random
# datetime

# math
import math
print(math.factorial(5))
print(math.sqrt(85))

# keyword: reserved words in python. 
# If we want to see how many reserved words are there in python then we can use this module.
import keyword
print(keyword.kwlist)

# random: generate random values.
import random
print(random.randint(1,100))

# datetime
import datetime
print(datetime.datetime.now())

# How many modules are available in python.
help('modules')