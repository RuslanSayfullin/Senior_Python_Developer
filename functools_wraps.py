import functools

def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Before the function is called")
        result = func(*args, **kwargs)
        print("After the function is called")
        return result
    return wrapper

@my_decorator
def my_function():
    """This is the docstring of my_function"""
    print("my_function is called")


print(my_function.__name__) # Вывод: "my_function"
print(my_function.__doc__)  # Вывод: "This is the docstring of my_function"
