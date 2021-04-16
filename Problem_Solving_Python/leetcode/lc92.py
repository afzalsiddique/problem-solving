import random
from bisect import bisect_left
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        return str(self.val)+','+str(self.next)
    def __eq__(self, other):
        return str(self)==str(other)
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        # p: prev, c: cur, n:next
        dummy=ListNode(-9999,head)
        p=dummy
        for _ in range(left-1):
            p=p.next
        c=p.next
        n=c.next
        for _ in range(right-left):
            c.next=n.next
            n.next=p.next
            p.next=n
            n=c.next
        return dummy.next

def make_linked_list(li,i=0):
    if i==len(li)-1:return ListNode(li[i])
    cur = ListNode(li[i])
    cur.next = make_linked_list(li,i+1)
    return cur

class tester(unittest.TestCase):
    def test1(self):
        head = make_linked_list([1,2,3,4,5])
        left = 2
        right = 4
        Output= make_linked_list([1,4,3,2,5])
        self.assertEqual(Output,Solution().reverseBetween(head,left,right))
    def test2(self):
        head = make_linked_list([5])
        left = 1
        right = 1
        Output= make_linked_list([5])
        self.assertEqual(Output,Solution().reverseBetween(head,left,right))
    def test3(self):
        head = make_linked_list([1,2,3,4,5])
        left = 2
        right = 2
        Output= make_linked_list([1,2,3,4,5])
        self.assertEqual(Output,Solution().reverseBetween(head,left,right))
