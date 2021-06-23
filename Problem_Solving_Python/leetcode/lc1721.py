import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self): return str(self.val) + "->" + str(self.next)
class Solution:
    # https://leetcode.com/problems/swapping-nodes-in-a-linked-list/discuss/1054370/Python-3-or-Swapping-NODES-or-Swapping-Values-or-One-Pass-or-Fully-explained
    # swap by reference instead of values
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        dummy = pre_right = pre_left = ListNode(next=head)
        right = left = head
        for i in range(k-1):
            pre_left = left
            left = left.next

        null_checker = left

        while null_checker.next:
            pre_right = right
            right = right.next
            null_checker = null_checker.next

        if left == right:
            return head

        pre_left.next, pre_right.next = right, left
        left.next, right.next = right.next, left.next
        return dummy.next

class Solution2:
    # https://leetcode.com/problems/swapping-nodes-in-a-linked-list/discuss/1013859/Python3Visualization-Two-Pointers-Solution-with-Explanation
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        dummy=ListNode(0,head)
        slow, fast = dummy, dummy
        for _ in range(k):
            fast = fast.next
        first = fast
        while fast:
            slow, fast = slow.next, fast.next
        first.val, slow.val = slow.val, first.val
        return dummy.next
class Solution3:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        n=0
        dummy = ListNode(0,head)
        node = dummy
        while node:
            node=node.next
            n+=1
        n1,n2=dummy,dummy
        i=0
        while i!=k:
            i+=1
            n1=n1.next
        i=0
        while i!=n-k:
            i+=1
            n2=n2.next
        n1.val,n2.val=n2.val,n1.val

        return dummy.next



def make_linked_list(li,i=0):
    if i==len(li)-1:return ListNode(li[i])
    cur = ListNode(li[i])
    cur.next = make_linked_list(li,i+1)
    return cur
class tester(unittest.TestCase):
    def test_01(self):
        head = [1, 2, 3, 4, 5]
        head = make_linked_list(head)
        k=2
        Output = [1,4,3,2,5]
        Output = make_linked_list(Output)
        self.assertEqual(Output, get_sol().swapNodes(head,k) )
    def test_01_2(self):
        head = [1, 2, 3, 4, 5]
        head = make_linked_list(head)
        k=3
        Output = [1, 2, 3, 4, 5]
        Output = make_linked_list(Output)
        self.assertEqual(Output, get_sol().swapNodes(head,k) )
    def test_01_3(self):
        head = [1, 2, 3, 4, 5]
        head = make_linked_list(head)
        k=4
        Output = [1,4,3,2,5]
        Output = make_linked_list(Output)
        self.assertEqual(Output, get_sol().swapNodes(head,k) )
    def test_02(self):
        head = [7,9,6,6,7,8,3,0,9,5]
        head = make_linked_list(head)
        k = 5
        Output= [7,9,6,6,8,7,3,0,9,5]
        Output = make_linked_list(Output)
        self.assertEqual(Output, get_sol().swapNodes(head,k) )
    def test_03(self):
        head = [1]
        head = make_linked_list(head)
        k = 1
        Output= [1]
        Output = make_linked_list(Output)
        self.assertEqual(Output, get_sol().swapNodes(head,k) )
    def test_04(self):
        head = [1,2]
        head = make_linked_list(head)
        k = 1
        Output= [2,1]
        Output = make_linked_list(Output)
        self.assertEqual(Output, get_sol().swapNodes(head,k) )
    def test_05(self):
        head = [1,2,3]
        head = make_linked_list(head)
        k = 2
        Output= [1,2,3]
        Output = make_linked_list(Output)
        self.assertEqual(Output, get_sol().swapNodes(head,k) )
