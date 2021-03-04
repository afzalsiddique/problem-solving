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




class MyTestCase(unittest.TestCase):

    def test_1(self):
        head1 = make_linked_list([1,2,3,4,5])
        head2 = make_linked_list([1,2,3,4,5])
        self.assertEqual(head1, head2)