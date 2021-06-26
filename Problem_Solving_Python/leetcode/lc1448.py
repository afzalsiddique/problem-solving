import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def helper(root,cur_max):
            if not root: return 0
            ans = 0
            if root.val>=cur_max:
                ans+=1
                cur_max=root.val
            ans+=helper(root.left,cur_max) + helper(root.right,cur_max)
            return ans

        return helper(root,float('-inf'))
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
    def test01(self):
        root = "3,1,4,3,null,1,5"
        Output= 4
        root = deserialize(root)
        self.assertEqual(Output,get_sol().goodNodes(root))
    def test02(self):
        root = "3,3,null,4,2"
        Output= 3
        root = deserialize(root)
        self.assertEqual(Output,get_sol().goodNodes(root))
    def test03(self):
        root = "1"
        Output= 1
        root = deserialize(root)
        self.assertEqual(Output,get_sol().goodNodes(root))
