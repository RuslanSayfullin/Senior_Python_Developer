import itertools
import string

# Задаем символы, их которых будет состоять пароль (буквы и цифры)
characters = string.ascii_letters + string.digits

# Задаем длину пароля
password_length = 8

# Генерируем все возможные комбинации символов длиной password_length
password_combinations = itertools.product(characters, repeat=password_length)

# Перебираем все комбинации и выводим их
for password in password_combinations:
	password_str = ''.join(password)
	print(password_str)
