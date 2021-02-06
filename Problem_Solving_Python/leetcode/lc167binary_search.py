from bisect import bisect_left
from typing import List
import unittest


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for i in range(n):
            new_target = target - numbers[i]
            tmp = numbers[:i] + numbers[i + 1:]
            idx = bisect_left(tmp, new_target)
            if idx != len(tmp) and tmp[idx] == new_target:
                return [i + 1, idx + 2] # we need to return idx+2. because len(temp) = len(numbers)-1


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
