from collections.abc import MutableMapping

class CustomDict(MutableMapping):
    def __init__(self):
        self.data = {}

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

    def __delitem__(self, key):
        del self.data[key]

    def __iter__(self):
        return iter(self.data)

    def __len__(self):
        return len(self.data)

my_dict = CustomDict()
my_dict['foo'] = 'bar'

print(my_dict['foo'])

my_dict['x'] = 10
print(my_dict['x'])

del my_dict['foo']
print(len(my_dict))
