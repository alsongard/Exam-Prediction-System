"""
    there are 2 types of argument:
    positional and keyword argument
"""

#positional argument
def sumProgram(a,b):
    return a + b

print(sumProgram(2,7))


#keyword argument
def minusProgram(c,d):
    return c - d

print(minusProgram(c=10,d=2))

#however 2 produce the Syntax Error: positional argument follows a keyword argument
# print(sumProgram(a=10,23))
# the above code will result in an error always ensure the positional argument comes first before the keyword argument
print(sumProgram(10,b=23))