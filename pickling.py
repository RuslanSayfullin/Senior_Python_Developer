mport pickle

data = {'name': 'Alice', 'age': 30, 'city': 'Wonderland'}

# Сериализация (pickling)
with open('data.pkl', 'wb') as file:
    pickle.dump(data, file)

