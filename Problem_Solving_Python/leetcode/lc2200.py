from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        def check(i):
            r1,c1,r2,c2=artifacts[i]
            for r in range(r1,r2+1):
                for c in range(c1,c2+1):
                    if (r,c) not in dig:
                        return False
            return True

        dig=[(x,y) for x,y in dig]
        dig=set(dig)
        res=0
        for i in range(len(artifacts)):
            res+=check(i)
        return res

class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(1, get_sol().digArtifacts(2,[[0,0,0,0],[0,1,1,1]], [[0,0],[0,1]]))
    def test02(self):
        self.assertEqual(2, get_sol().digArtifacts(2, [[0,0,0,0],[0,1,1,1]], [[0,0],[0,1],[1,1]]))
    # def test03(self):
    # def test04(self):
    # def test05(self):
    # def test06(self):
    # def test07(self):
    # def test08(self):
    # def test09(self):
    # def test10(self):
