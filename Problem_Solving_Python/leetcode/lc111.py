import math
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
    def minDepth(self, root: TreeNode) -> int:
        def helper(root:TreeNode):
            if not root.left and not root.right: return 1
            left,right = float('inf'),float('inf')
            if root.left:
                left = self.minDepth(root.left)
            if root.right:
                right = self.minDepth(root.right)
            return 1+min(left,right)

        if not root: return 0
        return helper(root)

def deserialize(data):
    sep,en = ',','null'
    data = data.split(sep)
    l = len(data)
    if l<1:return None
    root = TreeNode(int(data[0]))
    q = deque()
    q.append(root)
    i=1
    while i<l and q:

        curr = q.popleft()
        if data[i]!=en:
            curr.left = TreeNode(int(data[i]))
            q.append(curr.left)
        i+=1
        if i<l and data[i]!=en:
            curr.right = TreeNode(int(data[i]))
            q.append(curr.right)
        i+=1

    return root
class tester(unittest.TestCase):
    def test1(self):
        root = deserialize('3,9,20,null,null,15,7')
        Output= 2
        self.assertEqual(Output,Solution().minDepth(root))
    def test2(self):
        root = deserialize('2,null,3,null,4,null,5,null,6')
        Output= 5
        self.assertEqual(Output,Solution().minDepth(root))
