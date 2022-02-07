from itertools import accumulate; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    ### recursive  ####
    def __init__(self):
        self.max_level = -1
    def rightSideView(self, root: TreeNode) -> List[int]:
        result = []
        def helper(node:TreeNode, level:int):
            if node is None: return None

            if level>self.max_level:
                self.max_level=level
                result.append(node.val)

            helper(node.right,level+1)
            helper(node.left, level+1)


        helper(root,0)
        return result

class Solution2:
    ### iterative  ###
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:return []
        q = deque()
        res = []
        q.append((root))
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:q.append(node.left)
                if node.right:q.append(node.right)
            res.append(node.data)
        return res


class Solution3:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:return []
        q = deque()
        res = []
        q.append((root,1))
        while q:
            node, level = q.popleft()
            if q and q[0][1]==level+1: # the last node in the level
                res.append(node.data)
            if not q: # only one node in the level
                res.append(node.data)
            if node.left:
                q.append((node.left,level+1))
            if node.right:
                q.append((node.right, level+1))
        return res

class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual([1,3,4],get_sol().rightSideView(des([1,2,3,None,5,None,4])))
    def test02(self):
        self.assertEqual([1,3],get_sol().rightSideView(des([1,None,3])))
    def test03(self):
        self.assertEqual([],get_sol().rightSideView(des([])))
    # def test04(self):
    # def test05(self):
    # def test06(self):
    # def test07(self):
    # def test08(self):
    # def test09(self):
