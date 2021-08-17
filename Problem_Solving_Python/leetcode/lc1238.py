import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # tle
    def circularPermutation(self, n: int, start: int) -> List[int]:
        MAX=2**n
        powers={2**i for i in range(30)}
        res=[]
        def h(last,path):
            if len(path)==MAX and path[0]^path[-1] in powers:
                res.append(path)
                return
            for i in range(MAX):
                # tmp=i^last
                if i^last in powers and i not in path:
                    h(i,path+[i])

        h(start,[start])
        return res[-1]

class MyTestCase(unittest.TestCase):
    def test_1(self):
        n,start = 2, 3
        Output= [3,2,0,1]
        self.assertEqual(Output, get_sol().circularPermutation(n,start))
    def test_2(self):
        n,start = 3, 2
        Output= [2,6,7,5,4,0,1,3]
        self.assertEqual(Output, get_sol().circularPermutation(n,start))
    def test_3(self):
        n,start = 5, 14
        Output= [2,6,7,5,4,0,1,3]
        self.assertEqual(Output, get_sol().circularPermutation(n,start))
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
    # def test_9(self):