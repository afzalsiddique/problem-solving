# https://www.youtube.com/watch?v=uJ8BAQ8lASE
import unittest
from collections import Counter
from typing import List


class Solution:
    def isPossible(self, nums):
        left = Counter(nums)
        end = Counter()
        for i in nums:
            if not left[i]: continue
            left[i] -= 1
            if end[i - 1] > 0:
                end[i - 1] -= 1
                end[i] += 1
            elif left[i + 1] and left[i + 2]:
                left[i + 1] -= 1
                left[i + 2] -= 1
                end[i + 2] += 1
            else:
                return False
        return True



class MyTestCase(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        actual = sol.isPossible(nums = [1,2,3,3,4,5])
        expected = True
        self.assertEqual(expected, actual)

    def test_2(self):
        sol = Solution()
        actual = sol.isPossible([1,2,3,3,4,4,5,5])
        expected = False
        self.assertEqual(expected, actual)

    def test_3(self):
        sol = Solution()
        actual = sol.isPossible(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_4(self):
        sol = Solution()
        actual = sol.isPossible(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_5(self):
        sol = Solution()
        actual = sol.isPossible(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_6(self):
        sol = Solution()
        actual = sol.isPossible(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_7(self):
        sol = Solution()
        actual = sol.isPossible(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_8(self):
        sol = Solution()
        actual = sol.isPossible(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_9(self):
        sol = Solution()
        actual = sol.isPossible(0)
        expected = 0
        self.assertEqual(expected, actual)