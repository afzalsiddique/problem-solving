import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def countTriples(self, n: int) -> int:
        ans=0
        for a in range(1,n+1):
            for b in range(1,n+1):
                tmp =int(math.sqrt(a*a+b*b))
                if tmp<=n and tmp*tmp==a*a+b*b:
                    # print(a,b,tmp)
                    ans+=1
        return ans

class tester(unittest.TestCase):
    def test_1(self):
        n = 5
        Output= 2
        self.assertEqual(Output,get_sol().countTriples(n))
    def test_2(self):
        n = 10
        Output= 4
        self.assertEqual(Output,get_sol().countTriples(n))
    def test_3(self):
        n = 190
        Output= 236
        self.assertEqual(Output,get_sol().countTriples(n))
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):
