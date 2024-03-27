from datetime import datetime

# задаём дату, до которой нужно посчитать кол-во дней
date_str = '2022-12-31'
end_date = datetime.strtime(date_str, '%Y-%m%d')

# вычисляем текущую дату
today = datetime.today()

# вычисляем разницу между датами в днях 
days_left = (end_time - today).days

# выводим результат
print(f'осталось {days_left} дней до {date_str}')
