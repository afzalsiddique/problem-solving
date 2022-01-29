from itertools import accumulate; from math import floor,ceil; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt; from sortedcontainers import SortedList
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self): return str(self.val)
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def depth(node):
            nonlocal res
            if not node:
                return 0
            l=depth(node.left)
            r=depth(node.right)
            res=max(res,l+r) # update globally
            return 1+max(l,r)

        res=float('-inf')
        depth(root)
        return res


class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(3,get_sol().diameterOfBinaryTree(des([1,2,3,4,5])))
    def test02(self):
        self.assertEqual(1,get_sol().diameterOfBinaryTree(des([1,2])))
    # def test03(self):
    # def test04(self):
