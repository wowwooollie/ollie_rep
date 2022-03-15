"""
Write a function that accepts another function as an argument. Then it
should return such a function, so the every call to initial one
should be cached.


def func(a, b):
    return (a ** b) ** 2


cache_func = cache(func)

some = 100, 200

val_1 = cache_func(*some)
val_2 = cache_func(*some)

assert val_1 is val_2

"""
from datetime import datetime
from functools import lru_cache


def pow_func(a, b):
    return (a ** b) ** 2


def cache(func):
    @lru_cache()
    def inner_func(*args):
        return func(*args)
    return inner_func


cache_pow_func = cache(pow_func)
some = 1888888, 178888

then = datetime.utcnow()
val_1 = cache_pow_func(*some)
now = datetime.utcnow()
print(str((now - then).total_seconds()))  # 0.76659

then = datetime.utcnow()
val_2 = cache_pow_func(*some)
now = datetime.utcnow()
print(str((now - then).total_seconds()))  # 0.0


assert val_1 is val_2
