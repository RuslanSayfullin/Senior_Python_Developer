import arrow

# Арифметические операции
tomorrow = current_time.shift(days=1)
print(tomorrow)

# Формотирование даты
formatted_date = current_time.format('YYYY-MM-DD HH:mm:ss')
print(formatted_date)

# Извлечение компонентов даты
year = current_time.year
month = current_time.month
day = current_time.day
print(year, month, day)
