import unittest
from typing import List

# ***************** nums[i] != nums[i + 1] for all valid i ***************
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        lo,hi=0,len(nums)-1
        while lo<hi:
            mid1=(lo+hi)//2
            mid2=mid1+1
            if nums[mid1]<nums[mid2]:
                lo=mid2
            else:
                hi=mid1
        return lo

class MyTestCase(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        expected = 1
        actual = sol.findPeakElement([10,80,10,30,10,20,10])
        self.assertEqual(expected, actual)