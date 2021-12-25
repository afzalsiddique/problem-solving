import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List; import functools
from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxSumBST(self, root: TreeNode) -> int:
        def helper(node:TreeNode):
            nonlocal res
            if not node:
                return float('inf'),float('-inf'),0
            l=helper(node.left)
            r=helper(node.right)
            if not l or not r:
                return None
            minL,maxL,sumL=l
            minR,maxR,sumR=r
            if maxL>=node.val or minR<=node.val:
                return None
            summ=sumL+sumR+node.val
            res=max(res,summ)
            return min(minL,node.val),max(maxR,node.val),summ

        res=float('-inf')
        helper(root)
        return max(res,0)



class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual(20, get_sol().maxSumBST(deserialize("1,4,3,2,4,2,5,null,null,null,null,null,null,4,6")))
    def test2(self):
        self.assertEqual(2, get_sol().maxSumBST(deserialize("4,3,null,1,2")))
    def test3(self):
        self.assertEqual(0, get_sol().maxSumBST(deserialize("-4,-2,-5")))
    def test4(self):
        self.assertEqual(14, get_sol().maxSumBST(deserialize("4,null,1,-5,4,null,-3,null,10")))
    def test5(self):
        self.assertEqual(14, get_sol().maxSumBST(deserialize("4,8,null,6,1,9,null,-5,4,null,null,null,-3,null,10")))
    def test6(self):
        self.assertEqual(11, get_sol().maxSumBST(deserialize("8,9,8,null,9,null,1,null,null,-3,5,null,-2,null,6")))
    # def test6(self):
    # def test7(self):

