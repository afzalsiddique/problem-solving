from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def same(a,b):
            if not a and not b: return True
            if not a or not b: return False
            if a.val!=b.val: return False
            if not same(a.left,b.left):
                return False
            if not same(a.right,b.right):
                return False
            return True

        return same(p,q)


class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(True, get_sol().isSameTree(des([1,2,3]),des([1,2,3])))
    def test02(self):
        self.assertEqual(False, get_sol().isSameTree(des([1,2]),des([1,None,2])))
    def test03(self):
        self.assertEqual(False, get_sol().isSameTree(des([1,2,1]),des([1,1,2])))
    # def test04(self):
    # def test05(self):
    # def test06(self):
    # def test07(self):
