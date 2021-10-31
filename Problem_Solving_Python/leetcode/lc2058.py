import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self): return str(self.val) + "->" + str(self.next)
    def __eq__(self, other): return str(self)==str(other)
def make_linked_list(li,i=0):
    if not li: return None
    if i==len(li)-1:return ListNode(li[i])
    cur = ListNode(li[i])
    cur.next = make_linked_list(li,i+1)
    return cur
class Solution:
    def nodesBetweenCriticalPoints(self, head:ListNode) -> List[int]:
        # dummy_head = ListNode(float('inf'), head)
        # cur = dummy_head
        # while cur.next:
        #     cur = cur.next
        # dummy_tail = ListNode(float('inf'))
        # cur.next=dummy_tail

        li=[]
        # cur=dummy_head
        cur=head
        prev=cur.val
        cur=cur.next
        i=0
        while cur.next:
            if cur.val>prev and cur.val>cur.next.val:
                li.append(i)
            elif cur.val<prev and cur.val<cur.next.val:
                li.append(i)
            prev=cur.val
            cur=cur.next
            i+=1
        minn,maxx=float('inf'),float('-inf')
        for i in range(len(li)-1):
            minn=min(minn,li[i+1]-li[i])
        if len(li)>1:
            maxx=max(maxx,li[-1]-li[0])

        if minn==float('inf'): minn=-1
        if maxx==float('-inf'): maxx=-1
        return [minn,maxx]


class MyTestCase(unittest.TestCase):
    def test1(self):
        head = make_linked_list([3,1])
        Output= [-1,-1]
        self.assertEqual(Output, get_sol().nodesBetweenCriticalPoints(head))
    def test2(self):
        head = make_linked_list([5,3,1,2,5,1,2])
        Output= [1,3]
        self.assertEqual(Output, get_sol().nodesBetweenCriticalPoints(head))
    def test3(self):
        head = make_linked_list([1,3,2,2,3,2,2,2,7])
        Output= [3,3]
        self.assertEqual(Output, get_sol().nodesBetweenCriticalPoints(head))
    def test4(self):
        head = make_linked_list([2,3,3,2])
        Output= [-1,-1]
        self.assertEqual(Output, get_sol().nodesBetweenCriticalPoints(head))
    # def test5(self):
    # def test6(self):
