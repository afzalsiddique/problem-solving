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

# 1. If left sub tree height equals right sub tree height then,
#    a. left sub tree is perfect binary tree
#    b. right sub tree is complete binary tree
# 2. If left sub tree height greater than right sub tree height then,
#    a. left sub tree is complete binary tree
#    b. right sub tree is perfect binary tree
# time O((log n)^2)
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root: return 0

        def left_height(root):
            if not root: return 0
            h=0
            while root:
                h+=1
                root=root.left
            return h
        l=left_height(root.left)
        r=left_height(root.right)
        if l==r:
            return (1<<l) + self.countNodes(root.right)
        else:
            return (1<<r) + self.countNodes(root.left)


# very bad. time n, space n
class Solution2:
    def countNodes(self, root: TreeNode) -> int:
        if not root: return 0
        q,cnt=deque([root]),1
        while q:
            cur=q.popleft()
            if cur.left:
                q.append(cur.left)
                cnt+=1
            if cur.right:
                q.append(cur.right)
                cnt+=1
        return cnt