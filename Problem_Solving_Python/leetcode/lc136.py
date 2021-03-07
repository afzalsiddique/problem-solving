import unittest
from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # XOR of two equal numbers is 0 : a^a=0. This is the main idea of the algorithm.
        res = 0
        for num in nums:
            res ^= num
        return res
