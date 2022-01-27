from itertools import accumulate; from math import floor,ceil; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt; from sortedcontainers import SortedList
from binary_tree_tester import *
def get_sol(): return Solution()
class Solution:
    # time O(m^2). though O(m) solution exists it is difficult
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        dir={'R':(0,1),'L':(0,-1),'U':(-1,0),'D':(1,0)}
        @cache
        def dfs(x,y,i):
            if i==m: return False
            dx,dy=dir[s[i]]
            if 0<=x+dx<n and 0<=y+dy<n:
                return 1+dfs(x+dx,y+dy,i+1)
            return 0

        m=len(s)
        x,y=startPos
        return [dfs(x,y,i) for i in range(m)]

class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual([1,5,4,3,1,0], get_sol().executeInstructions(3, [0,1], "RRDDLU"))
    def test02(self):
        self.assertEqual([4,1,0,0], get_sol().executeInstructions(2, [1,1], "LURD"))
    def test03(self):
        self.assertEqual([0,0,0,0], get_sol().executeInstructions(1,[0,0], "LRUD"))
    # def test04(self):
    # def test05(self):
    # def test06(self):
    # def test07(self):
