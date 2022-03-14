"""
Given a list of integers numbers "nums".

You need to find a sub-array with length less equal to "k", with maximal sum.

The written function should return the sum of this sub-array.

Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""
from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    max_sum = nums[0]
    for key, _ in enumerate(nums):
        for i in range(k):
            current_subarray_sum = sum(nums[key:key+i+1])
            if max_sum < current_subarray_sum:
                max_sum = current_subarray_sum
    return max_sum
