from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        res=0
        while num1 and num2:
            if num1>=num2:
                num1-=num2
            else:
                num2-=num1
            res+=1
        return res

class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(3, get_sol().countOperations(2,3))
    def test2(self):
        self.assertEqual(1, get_sol().countOperations(10,10))
    # def test3(self):
    # def test4(self):
    # def test5(self):
    # def test6(self):
