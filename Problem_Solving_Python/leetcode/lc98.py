import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List; import functools
from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self): return str(self.val)
class Solution:
    # post order
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(node:TreeNode):
            if not node:
                return [float('inf'),float('-inf')]
            l=helper(node.left)
            r=helper(node.right)
            if not l or not r:
                return None
            minL,maxL=l
            minR,maxR=r
            if maxL>=node.val or minR<=node.val:
                return None
            return [min(minL,node.val),max(maxR,node.val)]

        ans=helper(root)
        if ans: return True
        return False
class Solution2:
    def isValidBST(self, root: TreeNode) -> bool:
        def valid(node: TreeNode,lo:int,hi:int):
            if not node: return True
            if not lo<node.val<hi: return False
            return valid(node.left,lo,node.val) and valid(node.right,node.val,hi)


        return valid(root,float('-inf'),float('inf'))


class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual(True, get_sol().isValidBST(deserialize("2,1,3")))
    def test2(self):
        self.assertEqual(False, get_sol().isValidBST(deserialize("5,1,4,null,null,3,6")))
    def test3(self):
        self.assertEqual(False, get_sol().isValidBST(deserialize("2,2,2")))
    def test4(self):
        self.assertEqual(False, get_sol().isValidBST(deserialize("5,4,6,null,null,3,7")))
    # def test5(self):
    # def test6(self):
    # def test7(self):

