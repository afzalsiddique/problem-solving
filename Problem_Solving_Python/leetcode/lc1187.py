import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List, Optional; import functools
from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/make-array-strictly-increasing/discuss/377495/Java-dp-solution-:-A-simple-change-from-Longest-Increasing-Subsequence/412456
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        def check(start, end):
            if start+1==end:
                return 0
            min_val=arr1[start]
            max_val=arr1[end]
            idx=bisect_right(arr2,min_val)

            maxcount=end-start-1
            endi=idx+maxcount-1
            if endi<len(arr2) and arr2[endi]<max_val:
                return maxcount
            else:
                return -1

        arr2=list(set(arr2))
        arr2.sort()
        n=len(arr1)
        arr1=[float('-inf')]+arr1+[float('inf')]
        dp=[float('inf')]*(n+2)
        dp[0]=0
        for i in range(1,n+2):
            for j in range(i):
                if arr1[j]<arr1[i]:
                    change=check(j,i)
                    if change!=-1:
                        dp[i]=min(dp[i],dp[j]+change)

        res=dp[-1]
        return res if res!=float('inf') else -1

class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(1, get_sol().makeArrayIncreasing([1,5,3,6,7], [1,3,2,4]))
    def test02(self):
        self.assertEqual(2, get_sol().makeArrayIncreasing([1,5,3,6,7], [4,3,1]))
    def test03(self):
        self.assertEqual(-1, get_sol().makeArrayIncreasing([1,5,1,6,7], [1,6,3,3]))
    def test04(self):
        self.assertEqual(5, get_sol().makeArrayIncreasing([0,11,6,1,4,3], [5,4,11,10,1,0]))

