import random
from bisect import bisect_left
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List



class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head: return head
        c=head
        while True:
            if not c: return head
            if c.child:
                break
            c=c.next
        self.flatten(c.child)
        n =c.next
        c.child.prev=c
        c.next=c.child
        while c.next:
            c=c.next
        c.next=n
        if n: n.prev=c
        c=head
        while c:
            c.child = None
            c=c.next
        return head



class tester(unittest.TestCase):
    def test1(self):
        s = "rabbbit"
        t = "rabbit"
        e = 3
        self.assertEqual(e,Solution().numDistinct(s,t))