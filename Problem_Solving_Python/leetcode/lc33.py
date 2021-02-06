import unittest
from bisect import bisect_left
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        lo,hi=0,n-1
        while lo<=hi:
            mid=(lo+hi)//2

            if nums[mid]==target:
                return mid

            if nums[lo]<=nums[mid]:
                if nums[lo]<=target<=nums[mid]:
                    idx=bisect_left(nums,target,lo,hi)
                    return idx if idx!=n and nums[idx]==target else -1
                else:
                    lo=mid+1
            elif nums[mid]<=nums[hi]:
                if nums[mid]<=target<=nums[hi]:
                    idx=bisect_left(nums,target,lo,hi)
                    return idx if idx!=n and nums[idx]==target else -1
                else:
                    hi=mid-1
        return -1



class MyTestCase(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        expected = 4
        actual = sol.search(nums = [4,5,6,7,0,1,2], target = 0)
        self.assertEqual(expected, actual)

    def test_2(self):
        sol = Solution()
        expected = -1
        actual = sol.search(nums = [4,5,6,7,0,1,2], target = 3)
        self.assertEqual(expected, actual)
    #
    def test_3(self):
        sol = Solution()
        expected = -1
        actual = sol.search(nums = [1], target = 0)
        self.assertEqual(expected, actual)

    def test_4(self):
        sol = Solution()
        expected = 0
        actual = sol.search(nums = [4,5,6,7,0,1,2], target = 4)
        self.assertEqual(expected, actual)

    def test_5(self):
        sol = Solution()
        expected = 6
        actual = sol.search(nums = [4,5,6,7,0,1,2], target = 2)
        self.assertEqual(expected, actual)

    def test_6(self):
        sol = Solution()
        expected = 2
        actual = sol.search(nums = [5,6,4], target = 4)
        self.assertEqual(expected, actual)

    def test_7(self):
        sol = Solution()
        expected = 1
        actual = sol.search(nums = [4,5,6], target = 5)
        self.assertEqual(expected, actual)

    def test_8(self):
        sol = Solution()
        expected = 2
        actual = sol.search(nums = [4,5,6], target = 6)
        self.assertEqual(expected, actual)

    def test_9(self):
        sol = Solution()
        expected = 0
        actual = sol.search(nums = [4,5], target = 4)
        self.assertEqual(expected, actual)

    def test_10(self):
        sol = Solution()
        expected = 0
        actual = sol.search(nums = [5,4], target = 5)
        self.assertEqual(expected, actual)

    def test_11(self):
        sol = Solution()
        expected = -1
        actual = sol.search([1,3,5], 2)
        self.assertEqual(expected, actual)