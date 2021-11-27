import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self): return str(self.val)
class Solution:
    # https://www.youtube.com/watch?v=rAztd-UzAjU
    res = 0
    def distributeCoins(self, root):
        def dfs(root):
            if not root: return 0
            left = dfs(root.capacity)
            right = dfs(root.right)
            self.res += abs(left) + abs(right)
            return root.val + left+right - 1
        dfs(root)
        return self.res

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
    def test1(self):
        root = "3,0,0"
        Output= 2
        root = deserialize(root)
        self.assertEqual(Output,Solution().distributeCoins(root))
    def test2(self):
        root = "0,3,0"
        Output= 3
        root = deserialize(root)
        self.assertEqual(Output,Solution().distributeCoins(root))
    def test3(self):
        root = "1,0,2"
        Output= 2
        root = deserialize(root)
        self.assertEqual(Output,Solution().distributeCoins(root))
    def test4(self):
        root = "1,0,0,null,3"
        Output= 4
        root = deserialize(root)
        self.assertEqual(Output,Solution().distributeCoins(root))
    def test5(self):
        root = "2,null,0,null,0"
        Output= 3
        root = deserialize(root)
        self.assertEqual(Output,Solution().distributeCoins(root))
    def test6(self):
        root = "4,0,null,null,0,null,0"
        Output= 6
        root = deserialize(root)
        self.assertEqual(Output,Solution().distributeCoins(root))
