import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List; import functools
from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self): return str(self.val)
class Solution:
    def recoverFromPreorder(self, traversal: str) -> TreeNode:
        def dfs(i,cur):
            j=i
            cnt=0 # no of '-'
            while j<n and traversal[j]=='-':
                cnt+=1
                j+=1
            if cnt!=cur+1:# no node can be created then no more chars have been considered so return i
                return None,i

            # if this node has one more '-' then the prev node, then this node is child of prev node
            num=[] # parse int
            while j<n and traversal[j]!='-':
                num.append(traversal[j])
                j+=1
            node=TreeNode(int(''.join(num)))
            left,new_i=dfs(j,cur+1)
            right,new_i=dfs(new_i,cur+1)
            node.left=left
            node.right=right
            return node,new_i

        n=len(traversal)
        root,_=dfs(0,-1)
        return root


class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual("1,401,null,349,88", serialize(get_sol().recoverFromPreorder("1-401--349--88")))
    def test2(self):
        self.assertEqual("1,2,5,3,null,6,null,4,null,7", serialize(get_sol().recoverFromPreorder(traversal = "1-2--3---4-5--6---7")))
    def test3(self):
        self.assertEqual("1,401,null,349,88,90", serialize(get_sol().recoverFromPreorder("1-401--349---90--88")))
    def test4(self):
        self.assertEqual("1,2,5,3,4,6,7", serialize(get_sol().recoverFromPreorder(traversal = "1-2--3--4-5--6--7")))
    # def test5(self):
    # def test6(self):
    # def test7(self):
