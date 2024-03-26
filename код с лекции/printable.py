from functools import wraps


def printable(old_function):

    @wraps(old_function)
    def new_function(*args, **kwargs):
        # код до вызова исходной функции

        print(f"Сейчас будет вызвана функция {old_function.__name__}")
        print(f"с аргументами {args} {kwargs}")
        result = old_function(*args, **kwargs)
        print(f"возвращен результат {result}")
        # код после  вызова исходной функции

        return result

    return new_function
