"""
Write a function that takes K lists as arguments and returns all possible
lists of K items where the first element is from the first list,
the second is from the second and so on.
You may assume that every list contain at least one element
Example:
assert combinations([1, 2], [3, 4]) == [
    [1, 3],
    [1, 4],
    [2, 3],
    [2, 4],
]
i_word chars = args[i][]
"""
from typing import List, Any
from itertools import product


def combinations(*args: List[Any]) -> List[tuple]:
    return list(product(*args))   # thought too much on the task and eventually did this :(


assert combinations([1, 2], [3, 4]) == [(1, 3), (1, 4), (2, 3), (2, 4)]