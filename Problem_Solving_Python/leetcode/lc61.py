from itertools import accumulate; from math import floor,ceil; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt; from sortedcontainers import SortedList
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()

# solve by making a circle
# https://leetcode.com/problems/rotate-list/discuss/22726/Anyone-solve-the-problem-without-counting-the-length-of-List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val) + "->" + str(self.next)



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

class Solution2:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:return None
        if not head.next:return head
        cnt = 1
        cur = head
        while cur.next:
            cur=cur.next
            cnt+=1
        if k%cnt==0:return head # optimization
        k=k%cnt
        cur.next = head
        temp = cnt-k-1
        cur = head
        while temp:
            cur=cur.next
            temp-=1
        head = cur.next
        cur.next=None
        return head




class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(make_linked_list([4,5,1,2,3]), get_sol().rotateRight(make_linked_list([1,2,3,4,5]), 2))
    def test02(self):
        self.assertEqual(make_linked_list([2,0,1]), get_sol().rotateRight(make_linked_list([0,1,2]), 4))
    def test03(self):
        self.assertEqual(make_linked_list([1,2]), get_sol().rotateRight(make_linked_list([1,2]), 4))
    def test04(self):
        self.assertEqual(make_linked_list([]), get_sol().rotateRight(make_linked_list([]), 0))
    def test05(self):
        self.assertEqual(make_linked_list([2,1]), get_sol().rotateRight(make_linked_list([1,2]), 1))
