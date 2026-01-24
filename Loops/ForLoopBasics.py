"""
Docstring for Loops.ForLoopBasics
"""

# Printing 1 to 10
for i in range(1, 11):
    print(i, end=" ")


# Print each fruit in a fruits list:
fruits = ["apple", "goava", "coconut", "banana", "cherry"]
for fruit in fruits:
    print(fruit)


# Looping through string
string = "abcde"
for chars in string:
    print(chars)


# break statement
fruits = ["apple", "goava", "coconut", "banana", "cherry"]

stop = "coconut"

for fruit in fruits:

    if fruit == stop:
        break

    print(fruit)


# continue statement
fruits = ["apple", "goava", "coconut", "banana", "cherry"]

skip = "banana"

for fruit in fruits:

    if fruit == skip:
        continue

    print(fruit)


# Increment the sequence with 3 (default is 1):
for i in range(1, 21, 2):
    print(i)