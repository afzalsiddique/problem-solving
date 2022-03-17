from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        def helper(root:TreeNode):
            if not root.left and not root.right: return 1
            left,right = float('inf'),float('inf')
            if root.left:
                left = self.minDepth(root.left)
            if root.right:
                right = self.minDepth(root.right)
            return 1+min(left,right)

        if not root: return 0
        return helper(root)

class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(2,get_sol().minDepth(des([3,9,20,None,None,15,7])))
    def test02(self):
        self.assertEqual(5,get_sol().minDepth(des([2,None,3,None,4,None,5,None,6])))
    def test03(self):
        self.assertEqual(0,get_sol().minDepth(des([])))
    # def test04(self):
    # def test05(self):
    # def test06(self):
    # def test07(self):
    # def test08(self):
    # def test09(self):
    # def test10(self):
