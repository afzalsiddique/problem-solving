from itertools import accumulate,permutations; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import heappop,heappush,heapify; import unittest; from typing import List, Optional, Union; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list, ListNode
from Problem_Solving_Python.template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        def ways(a,b):
            li = [a+b,a-b,b-a,a*b]
            if b!=0: li.append(a/b)
            if a!=0: li.append(b/a)
            return li




class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(23,get_sol().removeBoxes([1,3,2,2,2,3,4,3,1]))
    def test02(self):
        self.assertEqual(9,get_sol().removeBoxes([1,1,1]))
    def test03(self):
        self.assertEqual(1,get_sol().removeBoxes([1]))
    def test04(self):
        self.assertEqual(15,get_sol().removeBoxes([5,8,8,4,8,5,4]))
    def test05(self):
        self.assertEqual(18,get_sol().removeBoxes([5,8,3,8,4,8,5,7,4,2]))
    def test06(self):
        self.assertEqual(5,get_sol().removeBoxes([5,8,8]))
    # def test07(self):
    # def test08(self):
    # def test09(self):
