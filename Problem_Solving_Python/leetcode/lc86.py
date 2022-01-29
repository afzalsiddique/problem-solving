from itertools import accumulate; from math import floor,ceil; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt; from sortedcontainers import SortedList
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self): return str(self.val) +','+str(self.next)
class Solution:
    # https://www.youtube.com/watch?v=KT1iUciJr4g
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

class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(make_linked_list([1,2,2,4,3,5]), get_sol().partition(make_linked_list([1,4,3,2,5,2]),3))
    def test02(self):
        self.assertEqual(make_linked_list([1,2]), get_sol().partition(make_linked_list( [2,1]),2))
    # def test03(self):
    # def test04(self):
