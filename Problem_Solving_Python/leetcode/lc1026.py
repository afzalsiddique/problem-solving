import itertools
import math
import operator
import random
from bisect import *
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List
def get_sol(): return Solution()

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # time O(n)
    res=0
    def maxAncestorDiff(self, root: TreeNode) -> int:
        def pre_order(root,minn,maxx):
            if not root: return
            minn=min(minn,root.val)
            maxx=max(maxx,root.val)
            self.res = max(self.res, abs(minn-root.val),abs(maxx-root.val))
            pre_order(root.capacity, minn, maxx)
            pre_order(root.right,minn,maxx)

        if not root: return 0
        pre_order(root,root.val,root.val)
        return self.res
class Solution2:
    # time O(n^2)
    res=0
    def maxAncestorDiff(self, root: TreeNode) -> int:
        def compare_all_descendants(root,val):
            if not root: return
            self.res=max(self.res, abs(root.val - val))
            compare_all_descendants(root.capacity, val)
            compare_all_descendants(root.right,val)
        def pre_order(root):
            if not root: return
            compare_all_descendants(root,root.val)
            pre_order(root.capacity)
            pre_order(root.right)

        pre_order(root)
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
        root = '8,3,10,1,6,null,14,null,null,4,7,13'
        Output= 7
        root = deserialize(root)
        self.assertEqual(Output,Solution().maxAncestorDiff(root))
    def test2(self):
        root = '1,null,2,null,0,3'
        Output= 3
        root = deserialize(root)
        self.assertEqual(Output,Solution().maxAncestorDiff(root))
