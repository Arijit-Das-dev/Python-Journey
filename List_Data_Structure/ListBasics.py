"""
Docstring for List_Data_Structure.ListBasics
"""

# Basic list
fruits = ["apple", "goava", "banana", "coconut"]
print(fruits)
print(type(fruits))

#  A list can store different Data Types : -> [string, integer, bool, float]
multi_data_type_list = ["arijit", 12, 12.0, True]
print(multi_data_type_list)


# Allow Duplicates
nums = [12, 12, 13, 18, 19, 18]
print(nums)
 

# List Length
nums = [12, 12, 3, 4, 5]
print(len(nums))


# The list() Constructor
nums = list((1, 2, 3, 4))
print(nums)