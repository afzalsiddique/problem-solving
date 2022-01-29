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
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def depth(node,prev):
            nonlocal res
            if not node:
                return 0
            l=depth(node.left,node.val)
            r=depth(node.right,node.val)
            res=max(res,l+r)
            if node.val==prev:
                return 1+max(l,r)
            return 0

        res=0
        depth(root,-1001)
        return res


class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(2,get_sol().longestUnivaluePath(des([5,4,5,1,1,5])))
    def test02(self):
        self.assertEqual(2,get_sol().longestUnivaluePath((des([1,4,5,4,4,5]))))
    def test03(self):
        self.assertEqual(0,get_sol().longestUnivaluePath((des([]))))
    def test04(self):
        self.assertEqual(2,get_sol().longestUnivaluePath((des([4,4,4]))))
    def test05(self):
        self.assertEqual(1,get_sol().longestUnivaluePath((des([5,5]))))
