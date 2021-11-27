import functools; import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List; from math import sqrt
def get_sol(): return Solution()
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        return str(self.val) + "->" + str(self.next)
class Solution:
    def get_length_of_next_group(self,head,n):
        i=0
        cur=head
        while cur:
            cur=cur.next
            i+=1
            if i==n+1:
                return i
        return i
    def reverseEvenLengthGroups(self, head: ListNode) -> ListNode:
        cur=head
        n=1
        prev=None
        while cur:
            i=n
            if i%2:
                while i and cur:
                    prev=cur
                    cur=cur.next
                    i-=1
                start=prev
            else:
                while i and cur:
                    nxt=cur.next
                    cur.next=prev
                    prev=cur
                    cur=nxt
                    i-=1
                start.next.next=cur
                tmp_prev=start.next
                start.next=prev
                start=tmp_prev
            n=self.get_length_of_next_group(cur,n)
        return head


def make_linked_list(li:List) -> ListNode:
    """
    given a list it creates a linked list and returns the head of the linked list
    """
    n = len(li)
    if n==0:
        return None
    if n==1:
        return ListNode(li[0])
    temp = ListNode(li[-1], None)
    for i in range(n-2,-1,-1):
        temp = ListNode(li[i],temp)
    return temp



class MyTestCase(unittest.TestCase):
    def test_2(self):
        head = make_linked_list([5,2,6,3,9,1,7,3,8,4])
        actual = get_sol().reverseEvenLengthGroups(head)
        expected = make_linked_list([5,6,2,3,9,1,4,8,3,7])
        print(expected)
        print(actual)
        self.assertEqual(str(expected), str(actual))
    def test_3(self):
        head = make_linked_list([1,1,0,6])
        actual = get_sol().reverseEvenLengthGroups(head)
        expected = make_linked_list([1,0,1,6])
        print(expected)
        print(actual)
        self.assertEqual(str(expected), str(actual))
    def test_4(self):
        head = make_linked_list([1,1,0,6,5])
        actual = get_sol().reverseEvenLengthGroups(head)
        expected = make_linked_list([1,0,1,5,6])
        print(expected)
        print(actual)
        self.assertEqual(str(expected), str(actual))
    def test_5(self):
        head = make_linked_list([2,1])
        actual = get_sol().reverseEvenLengthGroups(head)
        expected = make_linked_list([2,1])
        print(expected)
        print(actual)
        self.assertEqual(str(expected), str(actual))
    def test_6(self):
        head = make_linked_list([8])
        actual = get_sol().reverseEvenLengthGroups(head)
        expected = make_linked_list([8])
        print(expected)
        print(actual)
        self.assertEqual(str(expected), str(actual))
