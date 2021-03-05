# https://leetcode.com/problems/merge-two-sorted-lists/discuss/9735/Python-solutions-(iteratively-recursively-iteratively-in-place).
import unittest
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val) + "->" + str(self.next)

    def __eq__(self, other):
        return str(self)==str(other)


def make_linked_list(li:List) -> ListNode:
    """
    given a list the function creates a linked list and returns the head of the linked list
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

class Solution:
    def mergeTwoLists(self, l1, l2):
        dummy = cur = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next

        cur.next = l1 if l1 else l2 # if one of them is at the end(means None), then the other one will append to the result directly.
        # the above line same as
        # while l1:
        #     cur.next=l1
        #     l1=l1.next
        #     cur=cur.next
        # while l2:
        #     cur.next=l2
        #     l2=l2.next
        #     cur=cur.nex
        return dummy.next

    def mergeTwoLists2(self, a, b):
        if (not a) or (b and a.val > b.val): #First make sure that a is the "better" one (meaning b is None or has larger/equal value). Then merge the remainders behind a.
            a, b = b, a
        if a:
            a.next = self.mergeTwoLists2(a.next, b)
        return a


class MyTestCase(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        head1 = make_linked_list([1,3,5])
        head2 = make_linked_list([2,4,6])
        actual = sol.mergeTwoLists(head1, head2)
        expected = make_linked_list([1,2,3,4,5,6])
        self.assertEqual(expected, actual)