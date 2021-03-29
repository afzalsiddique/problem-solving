from collections import deque, defaultdict
from heapq import *
import unittest
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:return None
        slow=fast = head
        cycle = False
        while fast.next and fast.next.next:
            fast=fast.next.next
            slow=slow.next
            if fast==slow:
                cycle=True
                break
        if not cycle:return None
        fast=head
        while fast!=slow:
            fast=fast.next
            slow=slow.next
        return fast
