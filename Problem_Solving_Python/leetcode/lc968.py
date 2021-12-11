import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List; import functools
from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        MONITORED_NOCAM='MONITORED_NOCAM'
        MONITORED_CAM='MONITORED_CAM'
        NOT_MONITORED='NOT_MONITORED'
        def dfs(node):
            nonlocal res
            if not node:
                return MONITORED_NOCAM
            left=dfs(node.left)
            right=dfs(node.right)
            if left==NOT_MONITORED or right==NOT_MONITORED:
                res+=1
                return MONITORED_CAM
            elif left==MONITORED_CAM or right==MONITORED_CAM:
                return MONITORED_NOCAM
            return NOT_MONITORED


        res=0
        ans=dfs(root)
        if ans==NOT_MONITORED: res+=1
        return res

class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(1, get_sol().minCameraCover(deserialize("0,1,null,2,3")))
    def test2(self):
        self.assertEqual(2, get_sol().minCameraCover(deserialize("0,1,null,2,null,3,null,null,4")))
    def test3(self):
        self.assertEqual(1, get_sol().minCameraCover(deserialize("0")))
    def test4(self):
        self.assertEqual(1, get_sol().minCameraCover(deserialize("0,0,0")))
    def test5(self):
        self.assertEqual(2, get_sol().minCameraCover(deserialize("0,null,0,null,0,0,0")))
