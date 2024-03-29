from itertools import accumulate; from math import floor,ceil; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt; from sortedcontainers import SortedList
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
# https://leetcode.com/problems/merge-two-sorted-lists/discuss/9735/Python-solutions-(iteratively-recursively-iteratively-in-place).
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self): return str(self.val) + "->" + str(self.next)


class Solution:
    def mergeTwoLists(self, l1, l2):
        dummy = cur = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next

        cur.next = l1 if l1 else l2 # if one of them is at the end(means None), then the other one will append to the result directly.
        # the above line same as
        # if l1:
        #     cur.next = l1
        # if l2:
        #     cur.next = l2
        return dummy.next

    def mergeTwoLists2(self, a, b):
        if (not a) or (b and a.val > b.val): #First make sure that a is the "better" one (meaning b is None or has larger/equal value). Then merge the remainders behind a.
            a, b = b, a
        if a:
            a.next = self.mergeTwoLists2(a.next, b)
        return a



class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(make_linked_list([1,2,3,4,5,6]), get_sol().mergeTwoLists(make_linked_list([1,3,5]), make_linked_list([2,4,6])))
    def test02(self):
        self.assertEqual(make_linked_list([]), get_sol().mergeTwoLists(make_linked_list([]), make_linked_list([])))
    def test03(self):
        self.assertEqual(make_linked_list([1]), get_sol().mergeTwoLists(make_linked_list([1]), make_linked_list([])))
    def test04(self):
        self.assertEqual(make_linked_list([1,1,2,3,4,4]), get_sol().mergeTwoLists(make_linked_list([1,2,4]), make_linked_list([1,3,4])))
