class File:
    def __init__(self, filename, mode):
        self.file = open(filename, mode)

    def __del__(self):
        # Деструктор - закрывает файл при удалении обьекта
        self.file.close()

f = File('data.txt', 'r')
# файл data.txt открыт

del f
# Вызывается __del__, закрывающий файл
# файл data.txt закрыт
