# STRING METHODS

"""
1. [Case Conversion]

lower() = convert to lowercase

upper() = convert to uppercase

title() = first letter capitalized

capitalize() = capitalize first character

swapcase() = swap upper ↔ lower

"""

a = "ABCDE"
print(a.lower())

b = "abcde"
print(b.lower())

c = "arijit"
print(c.title())

d = "abcdefgh"
print(d.capitalize())

e = "abcdef"
print(e.swapcase())

f = "ABCDEF"
print(f.swapcase())



"""
2. [Whitespace Removal]

strip() = remove leading & trailing spaces

lstrip() = remove left spaces

rstrip() = remove right spaces

"""

a = "Hello world"
print(a.strip())
print(a.lstrip())
print(a.rstrip())



"""
3. [Search & Check]

find() = first occurrence index

rfind() = last occurrence index

index() = like find (throws error if not found)

rindex() = reverse index

count() = count substring occurrences

"""

b = "abcdefghijklmnopqrstuv"

print(b.find("h"))
print(b.index("a"))
print(b.count("a"))



"""
4. [Boolean / Validation Methods]

startswith()

endswith()

isalnum()

isalpha()

isdigit()

isnumeric()

isdecimal()

islower()

isupper()

istitle()

isspace()

isidentifier()

isprintable()
"""

name = "alex"
print(name.startswith("a"))
print(name.endswith("v"))
print(name.islower())
print(name.isupper())
print(name.title())
print(name.isnumeric())
print(name.isdigit())



"""
5. [Replace & Modify]

replace() = replace substring

translate() = map characters

maketrans() = helper for translate

"""

string = "I love Python"
newString = string.replace("Python" ,"c++")
newString = string.replace(" ", "")
print(newString)


string2 = "machine learning"
mapping = string2.maketrans("learning", "12345678")
finalText = string2.translate(mapping)
print(finalText)


"""
6. [Encoding / Decoding]

encode() = string → bytes

"""

name = "alex"
print(name.encode())