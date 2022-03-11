"""
Given a list of integers numbers "nums".

You need to find a sub-array with length less equal to "k", with maximal sum.

The written function should return the sum of this sub-array.

Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""
from typing import List
from itertools import combinations


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    result_list = []
    for j in range(1, k+1):
        comb_list = list(combinations(nums, j))
        for k in comb_list:
            result_list.append(sum(k))
    return max(result_list)
