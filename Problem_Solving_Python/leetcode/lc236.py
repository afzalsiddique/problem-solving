import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List; import functools
from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
# https://www.youtube.com/watch?v=13m9ZCB8gjw
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __repr__(self): return str(self.val)

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def helper(root):
            if not root: return None
            if root.val == p.val or root.val == q.val: return root
            left = helper(root.left)
            right = helper(root.right)
            if left and right:
                return root
            return left or right
        return helper(root)
class Solution2:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def func(node:TreeNode):
            nonlocal res
            if not node: return False
            foundInThisNode=False
            if node.val==p.val or node.val==q.val:
                foundInThisNode= True
            l,r=func(node.left),func(node.right)
            if not res: # common ancestor not yet found
                if l and r:
                    res=node
                elif (l or r) and foundInThisNode: # lowest common ancestor is one of the given nodes
                    res=node
            return l or r or foundInThisNode

        res=None
        func(root)
        return res
class Solution3:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # If looking for me, return myself
        if root == p or root == q:
            return root

        left = right = None
        # else look in left and right child
        if root.left:
            left = self.lowestCommonAncestor(root.left, p, q)

        # optimization. not required -> https://www.youtube.com/watch?v=13m9ZCB8gjw&t=5m39s
        if left and left != p and left != q:
            return left

        if root.right:
            right = self.lowestCommonAncestor(root.right, p, q)

        # if both children returned a node, means
        # both p and q found so parent is LCA
        if left and right:
            return root
        else:
            # either one of the chidren returned a node, meaning either p or q found on left or right branch.
            # Example: assuming 'p' found in left child, right child returned 'None'. This means 'q' is
            # somewhere below node where 'p' was found we dont need to search all the way,
            # because in such scenarios, node where 'p' found is LCA

            # if not left:
            #     return right
            # if not right:
            #     return left
            return left or right # short version of previous few lines
class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual(5, get_sol().lowestCommonAncestor(deserialize("3,5,1,6,2,0,8,null,null,7,4"), TreeNode(5), TreeNode(4)).val)
    def test2(self):
        self.assertEqual(1, get_sol().lowestCommonAncestor(deserialize("1,2"), TreeNode(1), TreeNode(2)).val)
    def test3(self):
        self.assertEqual(3, get_sol().lowestCommonAncestor(deserialize("3,5,1,6,2,0,8,null,null,7,4"), TreeNode(5), TreeNode(1)).val)
    # def test4(self):
    # def test5(self):
    # def test6(self):
    # def test7(self):
    # def test8(self):
