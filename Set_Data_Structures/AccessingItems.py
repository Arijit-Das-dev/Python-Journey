# You can not access elements by indexes
collection = {"a", "b", "c", "a", 1, 1, 2, 2}

for i in collection:
    print(i)



# adding elements in the set
collection.add(5)
print(collection)


# adding another set collection
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)


# adding any iterable
tropical = {"pineapple", "mango", "papaya"}
list_collection = [1, 2, 3, 45]
tropical.update(list_collection)
print(tropical)