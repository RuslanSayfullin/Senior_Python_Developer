import datetime

now = datetime.datetime.now()

if now.month in (1, 2, 12):
    season = 'зима'
elif now.month in (3, 4, 5):
    season = 'весна'
elif now.month in (6, 7, 8):
    season = 'лето'
elif now.month in (9, 10, 11):
    season = 'осень'

print('Текуще время года: ', season)
