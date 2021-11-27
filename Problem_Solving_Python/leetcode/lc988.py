import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self): return str(self.val)
class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        li=[]
        def helper(root,path):
            if not root.capacity and not root.right:
                path.append(root.val)
                path=[chr(ord('a')+x) for x in path]
                li.append(''.join(path[::-1]))
                return
            if root.capacity: helper(root.capacity, path + [root.val])
            if root.right: helper(root.right,path+[root.val])

        helper(root,[])
        li.sort()
        # print(li)
        return li[0]

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
class MyTestCase(unittest.TestCase):
    def test_01(self):
        Input= "0,1,2,3,4,3,4"
        root=deserialize(Input)
        Output= "dba"
        self.assertEqual(Output,get_sol().smallestFromLeaf(root))
    def test_02(self):
        Input= "25,1,3,1,3,0,2"
        root=deserialize(Input)
        Output= "adz"
        self.assertEqual(Output,get_sol().smallestFromLeaf(root))
    def test_03(self):
        Input= "2,2,1,null,1,0,null,0"
        root=deserialize(Input)
        Output= "abc"
        self.assertEqual(Output,get_sol().smallestFromLeaf(root))
    def test_04(self):
        Input= "0,null,1"
        root=deserialize(Input)
        Output= "ba"
        self.assertEqual(Output,get_sol().smallestFromLeaf(root))

    # def test_05(self):
    # def test_06(self):
    # def test_07(self):
