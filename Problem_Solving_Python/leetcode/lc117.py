import random
from bisect import bisect_left
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

# bfs. time n. space 1
class Solution:
    # https://www.youtube.com/watch?v=yl-fdkyQD8A
    def connect(self, root: 'Node') -> 'Node':
        if not root: return
        head=root
        emptyNode=Node(0)
        while head:
            dummy=emptyNode
            dummy.next,dummy.left,dummy.right=None,None,None # reusing the node by making it empty
            child_head=dummy
            while head:
                if head.left:
                    child_head.next=head.left
                    child_head=child_head.next
                if head.right:
                    child_head.next=head.right
                    child_head=child_head.next
                head=head.next
            head=dummy.next
        return root

# basic bfs. time n space n
class Solution3:
    # https://www.youtube.com/watch?v=yl-fdkyQD8A
    def connect(self, root: 'Node') -> 'Node':
        if not root: return
        q=deque([root])
        while q:
            dummy=Node(0)
            for _ in range(len(q)):
                cur=q.popleft()
                dummy.next=cur
                dummy=dummy.next
                if cur.left: q.append(cur.left)
                if cur.right: q.append(cur.right)
        return root
class Solution2:
    def connect(self, root: 'Node') -> 'Node':
        di = defaultdict(lambda :None)
        def helper(root:Node,level):
            if not root: return
            useless1=helper(root.right,level+1)
            useless2=helper(root.left,level+1)
            root.next=di[level]
            di[level]=root
            return root

        return helper(root,0)
