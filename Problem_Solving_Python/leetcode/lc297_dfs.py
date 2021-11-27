import math
import random
from bisect import bisect_left
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Codec:
    # no # at the end
    def serialize(self, root)->str:
        res = []

        def dfs(root):
            if not root:
                res.append("#")
                return
            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        while res and res[-1]=='#':
            res.pop()
        return ",".join(res)


    def deserialize(self, data)->TreeNode:
        self.i=0
        def helper():
            if self.i==len(data): return
            if q[self.i] == "#":
                self.i+=1
                return
            root = TreeNode(int(data[self.i]))
            self.i+=1
            root.left = helper()
            root.right = helper()
            return root

        if not data: return None
        data = data.split(",")
        q = deque(data)
        return helper()

    def deserialize2(self, data)->TreeNode:
        def helper(q):
            if not q: return
            if q[0] == "#":
                q.popleft()
                return
            root = TreeNode(q.popleft())
            root.left = helper(q)
            root.right = helper(q)
            return root

        if not data: return None
        data = data.split(",")
        q = deque(data)
        return helper(q)

def my_deserialize(data):
    sep,en = ',','#'
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

class mytestcase(unittest.TestCase):
    def test1_1(self):
        root = my_deserialize("1,2,3,#,#,4,5")
        self.assertEqual("1,2,#,#,3,4,#,#,5",Codec().serialize(root))
