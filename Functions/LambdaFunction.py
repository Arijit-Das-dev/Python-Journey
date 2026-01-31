"""
Docstring for Functions.LambdaFunction

A lambda function is a small anonymous function.

A lambda function can take any number of arguments, but can only have one expression.
"""

# BASIC LAMBDA FUNCTION
add = lambda a : a + 10
print(add(2))

sub = lambda a, b  : a-b
print(sub(1, 2))

mul = lambda a, b, c : a*b*c
print(mul(1, 2, 4))

div = lambda a, b : a/b
print(div(4, 2))


# LAMBDA FUNCTION INSIDE A FUNCTION
"""
In this case we are defining two functions =>

1. Outer function
2. Inner lambda function

**Note = we have to pass two actual parameter
"""
def add(n):

    return lambda a: a*n

result = add(5)
print(result(5))


def myFunction(n):

    return lambda a : a/n

result = myFunction(5)
print(result(5))