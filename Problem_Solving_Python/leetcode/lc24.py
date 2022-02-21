from itertools import accumulate; from math import floor,ceil; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt; from sortedcontainers import SortedList
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self): return str(self.val)+','+str(self.next)

# recursive without changing node values
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        def helper(head):
            if not head: return
            if not head.next: return head # odd
            first,second=head,head.next
            res = helper(second.next)
            second.next=first
            first.next=res
            return second

        return helper(head)

# iterative without changing node values
class Solution2:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head: return
        first,second=head,head.next
        if head.next:
            new_head=second
        else:
            new_head=first
        while first and second:
            nxt=second.next
            if second.next and second.next.next:
                first.next=second.next.next
            else:
                first.next=second.next
            second.next=first
            first=nxt
            second=None if not nxt else nxt.next
        return new_head


class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual(make_linked_list([2,1,4,3]),get_sol().swapPairs(make_linked_list([1,2,3,4])))
    def test2(self):
        self.assertEqual(make_linked_list([1]),get_sol().swapPairs(make_linked_list([1])))
    def test3(self):
        self.assertEqual(make_linked_list([2,1]),get_sol().swapPairs(make_linked_list([1,2])))
    def test4(self):
        self.assertEqual(make_linked_list([2,1,3]),get_sol().swapPairs(make_linked_list([1,2,3])))
    def test5(self):
        self.assertEqual(make_linked_list([2,1,4,3,5]),get_sol().swapPairs(make_linked_list([1,2,3,4,5])))
