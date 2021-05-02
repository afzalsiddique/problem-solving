import unittest
from collections import deque
from typing import List
def get_sol_obj(): return Solution()


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n=len(nums)
        l,r=0,0
        cnt=0
        maxx=0
        while r<n:
            if cnt<k:
                if nums[r]==0:
                    cnt+=1
                r+=1
            elif cnt==k:
                if nums[r]==1:
                    r+=1
                else:
                    if nums[l]==0:
                        cnt-=1
                    l+=1
            maxx=max(maxx,r-l)
        return maxx


class MyTestCase(unittest.TestCase):
    def test_01(self):
        nums = [1,1,1,0,0,0,1,1,1,1,0]
        k = 2
        Output= 6
        self.assertEqual(Output, get_sol_obj().longestOnes(nums,k))
    def test_02(self):
        nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
        k = 3
        Output= 10
        self.assertEqual(Output, get_sol_obj().longestOnes(nums,k))
