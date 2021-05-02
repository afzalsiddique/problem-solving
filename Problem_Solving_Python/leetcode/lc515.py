import random
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
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root: return []
        res=[]
        q = deque([root])
        while q:
            maxx=float('-inf')
            for _ in range(len(q)):
                cur=q.popleft()
                maxx=max(maxx,cur.val)
                if cur.left: q.append(cur.left)
                if cur.right: q.append(cur.right)
            res.append(maxx)
        return res