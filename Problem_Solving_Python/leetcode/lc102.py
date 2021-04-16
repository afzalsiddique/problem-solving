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