# contest 227
import unittest
from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        cnt = 0
        for i in range(n-1):
            if nums[i]>nums[i+1]:
                cnt+=1
        if cnt==0:
            return True
        if cnt==1:
            if cnt==n-1:
                return True
            if nums[0] < nums[n-1]:
                return False
            return True
        return False

class MyTestCase(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        actual = sol.check(nums = [3,4,5,1,2])
        expected = True
        self.assertEqual(expected, actual)

    def test_2(self):
        sol = Solution()
        actual = sol.check(nums = [2,1,3,4])
        expected = False
        self.assertEqual(expected, actual)

    def test_3(self):
        sol = Solution()
        actual = sol.check(nums = [1,2,3])
        expected = True
        self.assertEqual(expected, actual)

    def test_4(self):
        sol = Solution()
        actual = sol.check(nums = [1,1,1])
        expected = True
        self.assertEqual(expected, actual)

    def test_5(self):
        sol = Solution()
        actual = sol.check(nums = [2,1])
        expected = True
        self.assertEqual(expected, actual)

    def test_6(self):
        sol = Solution()
        actual = sol.check(nums=[6,7,8,3,5,9])
        expected = False
        self.assertEqual(expected, actual)

    def test_7(self):
        sol = Solution()
        actual = sol.check(nums=[6,7,10,3,5,9])
        expected = False
        self.assertEqual(expected, actual)

    def test_8(self):
        sol = Solution()
        actual = sol.check(nums=[10,11,20,3,5,9])
        expected = True
        self.assertEqual(expected, actual)

    def test_9(self):
        sol = Solution()
        actual = sol.check([6,10,6])
        expected = True
        self.assertEqual(expected, actual)