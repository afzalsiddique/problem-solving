import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self): return str(self.val)
class Solution:
    # https://leetcode.com/problems/insufficient-nodes-in-root-to-leaf-paths/discuss/308326/JavaC%2B%2BPython-Easy-and-Concise-Recursion
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        def dfs(root,limit):
            if not root: return None
            if not root.left and not root.right:
                if limit>root.val:
                    return None
                return root
            root.left=dfs(root.left,limit-root.val)
            root.right=dfs(root.right,limit-root.val)
            if not root.left and not root.right:
                return None
            return root

        return dfs(root,limit)

def deserialize(data): # for unit testing
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
def serialize(root): # for unit testing
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
    while res and res[-1]=='null': res.pop()
    return sep.join(res)
class tester(unittest.TestCase):
    def test1(self):
        root,limit = "1,2,3,4,-99,-99,7,8,9,-99,-99,12,13,-99,14", 1
        root=deserialize(root)
        Output= "1,2,3,4,null,null,7,8,9,null,14"
        actual = serialize(get_sol().sufficientSubset(root,limit))
        self.assertEqual(Output,actual)
    def test2(self):
        root,limit = "5,4,8,11,null,17,4,7,1,null,null,5,3", 22
        root=deserialize(root)
        Output= "5,4,8,11,null,17,4,7,null,null,null,5"
        actual = serialize(get_sol().sufficientSubset(root,limit))
        self.assertEqual(Output,actual)
    def test3(self):
        root,limit = "1,2,-3,-5,null,4,null", -1
        root=deserialize(root)
        Output= "1,null,-3,4"
        actual = serialize(get_sol().sufficientSubset(root,limit))
        self.assertEqual(Output,actual)
    # def test4(self):
    # def test5(self):
    # def test6(self):
    # def test7(self):
