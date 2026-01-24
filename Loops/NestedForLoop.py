"""
Docstring for Loops.NestedForLoop
"""

nums = [1, 2, 3, 4, 5]
chars = ["a", "b", "c", "d"]

for num in nums:
    for char in chars:
        print(num, char)


nums = [1, 2, 3, 4]
chars = ["a", "b", "c", "d"]
numChars = ["1a", "2b", "3c", "4d"]

for num in nums:
    for char in chars:
        for numChar in numChars:
            print(num, char, numChar)