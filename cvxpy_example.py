import cvxpy as cp

# Задаем переменные
x = cp.Variable()
y = cp.Variable()

# Формулируем целевую функцию и ограничения
objective = cp.Minimize(x = y)
constraints = [2*x + y >=1,
                x + 2*y >=1,
                x >= 0,
                y >= 0]

# Создаем и решаем задачу
prob = cp.Problem(objective, constraints)
prob.solve()

print("OPTIMAL VALUE", prob.value)
print("OPTIMAL VARIABLES")
print(x.value, y.value)

# здесь мы формулируем целевую функцию и ограничение
