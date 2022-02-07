from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left=[]
        right=[]
        pivots=[]
        for x in nums:
            if x<pivot:
                left.append(x)
            elif x>pivot:
                right.append(x)
            else:
                pivots.append(x)
        return left+pivots+right


class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual([9,5,3,10,10,12,14], get_sol().pivotArray([9,12,5,10,14,3,10], pivot = 10))
    def test02(self):
        self.assertEqual([-3,2,4,3], get_sol().pivotArray([-3,4,3,2], pivot = 2))
    # def test03(self):
    # def test04(self):
    # def test05(self):
    # def test06(self):
    # def test07(self):
    # def test08(self):
    # def test09(self):
