from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from Problem_Solving_Python.template.binary_tree import deserialize


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

class Solution2:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        HAS_CAM,NO_CAM_BUT_MONI,NO_CAM_NO_MONI=1,0,-1
        def at_least_one_child_has_cam(l,r):
            return l==HAS_CAM or r==HAS_CAM
        def one_child_monitored(c):
            return c==HAS_CAM or c==NO_CAM_BUT_MONI
        def at_least_one_child_not_monitored(l,r):
            return not one_child_monitored(l) or not one_child_monitored(r)

        res=0
        def dfs(node):
            nonlocal res
            if not node:
                return NO_CAM_BUT_MONI
            l=dfs(node.left)
            r=dfs(node.right)
            if at_least_one_child_not_monitored(l,r):
                res+=1
                return HAS_CAM
            elif at_least_one_child_has_cam(l,r):
                return NO_CAM_BUT_MONI
            else:
                return NO_CAM_NO_MONI

        ans = dfs(root)
        if ans==NO_CAM_NO_MONI:
            res+=1
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
    def test6(self):
        self.assertEqual(2, get_sol().minCameraCover(deserialize("0,0,0,null,null,null,0")))