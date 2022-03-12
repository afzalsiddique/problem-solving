from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self): return str(self.val) + "->" + str(self.next)

# https://www.youtube.com/watch?v=meOY1wajrnw
class Solution:
    def reorderList(self, head):
        #step 1: find middle
        if not head: return
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        #step 2: reverse second half
        prev, curr = None, slow.next
        while curr:
            nextt = curr.next
            curr.next = prev
            prev = curr
            curr = nextt
        slow.next = None

        #step 3: merge lists
        head1, head2 = head, prev
        while head2:
            nextt = head1.next
            head1.next = head2
            head1 = head2
            head2 = nextt


# using stack. time n. memory n.
class Solution2:
    def reorderList(self, head: ListNode) -> None:
        if not head: return
        st,size=[],0
        cur=head
        while cur:
            st.append(cur)
            size+=1
            cur=cur.next
        cur=head
        for _ in range(size//2):
            nxt=cur.next
            cur.next=st.pop()
            cur=cur.next
            cur.next=nxt
            cur=cur.next
        cur.next=None

class Tester(unittest.TestCase):
    def test01(self):
        actual=make_linked_list([1,2,3,4])
        get_sol().reorderList(actual)
        self.assertEqual(make_linked_list([1,4,2,3]),actual)
    def test02(self):
        actual=make_linked_list([1,2,3,4,5])
        get_sol().reorderList(actual)
        self.assertEqual(make_linked_list([1,5,2,4,3]),actual)
    def test03(self):
        actual=make_linked_list([1,2,3,4,5,6,7,8,9,10])
        get_sol().reorderList(actual)
        self.assertEqual(make_linked_list([1,10,2,9,3,8,4,7,5,6]),actual)
    def test04(self):
        actual=make_linked_list([1,2,3,4,5,6,7,8,9,10,11])
        get_sol().reorderList(actual)
        self.assertEqual(make_linked_list([1,11,2,10,3,9,4,8,5,7,6]),actual)
