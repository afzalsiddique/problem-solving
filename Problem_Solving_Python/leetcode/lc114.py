from itertools import accumulate; from math import floor,ceil; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt; from sortedcontainers import SortedList
from binary_tree_tester import *; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self): return str(self.val)
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        def post(node):
            nonlocal last
            if not node: return
            post(node.right)
            post(node.left)
            node.right=last
            node.left=None
            last=node
            return


        last=None
        post(root)
        return root

class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual('1,null,2,null,3,null,4,null,5,null,6',ser(get_sol().flatten(des([1,2,5,3,4,None,6]))))
    def test02(self):
        self.assertEqual('',ser(get_sol().flatten(des([]))))
    def test03(self):
        self.assertEqual('0',ser(get_sol().flatten(des([0]))))
    # def test04(self):
    # def test05(self):
