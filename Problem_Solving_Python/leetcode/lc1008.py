import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List;
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution1_1()
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self): return str(self.val)
class Solution1_1:
    # without global variable
    # time O(n)
    def bstFromPreorder(self, preorder):
        preorder = preorder[::-1]
        def buildTree(upper_bound):
            if not preorder or preorder[-1] > upper_bound: return None
            node = TreeNode(preorder.pop())
            node.left = buildTree(node.val)
            node.right = buildTree(upper_bound)
            return node
        return buildTree(float('inf'))
class Solution1_2:
    # O(n). Only upper bound
    i = 0
    def bstFromPreorder(self, preorder):
        def helper(upper_bound):
            if self.i == len(preorder) or preorder[self.i] > upper_bound:
                return None
            root = TreeNode(preorder[self.i])
            self.i += 1
            root.left = helper( root.val)
            root.right = helper(upper_bound)
            return root
        return helper(float('inf'))
class Solution1_3:
    # using upper bound and lower bound. O(n)
    i=0
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder: return
        def helper(lo, hi):
            if self.i==len(preorder) or preorder[self.i]>hi or preorder[self.i]<lo:
                return
            root = TreeNode(preorder[self.i])
            self.i+=1
            root.left=helper(lo, root.val)
            root.right=helper(root.val, hi)
            return root

        return helper(float('-inf'),float('inf'))


class Solution2_1:
    # time O(n^2)
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        def insert(root,x):
            if not root: return TreeNode(x)
            if x<root.val:
                root.c=insert(root.c, x)
            else:
                root.right=insert(root.right,x)
            return root

        root=None
        for x in preorder:
            root=insert(root,x)
        return root
class Solution2_2:
    # time O(n)
    def bstFromPreorder(self, preorder):
        def helper(i, j):
            if i == j: return None
            root = TreeNode(preorder[i])
            mid = bisect(preorder, preorder[i], i + 1, j)
            root.left = helper(i + 1, mid)
            root.right = helper(mid, j)
            return root
        return helper(0, len(preorder))
class Solution2_3:
    # time O(n^2)
    def bstFromPreorder(self, preorder):
        def helper(preorder):
            if not preorder: return None
            root = TreeNode(preorder[0])
            i = bisect(preorder, preorder[0])
            root.left = helper(preorder[1:i])
            root.right = helper(preorder[i:])
            return root
        return helper(preorder)

class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(ser(des([8,5,10,1,7,None,12])),ser(get_sol().bstFromPreorder([8,5,1,7,10,12])))
    def test02(self):
        self.assertEqual(ser(des([1,None,3])),ser(get_sol().bstFromPreorder([1,3])))
    def test03(self):
        self.assertEqual(ser(des([4,2])),ser(get_sol().bstFromPreorder([4,2])))
    # def test04(self):
    # def test05(self):
    # def test06(self):
    # def test07(self):
    # def test08(self):
