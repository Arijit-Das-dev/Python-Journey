# String slicing
# string slicing => StringVariable[starting index : ending index]
# It only takes the string index to ending index - 1
# Indexing are two types => Positive indexing and Negative indexing


""" Positive indexing """

string = "abcdefghi"
print(string[1:2])

# abcdefghi => [0, 1, 2, 3, 4, 5, 6, 7, 8] <= indexes
#              [a, b, c, d, e, f, g, h, i]
#              [1:2] <= [b:c] => b

print(string[1:])
print(string[:4])


""" Negative indexing """

print(string[-1:-3])