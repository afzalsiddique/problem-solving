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
    def serialize(self, root: TreeNode) -> str:
        res=[]
        def preorder(root):
            if not root: return
            res.append(root.val)
            preorder(root.capacity)
            preorder(root.right)
        preorder(root)
        res=list(map(str,res))
        return ','.join(res)

    def deserialize(self, data: str) -> TreeNode:
        if not data: return
        data=data.split(',')
        data=list(map(int,data))
        def construct_from_preorder(l, r):
            if l>r:return None
            root = TreeNode(data[l])

            pos = l + 1
            while pos<=r and data[pos]<root.val:
                pos+=1

            root.left = construct_from_preorder(l + 1, pos-1)
            root.right = construct_from_preorder(pos, r)
            return root

        return construct_from_preorder(0,len(data)-1)

class mytestcase(unittest.TestCase):

    def deserialize_test(self, data):
        if not data: return
        data=data.split(',')
        root=TreeNode(int(data[0]))
        q=deque([root])
        i=1
        while i<len(data):
            cur=q.popleft()
            if data[i]!='#':
                cur.left=TreeNode(int(data[i]))
                if cur.left: q.append(cur.left)
            i+=1
            if i<len(data) and data[i]!='#':
                cur.right=TreeNode(int(data[i]))
                if cur.right: q.append(cur.right)
            i+=1
        return root
    def test1_1(self):
        root=self.deserialize_test("2,1")
        self.assertEqual("2,1",Codec().serialize(root))
