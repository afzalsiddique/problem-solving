import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self): return str(self.val)  + "->" + str(self.next)
    # def __eq__(self, other): return str(self)==str(other)
class Solution:
    # https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/discuss/366319/JavaC%2B%2BPython-Greedily-Skip-with-HashMap
    # Iterate for the first time, calculate the prefix sum, and save the it to seen[prefix]
    # Iterate for the second time, calculate the prefix sum, and directly skip to last occurrence of this prefix
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        di={}
        prefix=0
        node=dummy=ListNode(0,head)
        while node:
            prefix+=node.val
            di[prefix]=node
            node=node.next

        node = dummy

        prefix=0
        while node:
            prefix+=node.val
            node.next=di[prefix].next
            node=node.next
        return dummy.next
class Solution2:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        di={}
        rev_di={}
        cur_sum=0
        dummy=ListNode(0,head)
        node=dummy
        while node:
            cur_sum+=node.val
            if cur_sum in di:
                prev=di[cur_sum]
                tmp=prev.next
                while tmp!=node:
                    di.pop(rev_di[tmp])
                    tmp=tmp.next
                prev.next=node.next
                node=node.next
                continue
            di[cur_sum]=node
            rev_di[node]=cur_sum
            node=node.next
        return dummy.next
def make_linked_list(li,i=0):
    if not li: return None
    if i==len(li)-1:return ListNode(li[i])
    cur = ListNode(li[i])
    cur.next = make_linked_list(li,i+1)
    return cur
class tester(unittest.TestCase):
    def test_1(self):
        head = make_linked_list([1,2,-3,3,1])
        Output =  make_linked_list([3,1])
        self.assertEqual(Output, get_sol().removeZeroSumSublists(head))
    def test_2(self):
        head = make_linked_list( [1,2,3,-3,4])
        Output =  make_linked_list([1,2,4])
        self.assertEqual(Output, get_sol().removeZeroSumSublists(head))
    def test_3(self):
        head = make_linked_list([1,2,3,-3,-2])
        Output =  make_linked_list([1])
        self.assertEqual(Output, get_sol().removeZeroSumSublists(head))
    def test_4(self):
        head = make_linked_list([1,3,2,-3,-2,5,5,-5,1])
        Output =  make_linked_list([1,5,1])
        self.assertEqual(Output, get_sol().removeZeroSumSublists(head))
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):