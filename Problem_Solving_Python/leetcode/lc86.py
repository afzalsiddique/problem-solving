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
        return str(self.val) +','+str(self.next)
    def __eq__(self, other):
        return str(self)==str(other)
# https://www.youtube.com/watch?v=KT1iUciJr4g
class Solution:
    def partition(self, head, x):
        dummy1 = left = ListNode(0) # all nodes less then x
        dummy2 = right = ListNode(0) # all nodes greater than or equal to x
        while head:
            if head.val < x:
                left.next = head
                left = left.next
            else:
                right.next = head
                right = right.next
            head = head.next
        right.next = None
        left.next = dummy2.next
        return dummy1.next
def make_linked_list(li,i=0):
    if i==len(li)-1:return ListNode(li[i])
    cur = ListNode(li[i])
    cur.next = make_linked_list(li,i+1)
    return cur

class tester(unittest.TestCase):
    def test1(self):
        head = make_linked_list([1,4,3,2,5,2])
        x = 3
        Output= make_linked_list([1,2,2,4,3,5])
        self.assertEqual(Output,Solution().partition(head,x))
    def test2(self):
        head =make_linked_list( [2,1])
        x = 2
        Output= make_linked_list([1,2])
        self.assertEqual(Output,Solution().partition(head,x))
