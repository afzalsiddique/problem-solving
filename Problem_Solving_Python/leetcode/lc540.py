# https://leetcode.com/problems/single-element-in-a-sorted-array/discuss/100754/Java-Binary-Search-short-(7l)-O(log(n))-w-explanations
import unittest
from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        lo,hi=0,len(nums)-1
        while lo<hi:
            mid= (lo+hi)//2
            if mid%2==1:
                mid-=1
            if nums[mid]!=nums[mid+1]:
                hi=mid
            else:
                lo=mid+2
        return nums[lo]


class MyTestCase(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        expected = 2
        actual = sol.singleNonDuplicate([1,1,2,3,3,4,4,8,8])
        self.assertEqual(expected, actual)

    def test_2(self):
        sol = Solution()
        expected = 10
        actual = sol.singleNonDuplicate([3,3,7,7,10,11,11])
        self.assertEqual(expected, actual)

    def test_3(self):
        sol = Solution()
        expected = 2
        actual = sol.singleNonDuplicate([0,0,1,1,2,3,3,4,4,5,5,6,6])
        self.assertEqual(expected, actual)

    def test_4(self):
        sol = Solution()
        expected = 2
        actual = sol.singleNonDuplicate([0,0,1,1,2,3,3,4,4,5,5,6,6])
        self.assertEqual(expected, actual)

    def test_5(self):
        sol = Solution()
        expected = 4
        actual = sol.singleNonDuplicate([0,0,1,1,2,2,3,3,4,5,5])
        self.assertEqual(expected, actual)

    def test_6(self):
        sol = Solution()
        expected = 0
        actual = sol.singleNonDuplicate([0,1,1,2,2,3,3,4,4,5,5])
        self.assertEqual(expected, actual)

    def test_7(self):
        sol = Solution()
        expected = 6
        actual = sol.singleNonDuplicate([1,1,2,2,3,3,4,4,5,5,6])
        self.assertEqual(expected, actual)

    def test_8(self):
        sol = Solution()
        expected = 1
        actual = sol.singleNonDuplicate([1,2,2])
        self.assertEqual(expected, actual)

    def test_9(self):
        sol = Solution()
        expected = 2
        actual = sol.singleNonDuplicate([1,1,2])
        self.assertEqual(expected, actual)

    def test_10(self):
        sol = Solution()
        expected = 3
        actual = sol.singleNonDuplicate([1,1,2,2,3])
        self.assertEqual(expected, actual)

    def test_11(self):
        sol = Solution()
        expected = 1
        actual = sol.singleNonDuplicate([1])
        self.assertEqual(expected, actual)