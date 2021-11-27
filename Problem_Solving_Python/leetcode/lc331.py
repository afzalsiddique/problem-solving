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

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # https://www.youtube.com/watch?v=_mbnPPHJmTQ
    # in degree and out degree
    def isValidSerialization(self, preorder)-> bool:
        # remember how many empty slots we have
        # non-null nodes occupy one slot but create two new slots
        # null nodes occupy one slot

        p = preorder.split(',')

        #initially we have one empty slot to put the root in it
        slot = 1
        for node in p:
            # no empty slot to put the current node
            if slot == 0:
                return False
            # occupy slot (null nodes and non-null nodes occupy slots)
            slot-=1

            # only non-null nodes create slots
            if node!='#':
                slot += 2

        #we don't allow empty slots at the end
        return slot==0

class Solution2:
    # same as serialize and deserialize binary tree
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
    def isValidSerialization(self, preorder: str) -> bool:
        root = self.deserialize(preorder)
        serialized = self.serialize(root)
        if preorder==serialized: return True
        return False

class mytestcase(unittest.TestCase):
    def test1_1(self):
        preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#"
        Output= True
        self.assertEqual(Output,get_sol().isValidSerialization(preorder))
    def test1_2(self):
        preorder = "1,#"
        Output= False
        self.assertEqual(Output,get_sol().isValidSerialization(preorder))
    def test1_3(self):
        preorder = "9,#,#,1"
        Output= False
        self.assertEqual(Output,get_sol().isValidSerialization(preorder))
