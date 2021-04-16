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
    def __repr__(self):
        return str(self.val) +','+str(self.next)
    def __eq__(self, other):
        return str(self)==str(other)
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        left,right = dummy,head
        while right:
            if right.next and right.val == right.next.val:
                while right and right.next and right.val == right.next.val:
                    right = right.next
                left.next = right.next  # propose the next for left
                # this will be verified in the next iteration
            else: # proposal is correct. move left pointer forward
                left = left.next
            right = right.next
        return dummy.next
def make_linked_list(li,i=0):
    if i==len(li)-1:return ListNode(li[i])
    cur = ListNode(li[i])
    cur.next = make_linked_list(li,i+1)
    return cur

class tester(unittest.TestCase):
    def test1(self):
        head = make_linked_list([1,2,3,3,4,4,5])
        Output= make_linked_list([1,2,5])
        self.assertEqual(Output,Solution().deleteDuplicates(head))
    def test2(self):
        head = make_linked_list([1,1,2,2,3,4])
        Output= make_linked_list([3,4])
        self.assertEqual(Output,Solution().deleteDuplicates(head))
