def calculate_discount(price, discount):
    if discount < 0 or discount > 100:
        raise ValueError('Некорректная скидка')

    new_price = price * (1 - discount / 100)
    return new_price

price = 100
discount = -10

try:
    new_price = calculate_discount(price, discount)
except ValueError as e:
    print(e)

# Результат:
# Некорректная скидка

