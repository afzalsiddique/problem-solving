from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self): return str(self.val)
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        def trim(node):
            if not node:
                return None
            node.left=trim(node.left)
            node.right=trim(node.right)
            if low<=node.val<=high:
                return node
            return node.left or node.right

        return trim(root)
class Solution2:
    def trimBST(self, root, low, high)->TreeNode:
        def trim(node):
            if not node:
                return None
            elif node.val > high:
                return trim(node.left)
            elif node.val < low:
                return trim(node.right)
            else:
                node.left = trim(node.left)
                node.right = trim(node.right)
                return node

        return trim(root)


class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(ser(des([1,None,2])),ser(get_sol().trimBST(des([1,0,2]), 1, 2)))
    def test2(self):
        self.assertEqual(ser(des([3,2,None,1])),ser(get_sol().trimBST(des([3,0,4,None,2,None,None,1]), 1, 3)))
    def test3(self):
        self.assertEqual(ser(des([1])),ser(get_sol().trimBST(des([1]), 1, 2)))
    def test4(self):
        self.assertEqual(ser(des([1,None,2])),ser(get_sol().trimBST(des([1,None,2]), 1, 3)))
    def test5(self):
        self.assertEqual(ser(des([2,None,None])),ser(get_sol().trimBST(des([1,None,2]), 2, 4)))
    # def test6(self):
