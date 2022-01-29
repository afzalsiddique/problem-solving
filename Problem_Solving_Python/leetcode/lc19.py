from itertools import accumulate; from math import floor,ceil; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt; from sortedcontainers import SortedList
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self): return str(self.val) + "->" + str(self.next)
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        fast = slow = dummy
        # Advances fast pointer so that the gap between fast and slow is n nodes apart
        while n:
            fast = fast.next
            n-=1
        # move the first per maintaining the gap
        while fast.next:
            slow = slow.next
            fast= fast.next
        slow.next = slow.next.next
        return dummy.next
class Solution3:
    # two pass
    def removeNthFromEnd2(self, head: ListNode, n: int) -> ListNode:
        if head.next is None:
            return None # only one node
        head_copy = ListNode(head.val, head.next)
        total_length = 1
        while head.next != None:
            head = head.next
            total_length+=1
        if total_length == n: # if we need to delete the head node
            return head_copy.next
        length = total_length - n - 1
        head = head_copy
        while length!= 0:
            head = head.next
            length-=1
        head.next = head.next.next
        return head_copy

class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(make_linked_list([1,2,3,4,6,7]), get_sol().removeNthFromEnd(make_linked_list([1,2,3,4,5,6,7]),3))
    def test02(self):
        self.assertEqual(make_linked_list([1,2,3,5]), get_sol().removeNthFromEnd(make_linked_list([1,2,3,4,5]),2))
    def test03(self):
        self.assertEqual(make_linked_list([2]), get_sol().removeNthFromEnd(make_linked_list([1,2]),2))
    def test04(self):
        self.assertEqual(make_linked_list([1]), get_sol().removeNthFromEnd(make_linked_list([1,2]),1))
    def test05(self):
        self.assertEqual(make_linked_list([]), get_sol().removeNthFromEnd(make_linked_list([1]),1))
