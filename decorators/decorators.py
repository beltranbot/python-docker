import functools


def start_end_decorator(func):

    def wrapper(*arg, **args):
        print('Start')
        result = func(*arg, **args)
        print('End')

        return result

    return wrapper


def debug(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args] # repr returns the printable representation of a given object
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        result = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {result!r}")
        return result

    return wrapper


@debug
@start_end_decorator
def say_hello(name):
    """
        decorators are ran in the order they are listed
    """
    greeting = f'Hello {name}'
    print(greeting)
    return greeting


say_hello('Alex')
