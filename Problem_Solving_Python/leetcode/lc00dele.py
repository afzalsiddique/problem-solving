from itertools import accumulate,permutations; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import heappop,heappush,heapify; import unittest; from typing import List, Optional, Union, \
    Dict; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
from Problem_Solving_Python.template.binary_tree import deserialize,serialize

def get_sol(): return Solution()
class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        di={2:'ase'}
        print(di.get(1,'nai'))
        print(di.get(2,'nai'))

class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(7, get_sol().maxEqualFreq([2,2,1,1,5,3,3,5]))
    def test02(self):
        self.assertEqual(13, get_sol().maxEqualFreq([1,1,1,2,2,2,3,3,3,4,4,4,5]))
    def test03(self):
        self.assertEqual(5, get_sol().maxEqualFreq([8,3,8,5,2,3,7]))
    def test04(self):
        self.assertEqual(5, get_sol().maxEqualFreq([3,4,4,4,4,1,3,5]))
    def test05(self):
        self.assertEqual(2, get_sol().maxEqualFreq([1,2]))
    def test06(self):
        self.assertEqual(7, get_sol().maxEqualFreq([1,1,1,2,2,2,3,3,3]))
    def test07(self):
        self.assertEqual(2, get_sol().maxEqualFreq([1,1]))
    def test08(self):
        self.assertEqual(6, get_sol().maxEqualFreq([4,4,4,4,4,4]))
    # def test09(self):
    # def test10(self):
