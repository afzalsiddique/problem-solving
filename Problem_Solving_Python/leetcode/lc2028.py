import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m=len(rolls)
        total = (m+n) * mean
        left = total - sum(rolls)
        if not n<=left<=6*n: return []

        res = [1 for _ in range(n)]
        left -= n
        i=0
        while left:
            tmp = min(left,5)
            res[i]+= tmp
            left-=tmp
            i+=1
        return res

class MyTestCase(unittest.TestCase):
    def test1(self):
        rolls = [3,2,4,3]
        mean = 4
        n = 2
        Output= [6,6]
        self.assertEqual(Output, get_sol().missingRolls(rolls,mean,n))
    def test2(self):
        rolls = [1,5,6]
        mean = 3
        n = 4
        Output= [2,3,2,2]
        self.assertEqual(Output, get_sol().missingRolls(rolls,mean,n))
    def test3(self):
        rolls = [1,2,3,4]
        mean = 6
        n = 4
        Output= []
        self.assertEqual(Output, get_sol().missingRolls(rolls,mean,n))
    def test4(self):
        rolls = [1]
        mean = 3
        n = 1
        Output= [5]
        self.assertEqual(Output, get_sol().missingRolls(rolls,mean,n))
    # def test5(self):
    # def test6(self):
