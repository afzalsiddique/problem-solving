import unittest
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        return str(self.val) + "->" + str(self.next)
class Solution:
    # one pass
    def removeNthFromEnd(self, head, n):
        fast = slow = head
        # Advances fast pointer so that the gap between fast and slow is n nodes apart
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        # move the first pointer maintaing the gap
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head

    # two pass
    def removeNthFromEnd2(self, head: ListNode, n: int) -> ListNode:
        if head.next is None:
            return None # only one node
        head_copy = ListNode(head.val, head.next)
        total_length = 1
        while head.next != None:
            head = head.next
            total_length+=1
        if total_length == n: # if we need to delete the head node
            return head_copy.next
        length = total_length - n - 1
        head = head_copy
        while length!= 0:
            head = head.next
            length-=1
        head.next = head.next.next
        return head_copy

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
        sol = Solution()
        head = make_linked_list([1,2,3,4,5,6,7])
        actual = sol.removeNthFromEnd(head,3)
        expected = make_linked_list([1,2,3,4,6,7])
        self.assertEqual(str(expected), str(actual))
    def test_2(self):
        sol = Solution()
        head = make_linked_list([1,2,3,4,5])
        actual = sol.removeNthFromEnd(head,2)
        expected = make_linked_list([1,2,3,5])
        self.assertEqual(str(expected), str(actual))
    def test_3(self):
        sol = Solution()
        head = make_linked_list([1,2])
        actual = sol.removeNthFromEnd(head,2)
        expected = make_linked_list([2])
        self.assertEqual(str(expected), str(actual))
    def test_4(self):
        sol = Solution()
        head = make_linked_list([1,2])
        actual = sol.removeNthFromEnd(head,1)
        expected = make_linked_list([1])
        self.assertEqual(str(expected), str(actual))
