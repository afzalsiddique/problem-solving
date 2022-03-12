from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self): return str(self.val)

class Solution:
    # time O(n) space O(height)
    # https://leetcode.com/problems/recover-binary-search-tree/discuss/32535/No-Fancy-Algorithm-just-Simple-and-Powerful-In-Order-Traversal
    first,second=None,None
    prev=TreeNode(float('-inf'))
    def recoverTree(self, root: TreeNode) -> None:
        def traverse(root): # in order traversal
            if not root: return
            traverse(root.left)
            if self.first is None and self.prev.val>=root.val:
                self.first=self.prev
            if self.first is not None and self.prev.val>=root.val:
                self.second=root
            self.prev=root
            traverse(root.right)

        traverse(root)
        self.first.val,self.second.val=self.second.val,self.first.val

class Solution3:
    # time O(n) space O(n)
    def recoverTree(self, root: TreeNode) -> None:
        res=[]

        def in_order(root):
            if not root: return
            if root.left: in_order(root.left)
            res.append(root.val)
            if root.right: in_order(root.right)

        def search(root,key): # given node.val return node pointer
            if not root: return None
            if root.val==key: return root
            return search(root.left,key) or search(root.right,key)

        in_order(root)
        n=len(res)
        p,q=None,None
        # find first inconsistency
        for i in range(n):
            if i<n-1 and res[i]>res[i+1]:
                p=res[i]
                break
        # find second inconsistency
        for i in reversed(range(n)):
            if i>0 and res[i-1]>res[i]:
                q=res[i]
                break

        node_p=search(root,p)
        node_q=search(root,q)
        node_p.val,node_q.val=node_q.val,node_p.val
class Tester(unittest.TestCase):
    def test01(self):
        root=des([1,3,None,None,2])
        get_sol().recoverTree(root)
        self.assertEqual("3,1,null,null,2",ser(root))
    def test02(self):
        root=des([3,1,4,None,None,2])
        get_sol().recoverTree(root)
        self.assertEqual("2,1,4,null,null,3",ser(root))
