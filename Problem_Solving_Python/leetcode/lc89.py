import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # When n=3, we can get the result based on n=2.
    #   00, 01, 11, 10 ->
    # (000,001,011,010 ), (110,111,101,100).
    # The two parts differ at their highest bit and the rest numbers of part two are exactly
    # symmetric of part one.
    def grayCode(self, n:int)->List[int]:
        res=[0]
        for i in range(n):
            for j in range(len(res)-1,-1,-1):
            # for j in reversed(range(2**i)): # also works
                tmp=res[j]|1<<i
                res.append(tmp)
        return res
class Solution2:
    # tle. backtracking
    def grayCode(self, n: int) -> List[int]:
        MAX=2**n
        powers={2**i for i in range(30)}
        self.res=[]
        def h(last):
            if len(path)==MAX and path[0]^path[-1] in powers:
                self.res.append(path[:])
                return
            for i in range(MAX):
                # tmp=i^last
                if i^last in powers and i not in path:
                    path.append(i)
                    h(i)
                    path.pop()

        path=[0]
        h(0)
        return self.res[-1]


class MyTestCase(unittest.TestCase):
    def test_1(self):
        n=1
        Output=[0,1]
        self.assertEqual(Output, get_sol().grayCode(n))
    def test_2(self):
        n=2
        Output='unknown'
        self.assertEqual(Output, get_sol().grayCode(n))
    def test_3(self):
        n=3
        Output='unknown'
        self.assertEqual(Output, get_sol().grayCode(n))
    def test_4(self):
        n=4
        Output='unknown'
        self.assertEqual(Output, get_sol().grayCode(n))
    def test_5(self):
        n=5
        Output='unknown'
        self.assertEqual(Output, get_sol().grayCode(n))
    def test_6(self):
        n=6
        Output='unknown'
        self.assertEqual(Output, get_sol().grayCode(n))
    # def test_7(self):
    # def test_8(self):
    # def test_9(self):
