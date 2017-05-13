import functools
import time


def measured_func(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        total_time = time.time() - start_time
        print('{func} execution time is: {total_time}'.format(func=func.__name__, total_time=total_time))
        return result
    return wrapper

