import time
from functools import wraps


def with_attempts(sleep, attempts):

    number_of_calls = 0

    def decorator(
        old_function,
    ):

        @wraps(old_function)
        def new_function(*args, **kwargs):
            nonlocal number_of_calls
            error = None
            # код до вызова исходной функции
            for i in range(attempts):
                number_of_calls = number_of_calls + 1
                try:
                    result = old_function(*args, **kwargs)
                    return result
                except Exception as er:
                    print(
                        f"Exception {er} во время выполнения {old_function.__name__}"
                        f"с аргументами {args} {kwargs}"
                        f"попытка № {i} из {attempts}"
                    )
                    print(f"sleep({sleep})")
                    time.sleep(sleep)
                    error = er
            raise error

        return new_function

    return decorator


with_attempts_2_10 = with_attempts(sleep=2, attempts=10)
