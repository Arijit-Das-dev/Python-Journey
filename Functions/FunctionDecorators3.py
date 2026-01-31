def decorator(func):

    def wrapper(a, b):
        print("before addition")
        result = func(a, b)
        print("After addition")
        return result

    return wrapper

@decorator
def main(a, b):

    result = a+b
    print(result)