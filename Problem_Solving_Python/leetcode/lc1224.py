import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List, Optional; import functools
from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/maximum-equal-frequency/discuss/403628/Easy-Python-Solution-Concise-10-lines-Explained-O(N)/363435
    def maxEqualFreq(self, nums: List[int]) -> int:
        count=Counter()
        freq=Counter()
        maxFreq=0
        res=0
        for i,x in enumerate(nums):
            freq[count[x]]-=1
            count[x]+=1
            freq[count[x]]+=1
            maxFreq=max(maxFreq,count[x])
            if maxFreq==1:
                res=i+1
            elif maxFreq*freq[maxFreq]==i:
                res=i+1
            elif (maxFreq-1)*(freq[maxFreq-1]+1)==i:
                res=i+1
        return res
class Solution2:
    # bad solution
    def maxEqualFreq(self, nums: List[int]) -> int:
        def helper():
            sett=set(count.values())
            sett.discard(0)
            return len(sett)==1
        def valid():
            for key in count:
                count[key]-=1
                if helper():
                    return True
                count[key]+=1
            return False

        n=len(nums)
        count=Counter(nums)
        i=n-1
        while not valid():
            count[nums[i]]-=1
            i-=1
        return i+1

class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(7, get_sol().maxEqualFreq([2,2,1,1,5,3,3,5]))
    def test02(self):
        self.assertEqual(13, get_sol().maxEqualFreq([1,1,1,2,2,2,3,3,3,4,4,4,5]))
    def test03(self):
        self.assertEqual(5, get_sol().maxEqualFreq([8,3,8,5,2,3,7]))
    def test04(self):
        self.assertEqual(5, get_sol().maxEqualFreq([3,4,4,4,4,1,3,5]))
    def test05(self):
        self.assertEqual(2, get_sol().maxEqualFreq([1,2]))
    def test06(self):
        self.assertEqual(7, get_sol().maxEqualFreq([1,1,1,2,2,2,3,3,3]))
    def test07(self):
        self.assertEqual(2, get_sol().maxEqualFreq([1,1]))
    def test08(self):
        self.assertEqual(6, get_sol().maxEqualFreq([4,4,4,4,4,4]))
    # def test09(self):
    # def test10(self):
