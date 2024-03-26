from functools import wraps


def template(old_function):

    @wraps(old_function)
    def new_function(*args, **kwargs):

        # код до вызова исходной фкнкции
        result = old_function(*args, **kwargs)
        # код после  вызова исходной фкнкции

        return result

    return new_function


def parametrized_tempalate(param_1, param_2):

    def decorator(
        old_function,
    ):
        @wraps(old_function)
        def new_function(*args, **kwargs):
            # код до вызова исходной фкнкции
            result = old_function(*args, **kwargs)
            # код после  вызова исходной фкнкции

            return result

        return new_function

    return decorator
