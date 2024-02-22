from datetime import datetime

date_string = "22.02.2024 14:11"
format_string = "%d.%m.%Y %H:%M"

date_object = datetime.strftime(date_string, format_string)
print(date_object)
