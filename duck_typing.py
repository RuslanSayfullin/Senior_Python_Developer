class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Weow!"

class Duck:
    def speak(self):
        return "Quack!"

def animal_sound(animal):
    return animal.speak()

dog = Dog()
cat = Cat()
duck= Duck()

print(animal_sound(dog))    # Вывод: Woof!
print(animal_sound(cat))    # Вывод: Weow!
print(animal_sound(duck))   # Вывод: Quack!
