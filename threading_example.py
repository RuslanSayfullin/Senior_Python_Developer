import threading

def my_function(arg):
    print(f"Поток {threading.current_thread().name} выполняет функцию с аргументом {arg}")

# Создаём два потока
thread1 = threading.Thread(target=my_function, args=(1,))
thread2 = threading.Thread(target=my_function, args=(2,))

# Запускаем потоки
thread1.start()
thread2.start()

# Ждём завершения потоки
thread1.join()
thread2.join()

print("Все потоки завершены")
