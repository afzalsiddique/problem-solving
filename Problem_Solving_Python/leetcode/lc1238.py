import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # similar to leetcode 89
    def circularPermutation(self, n: int, start: int) -> List[int]:
        # When n=3, we can get the result based on n=2.
        #   00, 01, 11, 10 ->
        # (000,001,011,010 ), (110,111,101,100).
        # The two parts differ at their highest bit and the rest numbers of part two are exactly
        # symmetric of part one.
        res=deque([0])
        for i in range(n):
            for j in range(len(res)-1,-1,-1):
            # for j in reversed(range(2**i)): # also works
                tmp=res[j]|1<<i
                res.append(tmp)
        while res[0]!=start:
            res.append(res.popleft())
        return list(res)
class Solution2:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        res=deque([start])
        for i in range(n):
            for j in range(len(res)-1,-1,-1):
            # for j in reversed(range(2**i)): # also works
                tmp=res[j]^(1<<i) # xor
                res.append(tmp)
        return list(res)
class Solution3:
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
        Output= [14, 10, 11, 9, 8, 24, 25, 27, 26, 30, 31, 29, 28, 20, 21, 23, 22, 18, 19, 17, 16, 0, 1, 3, 2, 6, 7, 5, 4, 12, 13, 15]
        self.assertEqual(Output, get_sol().circularPermutation(n,start))
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
    # def test_9(self):
