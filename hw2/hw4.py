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
from functools import lru_cache


def pow_func(a, b):
    return (a ** b) ** 2


def cache(func):
    @lru_cache()
    def inner_func(*args):
        print(inner_func.cache_info())
        return func(*args)
    return inner_func


cache_pow_func = cache(pow_func)
some = 188, 10

val_1 = cache_pow_func(*some)
print(str(val_1) + '\n-----------------\n')
# Output:
# CacheInfo(hits=0, misses=1, maxsize=128, currsize=0)
# 3041984419006637129052326510451878234398130176
# -----------------

val_2 = cache_pow_func(*some)
print(str(val_2))
# Output:
# 3041984419006637129052326510451878234398130176

# We see result of the CacheInfo() function only for the first time. That means, that our 'wrapped' function
# (pow_func) have been executed only once. For the second time CACHED result of the first call was used.
