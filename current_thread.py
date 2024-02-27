import threading

def my_function():
    print(f"Идентификатор потока: {threading.current_thread().ident}")

t = threading.Thread(target=my_function)
t.start
