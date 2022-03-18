from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def merge(node1:TreeNode,node2:TreeNode)->TreeNode:
            if not node1 or not node2:
                return node1 or node2
            node1.left=merge(node1.left,node2.left)
            node1.right=merge(node1.right,node2.right)
            node1.val+=node2.val
            return node1

        return merge(root1,root2)
class Solution2:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        def helper(root1:TreeNode, root2:TreeNode):
            if not root1 and not root2:return None
            if not root1 or not root2:return root1 or root2
            new_root = TreeNode(root1.val + root2.val)
            new_root.left = helper(root1.left,root2.left)
            new_root.right = helper(root1.right,root2.right)
            return new_root

        return helper(root1,root2)
class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(ser(des([3,4,5,5,4,None,7])), ser(get_sol().mergeTrees(des([1,3,2,5]),des([2,1,3,None,4,None,7]))))
    def test02(self):
        self.assertEqual(ser(des([2,2])), ser(get_sol().mergeTrees(des([1]),des([1,2]))))
    # def test_3(self):
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):
