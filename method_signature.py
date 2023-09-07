import functools
import inspect

def check_signature(*arg_types, return_type=None):
    def decoration(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Получить сигнатуру метода
            signature = inspect.signature(func)
            bound_args = signature.bind(*args, **kwargs)

            # Проверить типы аргументов
            for param_name, param_value in bound_args.arguments.items():
                if param_name in arg_types and not isinstance(param_value, arg_types[param_name]):
                    raise TypeError(f"Argument '{param_name}' should be of type {arg_types[param_name].__name__}")

            # Вызвать метод
            result = func(*args, **kwargs)

            # Проверить тип возвращаемого значения
            if return_type is not None and not isinstance(result, return_type):
                raise TypeError(f"Return value should be of type {return_type.__name__}")

            return result
        return wrapper
    return decorator

# Пример использования
class MyClass:
    @check_signature(x=int, y=int, return_type=int)
    def add(self, x, y):
        return x + y

my_instance = MyClass()
result = my_instance.add(1, 2)      # Этот вызов будет успешным
result = my_instance.add(1, '2')    # Этот вызов взовет TypeError из-за неверного типа аргумента 'y'
