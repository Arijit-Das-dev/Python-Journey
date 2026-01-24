"""
Docstring for Functions.FunctionWithParameters
"""

# With Parameters
def parameters(a, b):

    summ = a + b

    return summ

result = parameters(10, 12)
print(result)


def greet(name):

    print("hello",name)

greet("arijit")


# Default arguements
def example(name = "default"):

    print("Hello",name)

example("Arijit")


# Keyword arguements <= when we pass the actual parameter name with it's value 
def pet(animalName, colour, breed):

    print("My animal name is",animalName)
    print("My", animalName,"'s" ,"colour is", colour)
    print("My dog's breed is",breed)

pet(animalName="Dog", colour="Black", breed="Pitbull")


# Positional arguements <= where we dont need to pass any actual parameter name, only the value
def pet(animalName, colour, breed):

    print("My animal name is",animalName)
    print("My", animalName,"'s" ,"colour is", colour)
    print("My dog's breed is",breed)

pet("Dog", "Black", "Pitbull")


# Passing Different Data Types <= list, dictionary, string
# List
def exampleOfList(items):

    for item in items:
        print(item)

exampleOfList([1, 2, 3, 4, 5, 6, 7])


# String
def exampleOfString(chars):

    for char in chars:
        print(char)

exampleOfString("abcdef")


# Dictionary
def exampleOfDictionary(person):
  print("Name:", person["name"])
  print("Age:", person["age"])

my_person = {"name": "Emil", "age": 25}
exampleOfDictionary(my_person)