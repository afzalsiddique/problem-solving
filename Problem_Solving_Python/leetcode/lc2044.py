import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        def b(start,path):
            bit_or = list(itertools.accumulate(path,lambda a,b:a|b))
            bit_or = bit_or[-1] if bit_or else 0
            count[bit_or]+=1
            if start==n: return
            for i in range(start,n):
                b(i+1,path+[nums[i]])
            return

        n=len(nums)
        count=Counter()
        b(0,[])
        max_or=max(count.keys())
        return count[max_or]
class MyTestCase(unittest.TestCase):
    def test1(self):
        nums = [3,1]
        Output= 2
        self.assertEqual(Output, get_sol().countMaxOrSubsets(nums))
    def test2(self):
        nums = [2,2,2]
        Output= 7
        self.assertEqual(Output, get_sol().countMaxOrSubsets(nums))
    def test3(self):
        nums = [3,2,1,5]
        Output= 6
        self.assertEqual(Output, get_sol().countMaxOrSubsets(nums))
    # def test4(self):
    # def test5(self):
    # def test6(self):
