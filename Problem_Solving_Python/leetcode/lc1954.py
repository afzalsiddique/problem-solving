import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # bad solution
    def minimumPerimeter(self, neededApples: int) -> int:
        def uptosum(n):
            return n*(n+1)//2
        def sum_range(left,right):
            ans1 = uptosum(right)
            ans2 = uptosum(left-1)
            return ans1 - ans2
        def get_sum(i):
            ans1 = sum_range(i,i+i-1)
            ans2 = sum_range(i+1,i+i)
            return ans1 + ans2

        neededApples = math.ceil(neededApples/4)
        i=1
        while neededApples>0:
            neededApples -= get_sum(i)
            i+=1
        return (i-1)*2*4

class MyTestCase(unittest.TestCase):
    def test1(self):
        neededApples = 1
        Output= 8 # 2*4
        self.assertEqual(Output, get_sol().minimumPerimeter(neededApples))
    def test2(self):
        neededApples = 13
        Output= 16 # 4*4
        self.assertEqual(Output, get_sol().minimumPerimeter(neededApples))
    def test3(self):
        neededApples = 150
        Output= 24 # 6*4
        self.assertEqual(Output, get_sol().minimumPerimeter(neededApples))
    def test4(self):
        neededApples = 169
        Output= 32 # 8*4
        self.assertEqual(Output, get_sol().minimumPerimeter(neededApples))
    def test5(self):
        neededApples = 361
        Output= 40 # 10*4
        self.assertEqual(Output, get_sol().minimumPerimeter(neededApples))
    def test6(self):
        neededApples = 1000000000
        Output= 5040
        self.assertEqual(Output, get_sol().minimumPerimeter(neededApples))
    # def test7(self):
    # def test8(self):
