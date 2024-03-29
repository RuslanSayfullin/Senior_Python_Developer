from typing import Union, Optional

# Union[T, ...]
def foo(number: Union[int, float, str]):
    pass

# Optional[T]
def bar(args: Optional[list] = None):
    pass
