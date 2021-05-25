import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        di,ans=defaultdict(int),0
        pre=[0] * n
        pre[0] = nums[0]
        for i in range(1,n):
            pre[i] = pre[i-1] + nums[i]
        for i in range(n):
            if pre[i]%k==0:ans+=1
            y= (pre[i]-k)%k
            if y in di:
                ans+=di[y]
            di[pre[i]%k]+=1
        return ans

class tester(unittest.TestCase):
    def test01(self):
        nums = [4,5,0,-2,-3,1]
        k = 5
        Output= 7
        self.assertEqual(Output, get_sol().subarraysDivByK(nums, k))
    def test02(self):
        nums = [-5]
        k = 5
        Output= 1
        self.assertEqual(Output, get_sol().subarraysDivByK(nums, k))