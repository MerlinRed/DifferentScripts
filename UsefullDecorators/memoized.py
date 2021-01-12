from collections import OrderedDict
from functools import wraps


def memoized(func):
    global cache
    cache = OrderedDict()

    @wraps(func)
    def inner(*args, **kwargs):
        key = args + tuple(sorted(kwargs.items()))
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]

    return inner
