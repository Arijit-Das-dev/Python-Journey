# Integer data type

a = 12

# Float Data Type

b = 12.0

# String Data Type

name = "abcde"

# boolean Data Type

isCorrect = True

# complex Data Type

com = 1 + 3j


# How to check data types of any variable ?
print(type(a))
print(type(b))
print(type(name))
print(type(isCorrect))
print(type(com))

# How to do type conversion ?

# int to float
a = 12
print(float(a))

# float to int
b = 12.0
print(int(b))

# string to int
# Note : It is only possible when the given string is a number other wise it will throw an error.
num = "1"
print(int(num))

# int to string
a = 12
print(str(a))


# int to complex conversion

num = 1
print(complex(num))