import unittest
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
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


class MyTestCase(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        five = ListNode(5,None)
        four = ListNode(4, five)
        three = ListNode(3, four)
        two = ListNode(2, three)
        one = ListNode(1, two)
        actual = sol.removeNthFromEnd(one, 2)
        expected = 0
        self.assertEqual(expected, actual)

    def test_2(self):
        sol = Solution()
        actual = sol.removeNthFromEnd(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_3(self):
        sol = Solution()
        actual = sol.removeNthFromEnd(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_4(self):
        sol = Solution()
        actual = sol.removeNthFromEnd(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_5(self):
        sol = Solution()
        actual = sol.removeNthFromEnd(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_6(self):
        sol = Solution()
        actual = sol.removeNthFromEnd(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_7(self):
        sol = Solution()
        actual = sol.removeNthFromEnd(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_8(self):
        sol = Solution()
        actual = sol.removeNthFromEnd(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_9(self):
        sol = Solution()
        actual = sol.removeNthFromEnd(0)
        expected = 0
        self.assertEqual(expected, actual)