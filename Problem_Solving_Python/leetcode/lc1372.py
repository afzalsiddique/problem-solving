import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List
def get_sol(): return Solution()
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def longestZigZag(self, root):
        self.maxx=float('-inf')
        def dfs(root):
            if not root: return [-1, -1]
            left_left,left_right = dfs(root.left)
            right_left,right_right=dfs(root.right)
            self.maxx=max(self.maxx,left_right + 1, right_left + 1)
            return [left_right + 1, right_left + 1]
        dfs(root)
        return self.maxx


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

class MyTestCase(unittest.TestCase):
    def test1(self):
        root = "1,null,1,1,1,null,null,1,1,null,1,null,null,null,1,null,1"
        root=deserialize(root)
        Output= 3
        self.assertEqual(Output,get_sol().longestZigZag(root))
    def test2(self):
        root = "1,1,1,null,1,null,null,1,1,null,1"
        root=deserialize(root)
        Output= 4
        self.assertEqual(Output,get_sol().longestZigZag(root))
    def test3(self):
        root = "1"
        root=deserialize(root)
        Output= 0
        self.assertEqual(Output,get_sol().longestZigZag(root))
    # def test4(self):
    # def test5(self):