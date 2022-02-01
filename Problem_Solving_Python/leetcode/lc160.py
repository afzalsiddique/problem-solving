from itertools import accumulate; from math import floor,ceil; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt; from sortedcontainers import SortedList
from binary_tree_tester import ser,des
def get_sol(): return Solution()
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        return str(self.val)
# https://www.youtube.com/watch?v=u4FWXfgS8jw&t=6m47s
class Solution:
    def getLength(self,head):
        n=0
        while head:
            head=head.next
            n+=1
        return n
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        n1,n2=self.getLength(headA),self.getLength(headB)
        if n1<n2: return self.getIntersectionNode(headB,headA) # make a longer linked list
        a,b=headA,headB
        diff=n1-n2
        while diff:
            a=a.next
            diff-=1
        while a!=b:
            a=a.next
            b=b.next
        return a
class Solution2:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:return None
        a,b=headA, headB
        while a!=b:
            a=headB if a is None else a.next
            b=headA if b is None else b.next
        return a

# https://leetcode.com/problems/intersection-of-two-linked-lists/discuss/49785/Java-solution-without-knowing-the-difference-in-len!/165648
# Visualization of this solution:
# Case 1 (Have Intersection & Same Len):
#
#        a
# A:     a1 → a2 → a3
#                    ↘
#                      c1 → c2 → c3 → null
#                    ↗
# B:     b1 → b2 → b3
#        b

#             a
# A:     a1 → a2 → a3
#                    ↘
#                      c1 → c2 → c3 → null
#                    ↗
# B:     b1 → b2 → b3
#             b

#                  a
# A:     a1 → a2 → a3
#                    ↘
#                      c1 → c2 → c3 → null
#                    ↗
# B:     b1 → b2 → b3
#                  b

# A:     a1 → a2 → a3
#                    ↘ a
#                      c1 → c2 → c3 → null
#                    ↗ b
# B:     b1 → b2 → b3
# Since a == b is true, end loop while(a != b), return the intersection node a = c1.
#
#
# Case 2 (Have Intersection & Different Len):
#
#             a
# A:          a1 → a2
#                    ↘
#                      c1 → c2 → c3 → null
#                    ↗
# B:     b1 → b2 → b3
#        b

#                  a
# A:          a1 → a2
#                    ↘
#                      c1 → c2 → c3 → null
#                    ↗
# B:     b1 → b2 → b3
#             b

# A:          a1 → a2
#                    ↘ a
#                      c1 → c2 → c3 → null
#                    ↗
# B:     b1 → b2 → b3
#                  b

# A:          a1 → a2
#                    ↘      a
#                      c1 → c2 → c3 → null
#                    ↗ b
# B:     b1 → b2 → b3

# A:          a1 → a2
#                    ↘           a
#                      c1 → c2 → c3 → null
#                    ↗      b
# B:     b1 → b2 → b3

# A:          a1 → a2
#                    ↘                a = null, then a = b1
#                      c1 → c2 → c3 → null
#                    ↗           b
# B:     b1 → b2 → b3

# A:          a1 → a2
#                    ↘
#                      c1 → c2 → c3 → null
#                    ↗                b = null, then b = a1
# B:     b1 → b2 → b3
#        a

#             b
# A:          a1 → a2
#                    ↘
#                      c1 → c2 → c3 → null
#                    ↗
# B:     b1 → b2 → b3
#             a

#                  b
# A:          a1 → a2
#                    ↘
#                      c1 → c2 → c3 → null
#                    ↗
# B:     b1 → b2 → b3
#                  a

# A:          a1 → a2
#                    ↘ b
#                      c1 → c2 → c3 → null
#                    ↗ a
# B:     b1 → b2 → b3
# Since a == b is true, end loop while(a != b), return the intersection node a = c1.
#
#
# Case 3 (Have No Intersection & Same Len):
#
#        a
# A:     a1 → a2 → a3 → null
# B:     b1 → b2 → b3 → null
#        b

#             a
# A:     a1 → a2 → a3 → null
# B:     b1 → b2 → b3 → null
#             b

#                  a
# A:     a1 → a2 → a3 → null
# B:     b1 → b2 → b3 → null
#                  b

#                       a = null
# A:     a1 → a2 → a3 → null
# B:     b1 → b2 → b3 → null
#                       b = null
# Since a == b is true (both refer to null), end loop while(a != b), return a = null.
#
#
# Case 4 (Have No Intersection & Different Len):
#
#        a
# A:     a1 → a2 → a3 → a4 → null
# B:     b1 → b2 → b3 → null
#        b

#             a
# A:     a1 → a2 → a3 → a4 → null
# B:     b1 → b2 → b3 → null
#             b

#                  a
# A:     a1 → a2 → a3 → a4 → null
# B:     b1 → b2 → b3 → null
#                  b

#                       a
# A:     a1 → a2 → a3 → a4 → null
# B:     b1 → b2 → b3 → null
#                       b = null, then b = a1

#        b                   a = null, then a = b1
# A:     a1 → a2 → a3 → a4 → null
# B:     b1 → b2 → b3 → null

#             b
# A:     a1 → a2 → a3 → a4 → null
# B:     b1 → b2 → b3 → null
#        a

#                  b
# A:     a1 → a2 → a3 → a4 → null
# B:     b1 → b2 → b3 → null
#             a

#                       b
# A:     a1 → a2 → a3 → a4 → null
# B:     b1 → b2 → b3 → null
#                  a

#                            b = null
# A:     a1 → a2 → a3 → a4 → null
# B:     b1 → b2 → b3 → null
#                       a = null
def make_linked_list(li,i=0):
    if not li: return None
    if i==len(li)-1:return ListNode(li[i])
    cur = ListNode(li[i])
    cur.next = make_linked_list(li,i+1)
    return cur
class MyTestCase(unittest.TestCase):
    def test01(self):
        common=make_linked_list([8,4,5])
        headA=make_linked_list([4,1])
        headB=make_linked_list([5,6,1])
        curA,curB=headA,headB
        while curA.next: curA=curA.next
        while curB.next: curB=curB.next
        curA.next=common
        curB.next=common
        self.assertEqual(common, get_sol().getIntersectionNode(headA,headB))
    def test02(self):
        common=make_linked_list([2,4])
        headA=make_linked_list([1,9,1])
        headB=make_linked_list([3])
        curA,curB=headA,headB
        while curA.next: curA=curA.next
        while curB.next: curB=curB.next
        curA.next=common
        curB.next=common
        self.assertEqual(common, get_sol().getIntersectionNode(headA,headB))
    def test03(self):
        common=make_linked_list([])
        headA=make_linked_list([2,6,4])
        headB=make_linked_list([1,5])
        curA,curB=headA,headB
        while curA.next: curA=curA.next
        while curB.next: curB=curB.next
        curA.next=common
        curB.next=common
        self.assertEqual(common, get_sol().getIntersectionNode(headA,headB))
    # def test04(self):
    # def test05(self):
    # def test06(self):
    # def test07(self):
