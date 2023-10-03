from sympy import *

x = Symbol('x')
y = Symbol('y')

expression = x**2 + x*y + y **2
expression

# Результат
# x**2 + x*y + y **2

deriv = diff(expression, x)
deriv

# Результат:
# 2*x + y

# Здесь создаются символьные переменные x и y, задается выражение с ними.


