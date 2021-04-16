from bisect import bisect_left
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        def helper(root1:TreeNode, root2:TreeNode):
            if not root1 and not root2:return None
            if not root1 or not root2:return root1 or root2
            new_root = TreeNode(root1.val + root2.val)
            new_root.left = helper(root1.left,root2.left)
            new_root.right = helper(root1.right,root2.right)
            return new_root

        return helper(root1,root2)