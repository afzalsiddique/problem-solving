import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:return [[]]
        res=[]
        q = deque([root])
        while q:
            tmp = []
            for _ in range(len(q)):
                node = q.popleft()
                tmp.append(node)
                if node.left:q.append(node.left)
                if node.right:q.append(node.right)
            res.append(tmp)
        return res
class Solution2:
    # recursion using dict
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        di=defaultdict(list)
        def helper(root,row):
            if not root: return
            di[row].append(root.val)
            helper(root.left, row + 1)
            helper(root.right,row+1)

        helper(root,0)
        res=[]
        for key in sorted(di.keys()):
            res.append(di[key])
        return res
