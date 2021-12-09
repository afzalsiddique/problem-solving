import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List; import functools
def get_sol(): return Solution()
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self): return str(self.val) + "->" + str(self.next)
    def __eq__(self, other): return str(self)==str(other)
class Solution:
    def deleteMiddle(self, head: ListNode) -> ListNode:
        dummy=ListNode(-1,head)
        n=-1
        cur=dummy
        while cur:
            n+=1
            cur=cur.next
        i=n//2
        cur=dummy
        for _ in range(i):
            cur=cur.next

        if cur.next:
            cur.next=cur.next.next
        else:
            cur.next=None
        return dummy.next


def make_linked_list(li,i=0):
    if not li: return None
    if i==len(li)-1:return ListNode(li[i])
    cur = ListNode(li[i])
    cur.next = make_linked_list(li,i+1)
    return cur

class tester(unittest.TestCase):
    def test1(self):
        Output= make_linked_list([1,3,4,1,2,6])
        self.assertEqual(Output,get_sol().deleteMiddle(head = make_linked_list([1,3,4,7,1,2,6])))
    def test2(self):
        Output= make_linked_list([1,2,4])
        self.assertEqual(Output,get_sol().deleteMiddle(head = make_linked_list([1,2,3,4])))
    def test3(self):
        Output= make_linked_list([2])
        self.assertEqual(Output,get_sol().deleteMiddle(head = make_linked_list([2,1])))
    def test4(self):
        Output= make_linked_list([])
        self.assertEqual(Output,get_sol().deleteMiddle(head = make_linked_list([2])))
    # def test5(self):
