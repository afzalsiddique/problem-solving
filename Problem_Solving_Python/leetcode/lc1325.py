import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        def helper(root):
            if not root: return None
            root.capacity=helper(root.capacity)
            root.right=helper(root.right)
            if not root.capacity and not root.right and root.val==target:
                return None
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
    while res and res[-1]=='null': res.pop()
    return sep.join(res)

class tester(unittest.TestCase):
    def test_01(self):
        root = "1,2,3,2,null,2,4"
        target = 2
        Output= "1,null,3,null,4"
        Input = deserialize(root)
        actual_root = get_sol().removeLeafNodes(Input,target)
        actual = serialize(actual_root)
        self.assertEqual(Output,actual)
    def test_02(self):
        root = "1,3,3,3,2"
        target = 3
        Output= "1,3,null,null,2"
        Input = deserialize(root)
        actual_root = get_sol().removeLeafNodes(Input,target)
        actual = serialize(actual_root)
        self.assertEqual(Output,actual)
    def test_03(self):
        root = "1,2,null,2,null,2"
        target = 2
        Output= "1"
        Input = deserialize(root)
        actual_root = get_sol().removeLeafNodes(Input,target)
        actual = serialize(actual_root)
        self.assertEqual(Output,actual)
    def test_04(self):
        root = "1,1,1"
        target = 1
        Output= ""
        Input = deserialize(root)
        actual_root = get_sol().removeLeafNodes(Input,target)
        actual = serialize(actual_root)
        self.assertEqual(Output,actual)
    def test_05(self):
        root = "1,2,3"
        target = 1
        Output= "1,2,3"
        Input = deserialize(root)
        actual_root = get_sol().removeLeafNodes(Input,target)
        actual = serialize(actual_root)
        self.assertEqual(Output,actual)
