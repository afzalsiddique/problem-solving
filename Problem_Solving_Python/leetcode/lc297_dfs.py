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
    def serialize(self, root):
        def dfs(root, res):
            if root == None:
                res.append('#')
                return
            res.append(root.val)
            dfs(root.left, res)
            dfs(root.right, res)

        res = []
        dfs(root, res)
        res = ','.join(map(str,res)) # return string
        return res

    def deserialize(self, data):
        def dfs():
            if data[p[0]] == '#':
                p[0] += 1
                return None
            root = TreeNode(data[p[0]])
            p[0] += 1
            root.left = dfs()
            root.right = dfs()
            return root

        data = data.split(',')
        p = [0]
        return dfs()

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
        self.assertEqual("1,2,#,#,3,4,#,#,5,#,#",Codec().serialize(root))
