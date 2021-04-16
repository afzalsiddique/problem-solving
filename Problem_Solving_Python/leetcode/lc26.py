import unittest
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        j=0
        for i in range(1, n):
            if nums[i]!=nums[j]:
                nums[j+1] = nums[i]
                j+=1
        return j+1

    def removeDuplicates2(self, nums: List[int]) -> int:
        n=len(nums)
        if n==0 or n==1: return n
        l,r=0,0
        while r<n:
            if nums[l]==nums[r]:
                r+=1
                continue
            nums[l+1]=nums[r]
            l+=1
            r+=1
        return l+1


class MyTestCase(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        actual = sol.removeDuplicates(nums = [0,0,1,1,1,2,2,3,3,4])
        expected = 5
        self.assertEqual(expected, actual)

    def test_2(self):
        sol = Solution()
        actual = sol.removeDuplicates([0,1,2,3,4])
        expected = 5
        self.assertEqual(expected, actual)

