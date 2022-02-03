from itertools import accumulate; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import *
def get_sol(): return Solution4()
class Solution:
    # time O(n) space O(1). remove binary search call
    def increasingTriplet(self, A: List[int]) -> bool:
        li=[float('inf'),float('inf')]
        for x in A:
            # very similar to binary search
            # idx=bisect_left(li,x)
            if x<li[0]: # result of binary search is 0 -> idx=0
                li[0]=x
            elif x<li[1] and x>li[0]: # result of binary search is 1 -> idx=1
                li[1]=x
            elif x>li[1]: # result of binary search is 2 -> idx==2
                return True
        return False
class Solution4:
    # time O(n) space O(1)
    def increasingTriplet(self, A: List[int]) -> bool:
        li = [float('inf'),float('inf')] # space O(1). because len(li) is 2
        for x in A:
            idx=bisect_left(li,x) # time O(1). because len(li) is 2
            if idx==2:
                return True
            li[idx]=x
        return False
class Solution2:
    # time O(n) space O(1)
    def increasingTriplet(self, A: List[int]) -> bool:
        li = [] # space O(1). because the max len(li) is 3
        for x in A:
            idx=bisect_left(li,x) # time O(1). because max len(li) is 3
            if idx==len(li):
                li.append(x)
            else:
                li[idx]=x
            if len(li)==3:
                return True
        return False


class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(True, get_sol().increasingTriplet([1,2,3,4,5]))
    def test02(self):
        self.assertEqual(False, get_sol().increasingTriplet([5,4,3,2,1]))
    def test03(self):
        self.assertEqual(False, get_sol().increasingTriplet([1,1,-2,6]))
    def test04(self):
        self.assertEqual(True, get_sol().increasingTriplet([5,1,5,5,2,5,4]))
    def test05(self):
        self.assertEqual(True, get_sol().increasingTriplet([2,1,5,0,4,6]))
    def test06(self):
        self.assertEqual(True, get_sol().increasingTriplet([3,4,-1,5]))
    def test07(self):
        self.assertEqual(True, get_sol().increasingTriplet([20,100,10,12,5,13]))
