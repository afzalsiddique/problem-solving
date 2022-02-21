import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution3()
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
class Solution2:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        res=0
        di=defaultdict(int)
        di[0]=1
        curSum=0
        for x in nums:
            curSum+=x
            y=curSum%k
            if y in di:
                res+=di[y]
            di[y]+=1
        return res
class Solution3:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        res=0
        di=defaultdict(int)
        di[0]=1
        curSum=0
        for x in nums:
            curSum=(curSum+x)%k
            if curSum in di:
                res+=di[curSum]
            di[curSum]+=1
        return res
class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(7, get_sol().subarraysDivByK([4,5,0,-2,-3,1] ,5))
    def test02(self):
        self.assertEqual(1, get_sol().subarraysDivByK([-5] , 5))