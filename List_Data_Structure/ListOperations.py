# List Joining
nums1 = [1, 2, 3, 4]
nums2 = [5, 6, 7, 8]

newNum = nums1 + nums2
print(newNum)


# List addition
nums = [1, 2, 3, 4, 5]
newNums1 = [i+1 for i in nums]
print(newNums1)


# List subtraction
newNums2 = [i-1 for i in nums]
print(newNums2)

# List multiplication
newNums3 = [i*2 for i in nums]
print(newNums3)

# List division
newNums4 = [i//2 for i in nums]
print(newNums4)


# Repetition (*)
newNums5 = nums * 2
print(newNums5)