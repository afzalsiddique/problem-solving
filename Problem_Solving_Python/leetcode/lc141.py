from collections import deque, defaultdict
from heapq import *
import unittest
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        return str(self.val)

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:return False
        slow=head
        fast=head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if fast==slow:return True
        return False
    def hasCycle2(self, head: ListNode) -> bool:
        if not head:return False
        slow=head
        fast=head.next
        while True:
            if fast is None:return False
            if fast.next is None:return False
            if fast==slow:return True
            slow = slow.next
            fast = fast.next.next
