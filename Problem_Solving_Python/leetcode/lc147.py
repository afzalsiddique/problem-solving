import pickle
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
        return str(self.val) + "->" + str(self.next)

    # def __eq__(self, other):
    #     return str(self)==str(other)

class Solution:
    def insertionSortList(self, head):
        cur = dummy = ListNode(0)
        while head:
            if cur.val > head.val: # reset pointer only when new number is smaller than pointer value
                cur = dummy
            while cur.next and cur.next.val < head.val: # find position
                cur = cur.next
            # this will not work
            # cur.next=head
            # cur.next.next=cur.next
            # head=head.next
            # https://www.youtube.com/watch?v=gAkRfdtDOaA&t=62s
            cur.next, cur.next.next, head = head, cur.next, head.next # insert
        return dummy.next

def make_linked_list(li,i=0):
    if i==len(li)-1:return ListNode(li[i])
    cur = ListNode(li[i])
    cur.next = make_linked_list(li,i+1)
    return cur
class tester(unittest.TestCase):
    def test1(self):
        expected = make_linked_list([1,2,3,4])
        actual=Solution().insertionSortList(make_linked_list([4,2,1,3]))
        self.assertEqual(expected,actual)