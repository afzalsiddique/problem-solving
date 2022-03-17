from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
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
class Solution2:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q=deque([root])
        while q:
            for _ in range(len(q)):
                node=q.popleft()
                node.left,node.right=node.right,node.left
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
        return root
