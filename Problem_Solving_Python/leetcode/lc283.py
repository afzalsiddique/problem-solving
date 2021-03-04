import unittest
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]):
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        j = 0
        for i in range(1,n):
            if nums[j]!=0:
                j+=1
            if nums[i]==0:
                continue
            if nums[j] == 0 and nums[i]!=0:
                nums[j],nums[i] = nums[i],nums[j]
                j+=1
        return nums



class MyTestCase(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        actual = sol.moveZeroes([0,1,0,3,12])
        expected = [1,3,12,0,0]
        self.assertEqual(expected, actual)

    def test_2(self):
        sol = Solution()
        actual = sol.moveZeroes([0,0,0,1,2,3])
        expected = [1,2,3,0,0,0]
        self.assertEqual(expected, actual)

    def test_3(self):
        sol = Solution()
        actual = sol.moveZeroes([1,2,3,4])
        expected = [1,2,3,4]
        self.assertEqual(expected, actual)

    def test_4(self):
        sol = Solution()
        actual = sol.moveZeroes([0,0,0,0,0,0])
        expected = [0,0,0,0,0,0]
        self.assertEqual(expected, actual)

    def test_5(self):
        sol = Solution()
        actual = sol.moveZeroes([1,3,12,0,0])
        expected = [1,3,12,0,0]
        self.assertEqual(expected, actual)

    def test_6(self):
        sol = Solution()
        actual = sol.moveZeroes([1,0,2,0,3,0])
        expected = [1,2,3,0,0,0]
        self.assertEqual(expected, actual)

    def test_7(self):
        sol = Solution()
        actual = sol.moveZeroes(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_8(self):
        sol = Solution()
        actual = sol.moveZeroes(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_9(self):
        sol = Solution()
        actual = sol.moveZeroes(0)
        expected = 0
        self.assertEqual(expected, actual)