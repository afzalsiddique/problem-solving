from collections import deque, defaultdict
from heapq import *
import unittest
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None



class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:return False
        if not head.next:return True
        slow=fast=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        node = None
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