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
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root: return 0
        q = deque([(root,0)])
        maxx=1
        while q:
            start,end=None,None
            for _ in range(len(q)):
                cur,i = q.popleft()
                if cur.left:
                    j=i*2
                    q.append((cur.left,j))
                    if start is None:
                        start=j
                    end=j
                if cur.right:
                    j=i*2+1
                    q.append((cur.right,j))
                    if start is None:
                        start=j
                    end=j
            if start is not None:
                maxx=max(maxx,end-start+1)
        return maxx

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
        root = deserialize('1,3,2,5,3,null,9')
        Output= 4
        self.assertEqual(Output,Solution().widthOfBinaryTree(root))
    def test2(self):
        root = deserialize('0,1,4,2,null,null,5,3,null,null,6')
        Output= 8
        self.assertEqual(Output,Solution().widthOfBinaryTree(root))
    def test3(self):
        root = deserialize('0,1,4,2,null,41,43,null,null,42,null,null,44')
        Output= 4
        self.assertEqual(Output,Solution().widthOfBinaryTree(root))
    def test4(self):
        root = deserialize('1,2,3,4,5,6,7')
        Output= 4
        self.assertEqual(Output,Solution().widthOfBinaryTree(root))
    def test5(self):
        root = deserialize('1')
        Output= 1
        self.assertEqual(Output,Solution().widthOfBinaryTree(root))