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
    def __init__(self):
        self.sep=','
        self.en='null'
    def serialize(self, root:Optional[TreeNode])->str:
        if not root:return ""
        q = deque()
        q.append(root)
        li = []
        while q:
            node = q.popleft()
            if node:
                li.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                li.append(self.en)
        while li and li[-1]==self.en: li.pop()
        return self.sep.join(li)
    def serialize2(self, root:Optional[TreeNode])->str:
        if not root: return ''

        q = deque()
        res = [str(root.val)]
        q.append(root)
        while q:
            cur = q.popleft()
            for child in [cur.left, cur.right]:
                if child:
                    q.append(child)
                    res.append(str(child.val))
                else:
                    res.append(self.en)
        while res and res[-1]==self.en: res.pop()
        return self.sep.join(res)

    def deserialize(self, data:str)->Optional[TreeNode]:
        if not data: return None
        data=data.split(self.sep)
        data=[int(x) if x!=self.en else None for x in data]
        l = len(data)
        root = TreeNode(int(data[0]))
        q = deque()
        q.append(root)
        i=1
        while i<l and q:
            curr = q.popleft()
            if data[i] is not None:
                curr.left = TreeNode(int(data[i]))
                q.append(curr.left)
            i+=1
            if i<l and data[i] is not None:
                curr.right = TreeNode(int(data[i]))
                q.append(curr.right)
            i+=1

        return root



class Tester(unittest.TestCase):
    def test01a(self):
        root = get_sol().deserialize("1,null,2,null,3,null,4,null,5")
        self.assertEqual(ser(root),Codec().serialize(root))
    def test01b(self):
        root=des([1,None,2,None,3,None,4,None,5])
        self.assertEqual(ser(root),Codec().serialize(root))
    def test02a(self):
        root = get_sol().deserialize("1,2,3")
        self.assertEqual(ser(root),Codec().serialize(root))
    def test02b(self):
        root=des([1,2,3])
        self.assertEqual(ser(root),Codec().serialize(root))
    def test03a(self):
        root = get_sol().deserialize("")
        self.assertEqual(ser(root),Codec().serialize(root))
    def test03b(self):
        root=des([])
        self.assertEqual(ser(root),Codec().serialize(root))
    def test04a(self):
        root=get_sol().deserialize("1,2,3,null,null,4,5")
        self.assertEqual(ser(root),Codec().serialize(root))
    def test04b(self):
        root=des([1,2,3,None,None,4,5])
        self.assertEqual(ser(root),Codec().serialize(root))
# class Tester(unittest.TestCase):
#     def test01(self):
#         root = get_sol().deserialize("1,null,2,null,3,null,4,null,5")
#         self.assertEqual("1,null,2,null,3,null,4,null,5",Codec().serialize(root))
#     def test02(self):
#         root = get_sol().deserialize("1,2,3")
#         self.assertEqual("1,2,3",Codec().serialize(root))
#     def test03(self):
#         root = get_sol().deserialize("")
#         self.assertEqual("",Codec().serialize(root))
#     def test04(self):
#         root=get_sol().deserialize("1,2,3,null,null,4,5")
#         self.assertEqual("1,2,3,null,null,4,5",Codec().serialize(root))
