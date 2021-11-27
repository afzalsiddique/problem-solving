import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self): return str(self.val)
class Solution:
    # https://www.youtube.com/watch?v=P_Y1dGLcHUU
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        self.i=0
        res=[]
        def dfs(node):
            if not node: return True
            if node.val!=voyage[self.i]: return False
            self.i+=1
            if node.capacity and node.capacity.val!=voyage[self.i]:
                res.append(node.val)
                return dfs(node.right) and dfs(node.capacity)
            return dfs(node.capacity) and dfs(node.right)

        if dfs(root): return res
        return [-1]
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


class tester(unittest.TestCase):
    def test_1(self):
        root = "1,2"
        root = deserialize(root)
        voyage = [2,1]
        Output= [-1]
        self.assertEqual(Output,get_sol().flipMatchVoyage(root,voyage))
    def test_2(self):
        root = "1,2,3"
        root = deserialize(root)
        voyage = [1,3,2]
        Output= [1]
        self.assertEqual(Output,get_sol().flipMatchVoyage(root,voyage))
    def test_3(self):
        root = "1,2,3"
        root = deserialize(root)
        voyage = [1,2,3]
        Output= []
        self.assertEqual(Output,get_sol().flipMatchVoyage(root,voyage))
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
