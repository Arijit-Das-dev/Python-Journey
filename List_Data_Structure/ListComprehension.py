# newlist = [expression for item in iterable if condition == True]

newList = [i for i in range(1, 11)]
print(newList)

newList2 = [x for x in range(0, 11) if x>5]
print(newList2)

evenList = [x for x in range(1, 21) if x%2 == 0]
print(evenList)

oddList = [x for x in range(1, 21) if x%2 != 0]
print(oddList)


evenOddList = ["Even" if x%2 == 0 else "Odd" for x in range(1, 21)]
print(evenOddList)

fruits = ["apple", "banana", "goava", "coconut"]
upperCaseList = [x.upper() for x in fruits]
print(upperCaseList)

fruits = ['APPLE', 'BANANA', 'GOAVA', 'COCONUT']
lowerCaseList = [x.lower() for x in fruits]
print(lowerCaseList)


nameList = ["abcd", "cdef", "ghji", "lkl0", "klqpw"]
newNameList = [x.capitalize() for x in nameList]
countCharOccurence = [x.count("e") for x in nameList]
print(newNameList)
print(countCharOccurence)