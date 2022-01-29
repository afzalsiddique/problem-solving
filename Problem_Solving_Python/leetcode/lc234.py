from itertools import accumulate; from math import floor,ceil; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt; from sortedcontainers import SortedList
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self): return str(self.val) + "->" + str(self.next)

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:return False
        if not head.next:return True
        slow=fast=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next

        # reverse the second part
        node = None # node is prev node of slow pointer
        while slow:
            nxt=slow.next
            slow.next=node
            node=slow
            slow=nxt

        while node:
            if node.val!=head.val:return False
            node=node.next
            head=head.next
        return True
class Solution2:
    def reverse(self,head):
        if not head: return None
        dummy=ListNode(-1,head)
        p=dummy
        c=p.next
        n=c.next
        while n:
            c.next=n.next
            n.next=p.next
            p.next=n
            n=c.next
        return dummy.next
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        dummy=ListNode(-1,head)
        cur=dummy
        cnt=0
        while cur.next:
            cur=cur.next
            cnt+=1

        cur=dummy
        for _ in range(cnt//2):
            cur=cur.next

        if cnt&1:
            second=cur.next.next
        else:
            second=cur.next

        first=dummy.next
        second=self.reverse(second)
        while second:
            if first.val!=second.val:
                return False
            first=first.next
            second=second.next
        return True




class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(True, get_sol().isPalindrome(make_linked_list([1,2,2,1])))
    def test02(self):
        self.assertEqual(False, get_sol().isPalindrome(make_linked_list([1,2])))
    def test03(self):
        self.assertEqual(True, get_sol().isPalindrome(make_linked_list([1])))
    # def test04(self):
    # def test05(self):
