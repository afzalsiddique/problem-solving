import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # similar to 239
    def maxResult(self, nums: List[int], k: int) -> int:
        n=len(nums)
        if n==1: return nums[0]
        q=deque()
        q.append((nums[0],0)) # score,idx
        for i in range(1,n):
            while q and q[0][1]<i-k:
                q.popleft()
            score,idx=q[0]
            new_score=score+nums[i]
            while q and q[-1][0]<=new_score:
                q.pop()
            q.append((new_score,i))
        return new_score
class Solution2:
    # TLE
    def maxResult(self, nums: List[int], k: int) -> int:
        n=len(nums)
        score=[float('-inf')]*n
        score[0]=nums[0]
        for i in range(n):
            for j in range(i+1,min(i+1+k,n)):
                score[j]=max(score[j],score[i]+nums[j])
        return score[-1]


class MyTestCase(unittest.TestCase):
    def test_1(self):
        nums,k = [1,-1,-2,4,-7,3], 2
        Output= 7
        self.assertEqual(Output, get_sol().maxResult(nums,k))
    def test_2(self):
        nums,k = [10,-5,-2,4,0,3], 3
        Output= 17
        self.assertEqual(Output, get_sol().maxResult(nums,k))
    def test_3(self):
        nums,k = [1,-5,-20,4,-1,3,-6,-3], 2
        Output= 0
        self.assertEqual(Output, get_sol().maxResult(nums,k))
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):