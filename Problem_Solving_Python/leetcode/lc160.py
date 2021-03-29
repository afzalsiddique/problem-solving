from collections import deque, defaultdict
from heapq import *
import unittest
from typing import List


# Definition for singly-linked list.
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        return str(self.val)

class Solution:
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
