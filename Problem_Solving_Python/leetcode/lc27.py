import unittest
from typing import List


class Solution:
    # def removeElement(self, nums: List[int], val: int) -> List:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        i=0
        for j in range(n):
            if nums[j] != val:
                nums[i] = nums[j]
                i+=1
        return i
        # return nums

class MyTestCase(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        x = '.'
        actual = sol.removeElement(nums = [0,1,2,2,3,0,4,2], val = 2)
        expected = [0,1,3,0,4,x,x,x]
        self.assertEqual(expected, actual)

    def test_2(self):
        sol = Solution()
        x = '.'
        actual = sol.removeElement(nums = [3,2,2,3], val = 3)
        expected = [2,2,x,x]
        self.assertEqual(expected, actual)

    def test_3(self):
        sol = Solution()
        actual = sol.removeElement(nums = [0,1,2,2,3,0,4,2], val = 2)
        expected = 5
        self.assertEqual(expected, actual)

    def test_4(self):
        sol = Solution()
        actual = sol.removeElement(nums = [3,2,2,3], val = 3)
        expected = 2
        self.assertEqual(expected, actual)

