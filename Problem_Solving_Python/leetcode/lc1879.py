import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List, Optional; import functools;from sortedcontainers import SortedList
# from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/minimum-xor-sum-of-two-arrays/discuss/1238641/Bit-Mask/955316
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        def turnOn(mask,i): return mask|(1<<i)
        def isOn(mask,i): return mask&(1<<i)
        def countSetBits(mask):
            cnt=0
            while mask:
                mask&=mask-1
                cnt+=1
            return cnt

        n=len(nums1)
        dp=[[float('inf')]*(1<<n) for _ in range(n)]
        for j in range(n):
            dp[0][turnOn(0,j)]=nums1[0]^nums2[j]

        for i in range(1,n):
            for mask in range(1<<n):
                if countSetBits(mask)!=i: continue
                for j in range(n):
                    if isOn(mask,j): continue
                    dp[i][turnOn(mask,j)]=min(dp[i][turnOn(mask,j)],dp[i-1][mask]+(nums1[i]^nums2[j]))
        return dp[-1][-1]
class Solution2:
    # tle
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        def recurse(left, path):
            if not left:
                return sum(map(lambda x,y:x^y,nums1,path))
            res=float('inf')
            for i in range(len(left)):
                res=min(res,recurse(left[:i]+left[i+1:],path+[left[i]]))
            return res


        return recurse(nums2,[])

class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual(2,get_sol().minimumXORSum( [1,2], [2,3]))
    def test2(self):
        self.assertEqual(8,get_sol().minimumXORSum( [1,0,3], [5,3,4]))
    def test3(self):
        self.assertEqual(8,get_sol().minimumXORSum([70,29,44,29,86,28,97,58,37,2], [53,71,82,12,23,80,92,37,15,95]))
    # def test4(self):
    # def test5(self):
