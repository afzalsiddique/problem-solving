import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        MOD=10**9+7; BIG=22; res=0
        pow_2=[2**i for i in range(BIG)]
        di=defaultdict(int)
        for x in deliciousness:
            for target in pow_2:
                res+=di[target-x]
                res%=MOD
            di[x]+=1
        return res
class MyTestCase(unittest.TestCase):
    def test_1(self):
        deliciousness = [1,3,5,7,9]
        Output= 4
        self.assertEqual(Output, get_sol().countPairs(deliciousness))
    def test_2(self):
        deliciousness = [1,1,1,3,3,3,7]
        Output= 15
        self.assertEqual(Output, get_sol().countPairs(deliciousness))
    def test_3(self):
        deliciousness = [149,107,1,63,0,1,6867,1325,5611,2581,39,89,46,18,12,20,22,234]
        Output= 12
        self.assertEqual(Output, get_sol().countPairs(deliciousness))
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):