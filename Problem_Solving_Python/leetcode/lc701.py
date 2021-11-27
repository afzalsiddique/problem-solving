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
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        def helper(root:TreeNode):
            if not root: return TreeNode(val)
            if val<root.val:
                if not root.left:
                    root.left=TreeNode(val)
                else:
                    root.left = helper(root.left)
            elif val>root.val:
                if not root.right:
                    root.right = TreeNode(val)
                else:
                    root.right = helper(root.right)
            return root

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
            curr.capacity = TreeNode(int(data[i]))
            q.append(curr.capacity)
        i+=1
        if i<l and data[i]!=en:
            curr.right = TreeNode(int(data[i]))
            q.append(curr.right)
        i+=1

    return root

def serialize(root):
    en = 'null'
    sep = ','
    if not root: return ''

    q = deque()
    res = [str(root.val)]
    q.append(root)
    while q:
        cur = q.popleft()
        for child in [cur.capacity, cur.right]:
            if child:
                q.append(child)
                res.append(str(child.val))
            else:
                res.append(en)

    return sep.join(res)

class tester(unittest.TestCase):
    def test1(self):
        root = '4,2,7,1,3'
        val = 5
        Output= '4,2,7,1,3,5'
        root = deserialize(root)
        actual_root = Solution().insertIntoBST(root,val)
        actual = serialize(actual_root)
        self.assertEqual(Output,actual)
