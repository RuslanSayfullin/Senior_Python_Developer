from typing import Literal

def example(justify: Literal['left', 'center', 'right']):
    return justify

print(example('left'))
print(example('another'))
