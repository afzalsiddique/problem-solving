from itertools import accumulate; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/ways-to-split-array-into-three-subarrays/discuss/999257/C%2B%2BJavaPython-O(n)-with-picture
    def waysToSplit(self, nums: List[int]) -> int:
        MOD=10**9+7
        n=len(nums)
        pre=list(accumulate(nums))
        res=0
        j,k=0,0
        for i in range(n-2):
            while j<=i or (j<n-1 and pre[i]>pre[j]-pre[i]):
                j+=1
            while k<j or (k<n-1 and pre[-1]-pre[k]>=pre[k]-pre[i]):
                k+=1
            res = (res+(k-j))%MOD
        return res
class Solution2:
    # tle
    def waysToSplit(self, nums: List[int]) -> int:
        def h(A:List[int],a):
            n=len(A)
            total=sum(A)
            pre=list(accumulate(A))
            initial_left=bisect_left(pre,a)
            left=initial_left
            right=n-1
            while left<=right:
                mid=(left+right)//2
                if pre[mid]<=total-pre[mid]:
                    left=mid+1
                else:
                    right=mid-1
            return left-initial_left

        n=len(nums)
        pre=list(accumulate(nums))
        ans=0
        for i in range(1,n-1):
            ans+=h(nums[i:],pre[i-1])
        return ans

class MyTestCase(unittest.TestCase):
    def test_1(self):
        nums = [1,1,1]
        Output= 1
        self.assertEqual(Output, get_sol().waysToSplit(nums))
    def test_2(self):
        nums = [1,2,2,2,5,0]
        Output= 3
        self.assertEqual(Output, get_sol().waysToSplit(nums))
    def test_3(self):
        nums = [3,2,1]
        Output= 0
        self.assertEqual(Output, get_sol().waysToSplit(nums))
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
    # def test_9(self):