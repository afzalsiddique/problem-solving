# solve by making a circle
# https://leetcode.com/problems/rotate-list/discuss/22726/Anyone-solve-the-problem-without-counting-the-length-of-List
import unittest
from operator import eq
from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val) + "->" + str(self.next)


def make_linked_list(li:List) -> ListNode:
    n = len(li)
    temp = ListNode(li[-1], None)
    for i in range(n-2,-1,-1):
        temp = ListNode(li[i],temp)
    return temp

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        fake = ListNode(-1)
        slow = fast = fake
        fake.next = head
        length = 0
        while fast.next != None: # fast will reach tail & count length
            fast = fast.next
            length+=1
        if length == 0: return None
        k = k % length
        for _ in range(length - k): # slow will reach before rotation point
            slow = slow.next

        fast.next = fake.next # connect the two parts
        fake.next = slow.next
        slow.next = None
        return fake.next

class MyTestCase(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        li = [1,2,3,4,5]
        head = make_linked_list(li)
        actual = sol.rotateRight(head, 2)
        expected = make_linked_list([4,5,1,2,3])
        self.assertEqual(expected, actual)

    def test_2(self):
        sol = Solution()
        li = [0,1,2]
        head = make_linked_list(li)
        actual = sol.rotateRight(head, 4)
        expected = make_linked_list([2,0,1])
        self.assertEqual(expected, actual)

    def test_3(self):
        sol = Solution()
        two = ListNode(2,None)
        one = ListNode(1,two)
        actual = sol.rotateRight(one, 2)
        expected = 0
        self.assertEqual(expected, actual)

    def test_4(self):
        sol = Solution()
        actual = sol.rotateRight(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_5(self):
        sol = Solution()
        actual = sol.rotateRight(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_6(self):
        sol = Solution()
        actual = sol.rotateRight(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_7(self):
        sol = Solution()
        actual = sol.rotateRight(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_8(self):
        sol = Solution()
        actual = sol.rotateRight(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_9(self):
        sol = Solution()
        actual = sol.rotateRight(0)
        expected = 0
        self.assertEqual(expected, actual)