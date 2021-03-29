import unittest
from typing import List

# ***************** nums[i] != nums[i + 1] for all valid i ***************
class Solution:
    # https://www.youtube.com/watch?v=a7D77DdhlFc
    def findPeakElement(self, nums: List[int]) -> int:
        n=len(nums)
        lo,hi=0,n-1
        while lo<=hi:
            mid = (lo+hi)//2
            if (mid==0 or nums[mid-1]<nums[mid]) and (mid==n-1 or nums[mid]>nums[mid+1]):
                return mid
            elif mid>0 and nums[mid-1]>nums[mid]:
                hi=mid-1
            else:
                lo=mid+1
        return lo
class Solution2:
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

    def test1(self):
        self.assertEqual(2, Solution().findPeakElement([1,2,3,1]))
    def test2(self):
        self.assertEqual(3, Solution().findPeakElement([10,80,10,30,10,20,10]))