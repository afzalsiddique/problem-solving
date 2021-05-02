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
    def __repr__(self):
        return str(self.val)
class Solution:
    def addOneRow(self, root: TreeNode, val: int, depth: int) -> TreeNode:
        if depth==1:
            return TreeNode(val,root)

        depth-=1
        q=deque([root])
        while depth:
            depth-=1
            for _ in range(len(q)):
                cur = q.popleft()
                if cur.left: q.append(cur.left)
                if cur.right: q.append(cur.right)
                if depth==0:
                    cur.left=TreeNode(val,cur.left,None)
                    cur.right=TreeNode(val,None,cur.right)
        return root


def deserialize(data):
    sep,en = ',','#'
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

def serialize(root):
    en = '#'
    sep = ','
    if not root: return ''

    q = deque()
    res = [str(root.val)]
    q.append(root)
    while q:
        cur = q.popleft()
        for child in [cur.left, cur.right]:
            if child:
                q.append(child)
                res.append(str(child.val))
            else:
                res.append(en)

    return sep.join(res)

class tester(unittest.TestCase):
    def test1(self):
        root = deserialize('4,2,6,3,1,5')
        val = 1
        depth = 2
        Output= '4,1,1,2,null,null,6,3,1,5'
        actual = Solution().addOneRow(root, val, depth)
        actual = serialize(actual)
        self.assertEqual(Output,actual)