# If you do not know how many arguments will be passed into your function, add a * before the parameter name.

# def function(*args):

def addition(*nums):

    total = 0

    for n in nums:

        total += n
    
    return total

print(addition(1, 2, 3, 4))


def subtraction(*nums):

    result = 0

    for n in nums:

        result -= n

    return result

print(subtraction(1, -2, 4))


def multiplication(*nums):

    result = 1

    for n in nums:

        result *= n

    return result

print(multiplication(1, 2, 3))


def division(*nums):

    result = nums[0]

    for n in nums[1:]:
        
        result /= n

    return result

print(division(12, 6))



# def function(**kwargs):


def my_function(**myvar):
  print("Type:", type(myvar))
  print("Name:", myvar["name"])
  print("Age:", myvar["age"])
  print("All data:", myvar)

my_function(name = "Tobias", age = 30, city = "Bergen")

def my_function(title, *args, **kwargs):
  print("Title:", title)
  print("Positional arguments:", args)
  print("Keyword arguments:", kwargs)

my_function("User Info", "Emil", "Tobias", age = 25, city = "Oslo")