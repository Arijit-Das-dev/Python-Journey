# local scope 
# A variable stores inside a function which is only accessable inside the function

def localScope():

    var = 12

    return var

print(localScope())


# Global scope 
# a variable created outside the function which is accessible anywhere

x = 10

def globalScope():

    print(x)

globalScope()