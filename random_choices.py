import random

lst = [10, 25, 30, 45, 50, 65, 70, 85, 90, 105]
a = random.choices(lst, k=5)
print(a)

b = random.choices(lst, k=3)
print(b)
