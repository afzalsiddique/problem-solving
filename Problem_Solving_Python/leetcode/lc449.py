from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Codec()
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __repr__(self): return str(self.val)
class Codec:
    NONE='null'
    SEP=','
    def serialize(self, root: TreeNode) -> str:
        res=[]
        def preorder(root):
            if not root: return
            res.append(root.val)
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        res=list(map(str,res))
        return self.SEP.join(res)

    def deserialize(self, data: str) -> TreeNode:
        def construct(hi):
            nonlocal i
            if i==n: return None
            if data[i]>hi: return None
            node=TreeNode(data[i])
            i+=1
            node.left=construct(node.val)
            node.right=construct(hi)
            return node

        if data=='': return None
        data=data.split(self.SEP)
        n=len(data)
        data=[int(x) for x in data]
        i=0
        return construct(float('inf'))


class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(ser(des([2,1,3])),get_sol().serialize(get_sol().deserialize("2,1,3")))
    def test02(self):
        self.assertEqual(ser(des([])),get_sol().serialize(get_sol().deserialize("")))
    # def test03(self):
    # def test04(self):
    # def test05(self):
    # def test06(self):
    # def test07(self):
    # def test08(self):
