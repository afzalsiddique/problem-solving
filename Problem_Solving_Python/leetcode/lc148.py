from bisect import bisect_left
from collections import deque, defaultdict
from heapq import *
import unittest
from typing import List








class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        return str(self.val) + "->" + str(self.next)
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def merge_two_lists(head1:ListNode, head2:ListNode):
            if not head1 and not head2:return None
            if not head1 or not head2:return head1 or head2
            dummy = ListNode(0)
            cur = dummy
            while head1 and head2:
                if head1.val<head2.val:
                    cur.next=head1
                    head1=head1.next
                else:
                    cur.next=head2
                    head2=head2.next
                cur=cur.next
            if not head1:
                cur.next =head2
            else:
                cur.next = head1
            return dummy.next
        def length(head:ListNode):
            if not head:return 0
            n = 0
            while head:
                head=head.next
                n+=1
            return n
        def helper(head:ListNode):
            n = length(head)
            if n==0:return None
            if n==1:return head
            if n==2:
                if head.val<=head.next.data:
                    return head
                else:
                    new_head = head.next
                    head.next.next=head
                    head.next=None
                    return new_head
            cnt,cur = 0, head
            while cnt!=n//2:
                cur=cur.next
                cnt+=1
            head2 = cur.next
            cur.next=None
            head = helper(head)
            head2 = helper(head2)
            new_head = merge_two_lists(head,head2)
            return new_head

        return helper(head)


def make_linked_list(li:List) -> ListNode:
    """
    given a list it creates a linked list and returns the head of the linked list
    """
    n = len(li)
    if n==0:
        return None
    if n==1:
        return ListNode(li[0])
    temp = ListNode(li[-1], None)
    for i in range(n-2,-1,-1):
        temp = ListNode(li[i],temp)
    return temp
class MyTestCase(unittest.TestCase):
    def test_1(self):
        actual = Solution().sortList(make_linked_list([2,1,6,5,4]))
        expected = make_linked_list([1,2,4,5,6])
        self.assertEqual(str(expected), str(actual))
    def test_2(self):
        actual = Solution().sortList(make_linked_list([5,-1,3,4,0]))
        expected = make_linked_list([-1,0,3,4,5])
        self.assertEqual(str(expected), str(actual))
    def test_3(self):
        actual = Solution().sortList(make_linked_list([]))
        expected = make_linked_list([])
        self.assertEqual(str(expected), str(actual))
