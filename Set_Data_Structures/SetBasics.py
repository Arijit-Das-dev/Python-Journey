# set basics
# sets are immutable -> unchangable
# sets are unordered

isSet = {"a", "b", "c", "d"}
print(isSet)
print(type(isSet))


# Duplicates Not Allowed
collection = {"a", "b", "c", "a", 1, 1, 2, 2}
print(collection)


# True and 1 consider as True
collection2 = {True, 1}
print(collection2)


# False and 0 are consider as False 
collection3 = {False, 0}
print(collection3)


# Length of set
collection4 = {1, 0.3, 2.234, True, False, "String"}
print(len(collection4))


# The set() Constructor
collection5 = set((1, 2, 3, 4, 5))
print(type(collection5))