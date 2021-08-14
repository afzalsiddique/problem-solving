import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        n=len(fronts)
        sett=set()
        minn=float('inf')
        for i in range(n):
            if fronts[i]==backs[i]:
                sett.add(fronts[i])
        for i in range(n):
            if fronts[i] not in sett:
                minn=min(minn,fronts[i])
            if backs[i] not in sett:
                minn=min(minn,backs[i])
        return minn if minn!=float('inf') else 0

class MyTestCase(unittest.TestCase):
    def test_1(self):
        fronts,backs = [1,2,4,4,7],[1,3,4,1,3]
        Output= 2
        self.assertEqual(Output, get_sol().flipgame(fronts,backs))
    def test_2(self):
        fronts,backs = [1],[1]
        Output= 0
        self.assertEqual(Output, get_sol().flipgame(fronts,backs))
    def test_3(self):
        fronts,backs = [1,1], [2,1]
        Output= 2
        self.assertEqual(Output, get_sol().flipgame(fronts,backs))
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
    # def test_9(self):
