"""
Docstring for Loops.whileLoopBasic
"""

# Print 0 to 10
i = 0
while(i <= 10):

    print(i)

    i += 1

# break statement
i = 1
while(i <= 10):

    print(i)

    if i == 5:
        break

    i += 1


# continue statement
i = 0
while i <= 10:
    print(i)

    if i == 5:
        i += 1
        continue

    i += 1