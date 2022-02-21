from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        return str(self.val)
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        def helper(root:TreeNode):
            if not root: return None
            root.left=helper(root.left)
            root.right=helper(root.right)
            if not root.left and not root.right and root.val==0: return None
            return root

        return helper(root)
class Solution2:
    def pruneTree(self, root):
        def containsOne(node):
            if not node: return False
            left = containsOne(node.left)
            right = containsOne(node.right)
            if not left: node.left = None
            if not right: node.right = None
            return node.val == 1 or left or right

        return root if containsOne(root) else None

class Solution3:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        def helper(root:TreeNode):
            if not root: return False
            if not root.left and not root.right:
                if root.val==0: return False
                if root.val==1: return True

            left = helper(root.left)
            if left==False:
                root.left=None
            right = helper(root.right)
            if right==False:
                root.right=None
            if not left and not right:
                return root.val==1
            return left or right

        ans = helper(root)
        if ans:
            return root
        return None
# wrong
class Solution4:
    def pruneTree(self, root):
        def containsOne(node):
            if not node: return None
            node.left=containsOne(node.left)
            node.right=containsOne(node.right)
            if node.val==1: return node
            if node.left and node.left.val==1: return node
            if node.right and node.right.val==1: return node
            return None

        return root if containsOne(root) else None



class tester(unittest.TestCase):
    def test01(self):
        self.assertEqual('1,1,1',ser(get_sol().pruneTree(des([1,1,1,0]))))
    def test02(self):
        self.assertEqual('1,null,0,null,1',ser(get_sol().pruneTree(des([1,None,0,0,1]))))
    def test03(self):
        self.assertEqual('1,null,1,null,1',ser(get_sol().pruneTree(des([1,0,1,0,0,0,1]))))
    def test04(self):
        self.assertEqual('1,1,0,1,1,null,1',ser(get_sol().pruneTree(des([1,1,0,1,1,0,1,0]))))
    def test05(self):
        self.assertEqual('0,null,1',ser(get_sol().pruneTree(des([0,0,1]))))
    def test06(self):
        self.assertEqual('0,null,0,1',ser(get_sol().pruneTree(des([0,None,0,1]))))
