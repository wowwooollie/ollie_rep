"""
Classic task, a kind of walnut for you

Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""
from typing import List
from itertools import product
import random


def zeros_from_four_lists_1(a: List[int], b: List[int], c: List[int], d: List[int]) -> List[tuple]:
    list_of_proper_indexes = []
    n = len(a)
    for i in range(0, n-1):
        for j in range(0, n-1):
            for k in range(0, n-1):
                for m in range(0, n-1):
                    sum_of_elements = a[i] + b[j] + c[k] + d[m]
                    if sum_of_elements == 0:
                        list_of_proper_indexes.append((i, j, k, m))
    return list_of_proper_indexes


N = random.randint(0, 1000)
A = []
B = []
C = []
D = []

for i in range(0, N):
    A.append(random.randint(-500, 500))
    B.append(random.randint(-500, 500))
    C.append(random.randint(-500, 500))
    D.append(random.randint(-500, 500))


def zeros_from_four_lists_2(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    lists = [a, b, c, d]
    combinations = list(product(*lists))
    counter = 0
    for combination in combinations:
        if sum(combination) == 0:
            counter += 1
    return counter


print(zeros_from_four_lists_2(A, B, C, D))
