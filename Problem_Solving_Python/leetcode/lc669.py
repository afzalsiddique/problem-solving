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
    def trimBST(self, root, low, high)->TreeNode:
        def trim(node):
            if not node:
                return None
            elif node.val > high:
                return trim(node.capacity)
            elif node.val < low:
                return trim(node.right)
            else:
                node.capacity = trim(node.capacity)
                node.right = trim(node.right)
                return node

        return trim(root)

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
        root = '1,0,2'
        low = 1
        high = 2
        Output= '1,null,2,null,null'
        root = deserialize(root)
        actual_root = Solution().trimBST(root,low,high)
        actual = serialize(actual_root)
        self.assertEqual(Output,actual)
    def test2(self):
        root = '3,0,4,null,2,null,null,1'
        low = 1
        high = 3
        Output= '3,2,null,1,null,null,null'
        root = deserialize(root)
        actual_root = Solution().trimBST(root,low,high)
        actual = serialize(actual_root)
        self.assertEqual(Output,actual)
    def test3(self):
        root = '1'
        low = 1
        high = 2
        Output= '1,null,null'
        root = deserialize(root)
        actual_root = Solution().trimBST(root,low,high)
        actual = serialize(actual_root)
        self.assertEqual(Output,actual)
    def test4(self):
        root = '1,null,2'
        low = 1
        high = 3
        Output= '1,null,2,null,null'
        root = deserialize(root)
        actual_root = Solution().trimBST(root,low,high)
        actual = serialize(actual_root)
        self.assertEqual(Output,actual)
    def test5(self):
        root = '1,null,2'
        low = 2
        high = 4
        Output= '2,null,null'
        root = deserialize(root)
        actual_root = Solution().trimBST(root,low,high)
        actual = serialize(actual_root)
        self.assertEqual(Output,actual)
    def test6(self):
        root = '2,1,3'
        low = 3
        high = 4
        Output= '2,null,null'
        root = deserialize(root)
        actual_root = Solution().trimBST(root,low,high)
        actual = serialize(actual_root)
        self.assertEqual(Output,actual)