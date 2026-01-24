"""
Docstring for Loops.ForElse

"""

# Else block will only execute after the execution of for loop command 
for x in range(3):
    print(x)
else:
    print("Finally finished!")


# Else block will not execute if a break statement execute between looping
for x in range(1, 11):

    if x == 5:
        break
    print(x)
else:
    print("Finally finished!")


# Else block execute successfully with continue statement
for x in range(11):
    
    if x == 5:
        continue
    print(x)

else:
    print("success")