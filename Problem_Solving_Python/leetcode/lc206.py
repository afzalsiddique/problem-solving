import unittest
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val) + "->" + str(self.next)
# iterative
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:return None
        if not head.next:return head
        prev=None
        while head:
            curr = head
            head = head.next
            curr.next=prev
            prev=curr
        return curr
# recursive
class Solution2:
    def reverseList(self, head: ListNode) -> ListNode:
        if head==None:return None
        if head.next==None:
            return head # head will be the first node in the reversed list. so return first node
        first_node = self.reverseList(head.next)
        head.next.next = head
        head.next=None
        return first_node
class Solution3:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        if head.next == None:
            return head
        curr = head.next
        prev = head
        while curr!=None:
            curr.next, prev, curr = prev, curr, curr.next # this line is very bad. avoid this. Does not do the job simultaneously
        head.next = None # to avoid cycle
        return prev

def make_linked_list2(nums):
    """
    given a list it creates a linked list and returns the head of the linked list
    """
    if not nums:return None
    if len(nums)==1:return ListNode(nums[0])
    cur = ListNode(nums[0])
    nxt = make_linked_list2(nums[1:])
    cur.next = nxt
    return cur

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
