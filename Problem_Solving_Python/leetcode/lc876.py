import unittest
from typing import List


# Definition for singly-linked list.
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


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        n = 0
        curr = head
        while curr.next != None:
            curr=curr.next
            n+=1
        n = (n+1)//2
        i = 0
        curr = head
        while i!=n:
            curr = curr.next
            i+=1
        return curr



class MyTestCase(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        head = make_linked_list([1,2,3,4,5])
        actual = sol.middleNode(head)
        expected = make_linked_list([3,4,5])
        print(expected)
        print(actual)
        self.assertEqual(str(expected), str(actual))

    def test_2(self):
        sol = Solution()
        head = make_linked_list([1,2,3,4,5,6])
        actual = sol.middleNode(head)
        expected = make_linked_list([4,5,6])
        print(expected)
        print(actual)
        self.assertEqual(str(expected), str(actual))

