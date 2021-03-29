from collections import deque, defaultdict
from heapq import *
import unittest
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def get_int_val(head:ListNode):
            mul=1
            ans = 0
            while head:
                ans+=head.val*mul
                mul*=10
                head=head.next
            return ans
        def make_linked_list(num:int):
            if num==0:return ListNode(0)
            li = []
            while num:
                digit = num%10
                li.append(digit)
                num=num//10
            li.reverse()
            prev=ListNode(li[0])
            for i in range(1,len(li)):
                curr = ListNode(li[i], prev)
                prev = curr
            return prev
        first = get_int_val(l1)
        second = get_int_val(l2)
        summ = first+second
        head = make_linked_list(summ)
        return head



