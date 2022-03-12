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
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def insert(node):
            if not node:
                return TreeNode(val)
            if val<node.val:
                node.left= insert(node.left)
            else:
                node.right= insert(node.right)
            return node

        return insert(root)
class Solution2:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        def helper(root:TreeNode):
            if not root: return TreeNode(val)
            if val<root.val:
                if not root.left:
                    root.left=TreeNode(val)
                else:
                    root.left = helper(root.left)
            elif val>root.val:
                if not root.right:
                    root.right = TreeNode(val)
                else:
                    root.right = helper(root.right)
            return root

        return helper(root)


class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(ser(des([4,2,7,1,3,5])),ser(get_sol().insertIntoBST(des([4,2,7,1,3]),5)))
    def test02(self):
        self.assertEqual(ser(des([40,20,60,10,30,50,70,None,None,25])),ser(get_sol().insertIntoBST(des([40,20,60,10,30,50,70]),25)))
    def test03(self):
        self.assertEqual(ser(des([4,2,7,1,3,5])),ser(get_sol().insertIntoBST(des([4,2,7,1,3,None,None,None,None,None,None]),5)))
    # def test04(self):
    # def test05(self):
