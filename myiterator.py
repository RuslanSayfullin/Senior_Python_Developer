class MyIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def _iter__(self):
        return self

    def __next__(self):
        if self.current < self.end:
            result = self.current
            self.current += 1
            return result
        else:
            raise StopIteration

# Пример использования:
my_iterator = MyIterator(1, 5)

for item in my_iterator:
    print(item)
