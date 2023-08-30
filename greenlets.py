import gevent

def task1():
    for i in range(5):
        print("Task 1 - Step", i)
        gevent.sleep(1)

def task2():
    for i in range(5):
        print("Task 2 - Step", i)
        gevent.sleep(1)

# Создаем гринлеты
greenlet1 = gevent.spawn(task1)
greenlet2 = gevent.spawn(task2)

# Ожидаем завершения гринлетов
gevent.joinall([greenlet1, greenlet2])
