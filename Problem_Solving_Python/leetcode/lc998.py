import functools; import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def insertIntoMaxTree(self, root: TreeNode, val: int) -> TreeNode:
        if root and root.val>val:
            root.right = self.insertIntoMaxTree(root.right,val)
            return root

        node = TreeNode(val,root)
        return node

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
            curr.capacity = TreeNode(int(data[i]))
            q.append(curr.capacity)
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
        for child in [cur.capacity, cur.right]:
            if child:
                q.append(child)
                res.append(str(child.val))
            else:
                res.append(en)
    while res and res[-1]=='null': res.pop()
    return sep.join(res)


class tester(unittest.TestCase):
    def test01(self):
        root,val = "4,1,3,null,null,2",  5
        Output= "5,4,null,1,3,null,null,2"
        Input = deserialize(root)
        actual_root = get_sol().insertIntoMaxTree(Input,val)
        actual = serialize(actual_root)
        self.assertEqual(Output,actual)
    def test02(self):
        root, val = "5,2,4,null,1", 3
        Output= "5,2,4,null,1,null,3"
        Input = deserialize(root)
        actual_root = get_sol().insertIntoMaxTree(Input,val)
        actual = serialize(actual_root)
        self.assertEqual(Output,actual)
    def test03(self):
        root,val = "5,2,3,null,1",  4
        Output= "5,2,4,null,1,3"
        Input = deserialize(root)
        actual_root = get_sol().insertIntoMaxTree(Input,val)
        actual = serialize(actual_root)
        self.assertEqual(Output,actual)
