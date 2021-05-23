import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        maxx=float('-inf')
        ans_level=0
        level=0
        q=deque([root])
        while q:
            level+=1
            tmp=0
            for _ in range(len(q)):
                cur=q.popleft()
                if cur.left: q.append(cur.left)
                if cur.right: q.append(cur.right)
                tmp+=cur.val
            if tmp>maxx:
                maxx=tmp
                ans_level=level
        return ans_level


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
        root = '1,7,0,7,-8,null,null'
        Output= 2
        root=deserialize(root)
        self.assertEqual(Output, get_sol().maxLevelSum(root))
    def test02(self):
        root = '989,null,10250,98693,-89388,null,null,null,-32127'
        Output= 2
        root=deserialize(root)
        self.assertEqual(Output, get_sol().maxLevelSum(root))
