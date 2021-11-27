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
    def findBottomLeftValue(self, root: TreeNode) -> int:
        q=deque([root])
        ans=root.val
        while q:
            for i in range(len(q)):
                cur=q.popleft()
                if i==0: ans = cur.val
                if cur.left: q.append(cur.left)
                if cur.right: q.append(cur.right)
        return ans

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
        root = deserialize([2,1,3])
        Output= 1
        self.assertEqual(Output,Solution().findBottomLeftValue(root))
    def test2(self):
        root = deserialize('1,2,3,4,null,5,6,null,null,7')
        Output= 7
        self.assertEqual(Output,Solution().findBottomLeftValue(root))