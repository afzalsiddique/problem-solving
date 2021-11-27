import itertools
import math
import operator
import random
from bisect import *
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List
def get_sol(): return Solution()

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self): return str(self.val)
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        gap_found = False
        q=deque([root])
        while q:
            for _ in range(len(q)):
                cur=q.popleft()
                if cur.left:
                    if gap_found: return False
                    q.append(cur.left)
                else:
                    gap_found=True
                if cur.right:
                    if gap_found: return False
                    q.append(cur.right)
                else:
                    gap_found=True
        return True
class Solution2:
    # wrong
    def isCompleteTree(self, root: TreeNode) -> bool:
        level=0
        q=deque([root])
        while q:
            width = len(q)
            for _ in range(width):
                cur = q.popleft()
                if cur.left: q.append(cur.left)
                if cur.right: q.append(cur.right)
            expected_width = pow(2,level)
            if expected_width!=width and len(q)!=0: return False
            level+=1
        return True
def serialize(root):
    en = 'null'
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
    while res and res[-1]==en: res.pop()
    return sep.join(res)
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

class mytestcase(unittest.TestCase):
    def test1_1(self):
        root = '1,2,3,4,5,6'
        Output= True
        root = deserialize(root)
        self.assertEqual(Output,get_sol().isCompleteTree(root))
    def test1_2(self):
        root = '1,2,3,4,5,null,7'
        Output= False
        root = deserialize(root)
        self.assertEqual(Output,get_sol().isCompleteTree(root))
