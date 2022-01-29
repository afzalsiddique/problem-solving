from itertools import accumulate; from math import floor,ceil; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt; from sortedcontainers import SortedList
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        return str(self.val)+','+str(self.next)
    def __eq__(self, other):
        return str(self)==str(other)
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        # p: prev, c: cur, n:next
        dummy=ListNode(-9999,head)
        p=dummy
        for _ in range(left-1):
            p=p.next
        c=p.next
        n=c.next
        for _ in range(right-left):
            c.next=n.next
            n.next=p.next
            p.next=n
            n=c.next
        return dummy.next


class Solution2:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        left-=1
        right-=1
        dummy=ListNode(0,head)
        cnt=0
        cur=dummy
        while cnt<left:
            cur=cur.next
            cnt+=1

        prevStart=cur

        cur=cur.next
        cnt+=1

        start=cur
        prev=cur
        cur=cur.next
        while cnt<=right:
            start.next=cur.next
            nxt=cur.next
            cur.next=prev
            prev=cur
            cur=nxt
            cnt+=1

        prevStart.next=prev
        return dummy.next

class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(make_linked_list([1,4,3,2,5]),Solution().reverseBetween(make_linked_list([1,2,3,4,5]),2,4))
    def test02(self):
        self.assertEqual(make_linked_list([5]),Solution().reverseBetween(make_linked_list([5]),1,1))
    def test03(self):
        self.assertEqual(make_linked_list([1,2,3,4,5]),Solution().reverseBetween(make_linked_list([1,2,3,4,5]),2,2))
    def test04(self):
        self.assertEqual(make_linked_list([5,3]),Solution().reverseBetween(make_linked_list([3,5]),1, 2))
