import random
from bisect import bisect_left
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head):
        left, right = head, head.next if head else None
        while right:
            if left.val == right.val:
                left.next = right.next
            else:
                left = right
            right = right.next

        return head
class Solution2:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head: return
        if not head.next: return head
        left,right=head,head
        while right:
            while right and right.val==left.val:
                right=right.next
            left.next=right
            left=left.next
        return head
