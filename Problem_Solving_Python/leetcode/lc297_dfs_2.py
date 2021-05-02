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
    def serialize(self, root)->str:
        def dfs(root):
            if not root:
                res.append("#,")
                return
            res.append(str(root.val)+",")
            dfs(root.left)
            dfs(root.right)

        res = []
        dfs(root)
        return "".join(res)


    def deserialize(self, data)->TreeNode:
        def helper(q):
            if q[0] == "#":
                q.popleft()
                return
            root = TreeNode(q.popleft())
            l = helper(q)
            r = helper(q)
            root.left = l
            root.right = r
            return root

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
        self.assertEqual("1,2,#,#,3,4,#,#,5,#,#,",Codec().serialize(root))
    def test1_2(self):
        data = "1,2,#,#,3,4,#,#,5,#,#,"
        actual_root = Codec().deserialize(data)
        actual_data = Codec().serialize(actual_root)
        self.assertEqual("1,2,#,#,3,4,#,#,5,#,#,",actual_data)
