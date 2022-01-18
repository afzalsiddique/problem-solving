from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import cache; from heapq import *; import unittest; from typing import List, Optional; import functools;from sortedcontainers import SortedList
# from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    def minWastedSpace(self, packages: List[int], sup: List[List[int]]) -> int:
        MOD=10**9+7
        packages.sort()
        summ=sum(packages)
        for x in sup: x.sort()
        res=float('inf')
        for B in sup:
            if packages[-1]>B[-1]: continue
            cur=0
            j=0
            for b in B:
                i=bisect_right(packages,b)
                cur+=(i-j)*b
                j=i
            res=min(res,cur-summ)
            res%=MOD
        return res if res!=float('inf') else -1
class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(6,get_sol().minWastedSpace( [2,3,5],  [[4,8],[2,8]]))
    def test02(self):
        self.assertEqual(-1,get_sol().minWastedSpace([2,3,5], [[1,4],[2,3],[3,4]]))
    def test03(self):
        self.assertEqual(9,get_sol().minWastedSpace([3,5,8,10,11,12],  [[12],[11,9],[10,5,14]]))
    # def test04(self):
    # def test05(self):

