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
    def maxSumBST(self, root: TreeNode) -> int:
        def valid(node: TreeNode,lo:int,hi:int):
            nonlocal res
            if not node: return True,0
            validL,summL=valid(node.left,lo,node.val)
            if validL:
                res=max(res,summL,summL+node.val)
            validR,summR=valid(node.right,node.val,hi)
            if validR:
                res=max(res,summR,summR+node.val)
            ans=summL+summR+node.val
            if validL and validR:
                res=max(res,ans)
            if not lo<node.val<hi: return False,0
            return validL and validR,ans


        res=float('-inf')
        valid(root,float('-inf'),float('inf'))
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
    # def test5(self):
    # def test6(self):
    # def test7(self):

