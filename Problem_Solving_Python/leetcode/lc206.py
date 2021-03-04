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
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        if head.next == None:
            return head
        curr = head.next
        prev = head
        while curr!=None:
            curr.next, prev, curr = prev, curr, curr.next
        head.next = None
        return prev


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
        head = make_linked_list([1,2,3,4,5])
        actual = sol.reverseList(head)
        expected = make_linked_list([5,4,3,2,1])
        print(expected)
        print(actual)
        self.assertEqual(str(expected), str(actual))

    def test_2(self):
        sol = Solution()
        head = make_linked_list([1,2])
        actual = sol.reverseList(head)
        expected = make_linked_list([2,1])
        print(expected)
        print(actual)
        self.assertEqual(str(expected), str(actual))

    def test_3(self):
        sol = Solution()
        head = make_linked_list([])
        actual = sol.reverseList(head)
        expected = make_linked_list([])
        print(expected)
        print(actual)
        self.assertEqual(str(expected), str(actual))

    def test_4(self):
        sol = Solution()
        head = make_linked_list([1])
        actual = sol.reverseList(head)
        expected = make_linked_list([1])
        print(expected)
        print(actual)
        self.assertEqual(str(expected), str(actual))

    def test_5(self):
        sol = Solution()
        actual = sol.reverseList(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_6(self):
        sol = Solution()
        actual = sol.reverseList(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_7(self):
        sol = Solution()
        actual = sol.reverseList(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_8(self):
        sol = Solution()
        actual = sol.reverseList(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_9(self):
        sol = Solution()
        actual = sol.reverseList(0)
        expected = 0
        self.assertEqual(expected, actual)