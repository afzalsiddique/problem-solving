import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # time O(n)
    # https://leetcode.com/problems/max-number-of-k-sum-pairs/discuss/961351/C%2B%2B-Map-O(n)-and-Two-Pointer-O(nlogn)-easy-solution
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = Counter(nums)
        ans=0
        for num in count:
            if k-num in count:
                if num==k-num:
                    ans+=count[num]//2
                else:
                    minn=min(count[num],count[k-num])
                    count[num]-=minn
                    count[k-num]-=minn
                    ans+=minn
        return ans
class Solution2:
    # time O(nlogn)
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans=0
        left=0
        right=len(nums)-1
        while left<right:
            l,r=nums[left],nums[right]
            if l+r==k:
                ans+=1
                left+=1
                right-=1
            elif l+r>k:
                right-=1
            else:
                left+=1
        return ans


class MyTestCase(unittest.TestCase):
    def test_01(self):
        nums = [1,2,3,4]
        k = 5
        Output= 2
        self.assertEqual(Output,get_sol().maxOperations(nums,k))
    def test_02(self):
        nums = [3,1,3,4,3]
        k = 6
        Output= 1
        self.assertEqual(Output,get_sol().maxOperations(nums,k))
    def test_03(self):
        nums = [3,1,5,1,1,1,1,1,2,2,3,2,2]
        k = 1
        Output= 0
        self.assertEqual(Output,get_sol().maxOperations(nums,k))
    # def test_04(self):
    # def test_05(self):
    # def test_06(self):
    # def test_07(self):