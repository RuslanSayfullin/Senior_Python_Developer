import pysnooper

@pysnooper.snoop()
def example_function():
    a = 10
    b = 20
    result = a + b
    return result

if __name__ == "__main__":
    example_function()
