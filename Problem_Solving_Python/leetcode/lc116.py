from itertools import accumulate; from math import floor,ceil; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt; from sortedcontainers import SortedList
from binary_tree_tester import *; from a_linked_list import make_linked_list
def get_sol(): return Solution()

# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/discuss/37715/Python-solutions-(Recursively-BFS%2Bqueue-DFS%2Bstack)
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:return None
        q = deque([root])
        while q:
            cur = q.popleft()
            if cur.right and cur.left:
                cur.left.next = cur.right
                q.append(cur.left)
                q.append(cur.right)
            if cur.right and cur.next:
                cur.right.next=cur.next.left if cur.next.left else cur.next.right
        return root
class Solution2:
    def connect(self, root: 'Node') -> 'Node':
        if not root:return None
        q = deque([root])
        while q:
            curr = q.popleft()
            if curr.left and curr.right:
                curr.left.next = curr.right
                if curr.next:
                    curr.right.next=curr.next.left
                q.append(curr.left)
                q.append(curr.right)
        return root
class Solution3:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        def helper(node,leftChild,par):
            if not node:
                return
            if leftChild and par and par.right:
                node.next=par.right
            elif par and par.next and par.next.left:
                node.next=par.next.left
            elif par and par.next and par.next.right:
                node.next=par.next.right
            helper(node.right,False,node)
            helper(node.left,True,node)

        helper(root,'does not matter',None)
        return root
