from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
from Problem_Solving_Python.template.binary_tree import deserialize
def get_sol(): return Solution()
class Solution:
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
        self.assertEqual(2, get_sol().minCameraCover(deserialize("0,null,1,null,2,3,4")))
    def test6(self):
        self.assertEqual(2, get_sol().minCameraCover(deserialize("0,1,2,null,null,null,3")))
