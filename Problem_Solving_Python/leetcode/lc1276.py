import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        tmp = 1*4-1*2
        x=-2*cheeseSlices+1*tomatoSlices
        x/=tmp
        if x<0 or math.floor(x)!=math.ceil(x): return []
        y=4*cheeseSlices-1*tomatoSlices
        y/=tmp
        if y<0 or math.floor(y)!=math.ceil(y): return []
        return [int(x),int(y)]


class Tester(unittest.TestCase):
    def test_1(self):
        tomatoSlices,cheeseSlices = 16, 7
        Output= [1,6]
        self.assertEqual(Output,get_sol().numOfBurgers(tomatoSlices,cheeseSlices))
    def test_2(self):
        tomatoSlices,cheeseSlices = 17, 4
        Output= []
        self.assertEqual(Output,get_sol().numOfBurgers(tomatoSlices,cheeseSlices))
    def test_3(self):
        tomatoSlices,cheeseSlices = 4, 17
        Output= []
        self.assertEqual(Output,get_sol().numOfBurgers(tomatoSlices,cheeseSlices))
    def test_4(self):
        tomatoSlices,cheeseSlices = 0, 0
        Output= [0,0]
        self.assertEqual(Output,get_sol().numOfBurgers(tomatoSlices,cheeseSlices))
    def test_5(self):
        tomatoSlices,cheeseSlices = 2, 1
        Output= [0,1]
        self.assertEqual(Output,get_sol().numOfBurgers(tomatoSlices,cheeseSlices))
    # def test_6(self):
    # def test_7(self):
