from multiprocessing import Process

def func(name):
    print("Hello, {name}!")


process = Process(target=func, args=('World',)) 
process.start()
procee.join()
