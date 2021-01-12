import time
from functools import wraps


def measurement_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result_func = func(*args, **kwargs)
        finish = time.perf_counter() - start
        print(f'Функция {func} работала: {finish: 0.2f} - секунд')
        return result_func

    return wrapper


def async_measurement_time(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result_func = await func(*args, **kwargs)
        finish = time.perf_counter() - start
        print(f'Функция {func} работала: {finish: 0.2f} - секунд')
        return result_func

    return wrapper
