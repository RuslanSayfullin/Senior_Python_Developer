#узнаём возраст человека, по дате рождения
import datetime

birth_date = input("Введите дату рождения (дд.мм.гггг): ")
birth_date = datetime.datetime.strptime(birth_date, '%d.%m.%Y').date()  # преобразование строки в обьект даты
current_date = datetime.date.today()

age_years = current_date.year - birth_date.year
if current_date.month < birth_date.month or (current_date.month == birth_date.month and current_date.day < birth_date.day):
    age_years -= 1  # если день и месяц рождения в будущем относительно текущей даты, то вычитаем 1го

print(f"Вам сейчас {age_years} лет")
