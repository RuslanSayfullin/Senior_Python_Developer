import itertools
import string

# Задаём символы, из которых будет состоять пароль (буквы и цифры)
characters = string.ascii_letters + string.digits

# Задаём длину пароля
password_lenght = 4

# Генерируем все возможные комбинации символов длиной password_lenght
password_combinations = itertools.product(characters, repeat=password_lenght)

# Перебираем все комбинации и выводим их
for password in password_combinations:
    password_str = ''.join(password)
    print(password_str)
