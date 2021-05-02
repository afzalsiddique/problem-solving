import random
from bisect import bisect_left
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res=[]
        if not root: return res
        q = deque([root])
        while q:
            temp=[]
            for _ in range(len(q)):
                cur=q.popleft()
                temp.append(cur.val)
                for child in cur.children:
                    q.append(child)
            res.append(temp)
        return res
