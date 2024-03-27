from functools import cached_property

class Sample():
    @cached_property
    def value(self):
        print('Произвлодим вычисления ...')
        return 21 * 2

obj = Sample()
print(obj.value)
print(obj.value)
