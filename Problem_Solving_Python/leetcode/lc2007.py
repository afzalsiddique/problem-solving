import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed)&1: return []
        count = Counter(changed)
        res=[]
        if 0 in count:
            if count[0]&1:
                return []
            freq = count[0]//2
            res.extend([0]*freq)
            count.pop(0)

        li = sorted(list(set(changed)))
        for x in li:
            if count[x] and count[x*2]<count[x]:
                return []
            if count[x]:
                freq = count[x]
                count[x]=0
                count[x*2]-=freq
                res.extend([x]*freq)
        return res

class MyTestCase(unittest.TestCase):
    def test1(self):
        changed = [1,3,4,2,6,8]
        Output= [1,3,4]
        self.assertEqual(Output, get_sol().findOriginalArray(changed))
    def test2(self):
        changed = [6,3,0,1]
        Output= []
        self.assertEqual(Output, get_sol().findOriginalArray(changed))
    def test3(self):
        changed = [1]
        Output= []
        self.assertEqual(Output, get_sol().findOriginalArray(changed))
    def test4(self):
        changed = [0]
        Output= []
        self.assertEqual(Output, get_sol().findOriginalArray(changed))
    def test5(self):
        changed = [0,0]
        Output= [0]
        self.assertEqual(Output, get_sol().findOriginalArray(changed))
    def test6(self):
        changed = [0,0,0,0]
        Output= [0,0]
        self.assertEqual(Output, get_sol().findOriginalArray(changed))
    def test7(self):
        changed = [4,2,0]
        Output= []
        self.assertEqual(Output, get_sol().findOriginalArray(changed))
    # def test8(self):
    # def test9(self):
