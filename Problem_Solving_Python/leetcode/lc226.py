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
    def invertTree(self, root: TreeNode) -> TreeNode:
        def helper(root:TreeNode):
            if not root:return None
            root.left,root.right = root.right, root.left
            if root.left:
                helper(root.left)
            if root.right:
                helper(root.right)
            return root

        return helper(root)