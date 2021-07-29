import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List
def get_sol(): return Solution()
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self): return str(self.val) + "->" + str(self.next)
    def __eq__(self, other): return str(self)==str(other)
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        a_node_prev=list1
        b_node=list1
        a-=1
        while a:
            a_node_prev=a_node_prev.next
            a-=1
        while b:
            b_node=b_node.next
            b-=1

        list2_end = list2
        while list2_end.next:
            list2_end=list2_end.next

        a_node_prev.next=list2
        list2_end.next=b_node.next
        b_node.next=list2_end
        return list1

def make_linked_list(li,i=0):
    if not li: return None
    if i==len(li)-1:return ListNode(li[i])
    cur = ListNode(li[i])
    cur.next = make_linked_list(li,i+1)
    return cur
class tester(unittest.TestCase):
    def test_1(self):
        list1,a,b,list2 = [0,1,2,3,4,5],   3,   4,   [1000000,1000001,1000002]
        Output= [0,1,2,1000000,1000001,1000002,5]
        self.assertEqual(make_linked_list(Output),get_sol().mergeInBetween(make_linked_list(list1),a,b,make_linked_list(list2)))
    def test_2(self):
        list1,a,b,list2 = [0,1,2,3,4,5,6],   2,   5,   [1000000,1000001,1000002,1000003,1000004]
        Output= [0,1,1000000,1000001,1000002,1000003,1000004,6]
        self.assertEqual(make_linked_list(Output),get_sol().mergeInBetween(make_linked_list(list1),a,b,make_linked_list(list2)))
    # def test_3(self):
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):