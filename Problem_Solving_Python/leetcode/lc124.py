from itertools import accumulate; from math import floor,ceil; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt; from sortedcontainers import SortedList
from binary_tree_tester import *; from a_linked_list import make_linked_list
def get_sol(): return Solution()

# https://www.youtube.com/watch?v=6cA_NDtpyz8
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        return str(self.val)
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def helper(node):
            nonlocal res
            if not node: return 0
            l=helper(node.left)
            r=helper(node.right)
            tmp=node.val+max(0,l,r,l+r) # take node or node+left or node+right or node+left+right
            res=max(res,tmp)
            # take node or node+left or node+right.
            # if node+left+right is taken then path will be broken in the parent node
            return node.val+max(0,l,r)

        res=float('-inf')
        helper(root)
        return res
class Solution3:
    def __init__(self):
        self.maxx = float('-inf')
    def maxPathSum(self, root: TreeNode) -> int:
        def postorder(root:TreeNode): # post order traversal
            if not root:return 0
            take_left=postorder(root.left)
            do_not_take_left=0
            left = max(take_left,do_not_take_left)
            take_right=postorder(root.right)
            do_not_take_right = 0
            right = max(take_right,do_not_take_right)
            self.maxx = max(self.maxx, left + right + root.val)
            return root.val + max(left, right)

        postorder(root)
        return self.maxx

class Solution2:
    def maxPathSum(self, root: TreeNode) -> int:
        self.maxx = float('-inf')
        def postorder(root:TreeNode):
            if not root:return 0
            left = postorder(root.left)
            right = postorder(root.right)
            self.maxx = max(self.maxx, left+right+root.val)
            return max (max(left,right)+root.val, 0)

        postorder(root)
        return self.maxx



class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(6,get_sol().maxPathSum(des([1,2,3])))
    def test02(self):
        self.assertEqual(42,get_sol().maxPathSum(des([-10,9,20,None,None,15,7])))
    def test03(self):
        self.assertEqual(48,get_sol().maxPathSum(des([5,4,8,11,None,13,4,7,2,None,None,None,1])))
    def test04(self):
        self.assertEqual(28,get_sol().maxPathSum(des([5,4,8,11,4])))
    def test05(self):
        self.assertEqual(-1,get_sol().maxPathSum(des([-1,-2,-3])))
