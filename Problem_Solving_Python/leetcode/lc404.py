from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self): return str(self.val)
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def recur(node, leftChild):
            if not node:
                return 0
            res=0
            if leftChild and not node.left and not node.right:
                res+=node.val
            res+= recur(node.left, True)
            res+= recur(node.right, False)
            return res

        return recur(root,False)
class Solution2:
    total = 0
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        def helper(root:TreeNode):
            if root.left and not root.left.left and not root.left.right:
                self.total += root.left.val
            if root.left:
                helper(root.left)
            if root.right:
                helper(root.right)

        helper(root)
        return self.total

class tester(unittest.TestCase):
    def test1(self):
        self.assertEqual(24,Solution().sumOfLeftLeaves(des([3,9,20,None,None,15,7])))
    def test2(self):
        self.assertEqual(0,Solution().sumOfLeftLeaves(des([1])))
    def test3(self):
        self.assertEqual(5,Solution().sumOfLeftLeaves(des([0,2,4,1,None,3,-1,5,1,None,6,None,8])))
    def test4(self):
        self.assertEqual(0,Solution().sumOfLeftLeaves(des([1,None,2])))
