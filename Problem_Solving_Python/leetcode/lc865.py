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
    # time O(n) space O(n)
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        def deep(node:TreeNode):
            if not node: return 0,None # depth,TreeNode
            left_depth,left_parent=deep(node.left)
            right_depth,right_parent=deep(node.right)
            if left_depth>right_depth:
                return left_depth+1,left_parent
            elif right_depth>left_depth:
                return right_depth+1,right_parent
            else:
                return 1+left_depth, node

        return deep(root)[1]

class Solution2:
    # time O(n) space O(n)
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        def depth(node):
            if not node:
                return 0
            return 1+max(depth(node.left),depth(node.right))
        def dfs(node,depth):
            if not node:
                return 0
            if depth==maxDepth:
                di[node]=1
                return 1
            di[node]=dfs(node.left,depth+1)+dfs(node.right,depth+1)
            return di[node]
        def smallest(node):
            if not node:
                return None
            if node.left in di and di[node.left]==di[node]:
                return smallest(node.left)
            if node.right in di and di[node.right]==di[node]:
                return smallest(node.right)
            return node

        di={}
        maxDepth=depth(root)
        dfs(root,1)
        return smallest(root)

class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual('2,7,4',ser(get_sol().subtreeWithAllDeepest(des([3,5,1,6,2,0,8,None,None,7,4]))))
    def test02(self):
        self.assertEqual('2,7,4',ser(get_sol().subtreeWithAllDeepest(des([5,6,2,None,None,7,4]))))
    def test03(self):
        self.assertEqual('1',ser(get_sol().subtreeWithAllDeepest(des([1]))))
