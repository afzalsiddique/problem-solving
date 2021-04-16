# https://www.youtube.com/watch?v=dfIqLxAf-8s
# https://www.youtube.com/watch?v=-YiQZi3mLq0
import unittest
from typing import List


class Solution:
    # this will not work if array is in the range [0,n] (inclusive). It has to be [1,n]
    # floyd cycle detection by changing the input array
    def findDuplicate1(self, nums: List[int]) -> int:
        slow, fast = nums[0], nums[0]
        while True:
            slow = nums[slow]
            fast = nums[fast]
            fast = nums[fast]
            if slow == fast:
                break
        fast = nums[0]
        while slow!=fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow

    # this will work even if the array contains 0
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            idx = abs(nums[i])-1 # will work even if the array contains 0
            # idx = abs(nums[i]) # will not work if the array contains 0
            if nums[idx]<0:
                return abs(nums[i])
            else:
                nums[idx]*=-1
class MyTestCase(unittest.TestCase):
    def test_10(self):
        sol = Solution()
        expected = 4
        actual = sol.findDuplicate([3,4,1,4,2])
        self.assertEqual(expected, actual)
    # good example
    def test_1(self):
        sol = Solution()
        expected = 2
        actual = sol.findDuplicate([1,3,4,2,2])
        self.assertEqual(expected, actual)
    def test_11(self):
        sol = Solution()
        expected = 2
        actual = sol.findDuplicate([5,2,3,4,2,1])
        self.assertEqual(expected, actual)

    def test_20(self):
        sol = Solution()
        expected = 3
        actual = sol.findDuplicate([3,1,3,4,2])
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