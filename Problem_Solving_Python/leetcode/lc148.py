from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        return str(self.val) + "->" + str(self.next)
class Solution:
    def getLen(self,node:ListNode): return 1+self.getLen(node.next) if node else 0
    def conquer(self,node):
        if not node or not node.next: return node
        n=self.getLen(node)
        if n==2:
            res=node
            if node.val>node.next.val:
                res=node.next
                node.next.next=node
                node.next=None
            return res

        A,B=self.divide(node)
        A=self.conquer(A)
        B=self.conquer(B)
        res=self.mergeTwoLists(A,B)
        return res

    def divide(self, node1):
        n=self.getLen(node1)
        if n==0 or n==1: return node1,None
        cur=node1
        n=n//2-1
        while n:
            cur=cur.next
            n-=1
        node2=cur.next
        cur.next=None
        return node1, node2
    def mergeTwoLists(self, A: Optional[ListNode], B: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(-1)
        cur=dummy
        while A and B:
            if A.val<B.val:
                cur.next=A
                A=A.next
            else:
                cur.next=B
                B=B.next
            cur=cur.next
        cur.next = A if A else B # if one of them is at the end(means None), then the other one will append to the result directly.
        return dummy.next
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.conquer(head)
class Solution2:
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
                if head.val<=head.next.val:
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

class MyTestCase(unittest.TestCase):
    def test01(self):
        actual = get_sol().sortList(make_linked_list([2,1,6,5,4]))
        expected = make_linked_list([1,2,4,5,6])
        self.assertEqual(str(expected), str(actual))
    def test02(self):
        actual = get_sol().sortList(make_linked_list([5,-1,3,4,0]))
        expected = make_linked_list([-1,0,3,4,5])
        self.assertEqual(str(expected), str(actual))
    def test03(self):
        actual = get_sol().sortList(make_linked_list([]))
        expected = make_linked_list([])
        self.assertEqual(str(expected), str(actual))
