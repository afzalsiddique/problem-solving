# https://www.youtube.com/watch?v=dfIqLxAf-8s
# https://www.youtube.com/watch?v=-YiQZi3mLq0
import unittest
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        p_slow, p_fast = nums[0], nums[0]
        while True:
            p_slow = nums[p_slow]
            p_fast = nums[nums[p_fast]]
            if p_slow == p_fast:
                break
        p_fast = nums[0]
        while p_slow!=p_fast:
            p_slow = nums[p_slow]
            p_fast = nums[p_fast]
        return p_slow

class MyTestCase(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        expected = 2
        actual = sol.findDuplicate([1,3,4,2,2])
        self.assertEqual(expected, actual)

    def test_2(self):
        sol = Solution()
        expected = 4
        actual = sol.findDuplicate([3,4,2,1,4])
        self.assertEqual(expected, actual)

    def test_3(self):
        sol = Solution()
        expected = 1
        actual = sol.findDuplicate([1,1])
        self.assertEqual(expected, actual)

    def test_4(self):
        sol = Solution()
        expected = 1
        actual = sol.findDuplicate([1,1,2])
        self.assertEqual(expected, actual)