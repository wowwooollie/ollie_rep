"""
Some functions have a bit of cumbersome behavior when we deal with
positional and keyword arguments.
Write a function that accept any iterable of unique values, and then
it behaves as range function:
import string
assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']
"""
import string
from typing import List, Any


def custom_range(**kwargs) -> List[Any]:
    line = kwargs["iter_object"]
    stop = kwargs["stop"]
    if len(kwargs) == 2:
        return line[:line.index(stop)]
    elif len(kwargs) == 3:
        start = kwargs["start"]
        return line[line.index(start):line.index(stop)]
    elif len(kwargs) == 4:
        step = kwargs["step"]
        start = kwargs["start"]
        return line[line.index(start):line.index(stop):step]


def custom_range2(line, stop, start=None, step=None) -> List[Any]:
    if step is None:
        return line[:line.index(stop)]
    elif start is not None and step is not None:
        return line[line.index(start):line.index(stop):step]
    else:
        raise TypeError("""the function takes following sets of arguments:
        1)line and stop
        2)line, start and stop
        3) line, start, stop and step""")


# test_dict = {'iter_object': string.ascii_lowercase, 'stop': 'z', 'start': 'a', 'step': 2}
test_dict = {'iter_object': string.ascii_lowercase, 'stop': 'a', 'start': 'z', 'step': -1}
print(custom_range(**test_dict))  # calling the first option of the custom_range function

try:
    print(custom_range2(string.ascii_lowercase, 'h', step=2))  # calling the second option of the custom_range function
except TypeError as er:
    print(er)
