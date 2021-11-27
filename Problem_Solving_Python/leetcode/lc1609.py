import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        q=deque([root])
        even=False
        prev=''
        while q:
            even=not even
            for i in range(len(q)):
                cur=q.popleft()
                if even!=cur.val%2: return False
                if i!=0:
                    if even and (cur.val%2==0 or cur.val<=prev): return False
                    if not even and (cur.val%2==1 or cur.val>=prev): return False
                prev=cur.val
                if cur.left: q.append(cur.left)
                if cur.right: q.append(cur.right)
        return True
class Solution2:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        q=deque([root])
        level=-1
        prev=''
        while q:
            level+=1
            for i in range(len(q)):
                cur=q.popleft()
                if level%2==cur.val%2:
                    return False
                if i!=0:
                    if level%2:
                        if cur.val>=prev:
                            return False
                    else:
                        if cur.val<=prev:
                            return False
                prev=cur.val
                if cur.left: q.append(cur.left)
                if cur.right: q.append(cur.right)
        return True


def deserialize(data): # for unit testing
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
class Tester(unittest.TestCase):
    def test1(self):
        root = deserialize("1,10,4,3,null,7,9,12,8,6,null,null,2")
        Output= True
        self.assertEqual(Output,get_sol().isEvenOddTree(root))
    def test2(self):
        root = deserialize("5,4,2,3,3,7")
        Output= False
        self.assertEqual(Output,get_sol().isEvenOddTree(root))
    def test3(self):
        root = deserialize("5,9,1,3,5,7")
        Output= False
        self.assertEqual(Output,get_sol().isEvenOddTree(root))
    def test4(self):
        root = deserialize("1")
        Output= True
        self.assertEqual(Output,get_sol().isEvenOddTree(root))
    def test5(self):
        root = deserialize("11,8,6,1,3,9,11,30,20,18,16,12,10,4,2,17")
        Output= True
        self.assertEqual(Output,get_sol().isEvenOddTree(root))
    def test6(self):
        root = deserialize("13,34,32,23,25,27,29,44,40,36,34,30,30,28,26,3,7,9,11,15,17,21,25,null,null,27,31,35,null,37,null,30,null,26,null,null,null,24,null,20,16,12,10,null,null,8,null,null,null,null,null,6,null,null,null,null,null,15,19,null,null,null,null,23,null,27,29,33,37,null,null,null,null,null,null,48,null,null,null,46,null,null,null,42,38,34,32,null,null,null,null,19")
        Output= False
        self.assertEqual(Output,get_sol().isEvenOddTree(root))
    def test7(self):
        root = deserialize("2,12,8,5,9,null,null,18,16")
        Output= False
        self.assertEqual(Output,get_sol().isEvenOddTree(root))
