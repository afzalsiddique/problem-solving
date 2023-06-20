from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional,Union; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
from Problem_Solving_Python.template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Di(defaultdict):
    def __missing__(self, key): return key
class Solution:
    def nextGreater(self, nums) -> List[int]:
        li = [1,2,3,4]
        li = list(filter(lambda x:x%2, li))
        print(li)

class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual(4,get_sol().nextGreater([]))
    # def test2(self):
    # def test3(self):
    # def test4(self):
    # def test5(self):
    # def test6(self):
    # def test7(self):
    # def test8(self):
    # def test9(self):
