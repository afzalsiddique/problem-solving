from bisect import bisect_left
from typing import List
import unittest


class Solution:
    def twoSum(self, numbers, target):
        dic = {}
        for i, num in enumerate(numbers):
            if target - num in dic:
                return [dic[target - num] + 1, i + 1]
            dic[num] = i



class MyTestCase(unittest.TestCase):

    def test_1(self):
        solution = Solution()
        self.assertEqual([1, 2], solution.twoSum(numbers=[2, 7, 11, 15], target=9))

    def test_2(self):
        solution = Solution()
        self.assertEqual([1, 3], solution.twoSum(numbers=[2, 3, 4], target=6))

    def test_3(self):
        solution = Solution()
        self.assertEqual([1, 2], solution.twoSum(numbers=[-1, 0], target=-1))

    def test_4(self):
        solution = Solution()
        self.assertEqual([3, 6], solution.twoSum(numbers=[3,24,50,79,88,150,345], target=200))

    def test_5(self):
        solution = Solution()
        self.assertEqual([2,3], solution.twoSum(numbers=[5,25,75], target=100))
