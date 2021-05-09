import math
import random
from bisect import bisect_left
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List
def get_sol(): return Solution()


class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        n=len(nums)
        prefix_sum=[nums[0]]
        for i in range(1,n):
            prefix_sum.append(prefix_sum[i-1]+nums[i])
        right=[n-1 for _ in range(0,n)]
        left=[0 for _ in range(0,n)]
        st=[]
        for i in range(n):
            while st and nums[i]<nums[st[-1]]:
                top = st.pop()
                right[top] = i-1
            st.append(i)
        st.clear()
        for i in reversed(range(n)):
            while st and nums[i]<nums[st[-1]]:
                top = st.pop()
                left[top] = i+1
            st.append(i)
        maxx=1
        for i in range(n):
            l=left[i]
            r=right[i]
            if l!=0:
                summ = prefix_sum[r]-prefix_sum[l-1]
            else:
                summ =prefix_sum[r]
            maxx=max(maxx,nums[i]*summ)
        return maxx % int(1e9+7)


class tester(unittest.TestCase):
    def test01(self):
        nums = [1,2,3,2]
        Output= 14
        self.assertEqual(Output,get_sol().maxSumMinProduct(nums))
    def test02(self):
        nums = [2,3,3,1,2]
        Output= 18
        self.assertEqual(Output,get_sol().maxSumMinProduct(nums))
    def test03(self):
        nums = [3,1,5,6,4,2]
        Output= 60
        self.assertEqual(Output,get_sol().maxSumMinProduct(nums))