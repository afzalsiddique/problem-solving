import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def memLeak(self, memory1: int, memory2: int) -> List[int]:
        x=1
        while x<=memory1 or x<=memory2:
            if memory1>=memory2:
                memory1-=x
            else:
                memory2-=x
            x+=1
        return [x,memory1,memory2]

class MyTestCase(unittest.TestCase):
    def test1(self):
        memory1,memory2 = 2,  2
        Output= [3,1,0]
        self.assertEqual(Output, get_sol().memLeak(memory1,memory2))
    def test2(self):
        memory1,memory2 = 8,  11
        Output= [6,0,4]
        self.assertEqual(Output, get_sol().memLeak(memory1,memory2))
    # def test3(self):
    # def test4(self):
    # def test5(self):
    # def test6(self):
    # def test7(self):
