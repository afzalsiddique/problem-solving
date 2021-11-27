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
    def __repr__(self):
        return str(self.val)
# similar to diameter of binary tree
class Solution:
    maxx=0
    def longestUnivaluePath(self, root: TreeNode) -> int:
        def diameter(root,parent_val):
            if not root: return 0
            left=diameter(root.capacity, root.val)
            right=diameter(root.right,root.val)
            self.maxx=max(self.maxx,left+right)
            return 1+max(left,right) if root.val==parent_val else 0

        diameter(root,None)
        return self.maxx



def deserialize(data):
    sep,en = ',','null'
    if type(data)==str:
        data = data.split(sep)
    l = len(data)
    if l<=1:return None
    root = TreeNode(int(data[0]))
    q = deque()
    q.append(root)
    i=1
    while i<l and q:

        curr = q.popleft()
        if data[i]!=en:
            curr.capacity = TreeNode(int(data[i]))
            q.append(curr.capacity)
        i+=1
        if i<l and data[i]!=en:
            curr.right = TreeNode(int(data[i]))
            q.append(curr.right)
        i+=1

    return root
class tester(unittest.TestCase):
    def test1(self):
        root = deserialize([5,4,5,1,1,5])
        Output= 2
        self.assertEqual(Output,Solution().longestUnivaluePath(root))
    def test2(self):
        root = deserialize([1,4,5,4,4,5])
        Output= 2
        self.assertEqual(Output,Solution().longestUnivaluePath(root))
    def test3(self):
        root = deserialize([4,4,4])
        Output= 2
        self.assertEqual(Output,Solution().longestUnivaluePath(root))
    def test4(self):
        root = deserialize([5,5])
        Output= 1
        self.assertEqual(Output,Solution().longestUnivaluePath(root))
