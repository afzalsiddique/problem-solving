from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self): return str(self.val)+'->'+str(self.next)
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        # move the node positioned after n2 to after n1
        # 1->3->2->4->   5->    6->None
        #    n1   n2  n2.next

        # 1->3->5->2->4->6->None
        #    n1      n2
        n1=head
        n2=head.next
        while n1 and n2 and n2.next:
            wilBeMoved=n2.next
            n2.next=wilBeMoved.next
            wilBeMoved.next=n1.next
            n1.next=wilBeMoved
            n1=n1.next
            n2=n2.next
        return head



class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(make_linked_list([1,3,5,2,4]), get_sol().oddEvenList(make_linked_list([1,2,3,4,5])))
    def test02(self):
        self.assertEqual(make_linked_list([2,3,6,7,1,5,4]), get_sol().oddEvenList(make_linked_list([2,1,3,5,6,4,7])))
    def test03(self):
        self.assertEqual(make_linked_list([]), get_sol().oddEvenList(make_linked_list([])))
    def test04(self):
        self.assertEqual(make_linked_list([1,3,2]), get_sol().oddEvenList(make_linked_list([1,2,3])))
    def test05(self):
        self.assertEqual(make_linked_list([1,3,2,4]), get_sol().oddEvenList(make_linked_list([1,2,3,4])))
    def test06(self):
        self.assertEqual(make_linked_list([1]), get_sol().oddEvenList(make_linked_list([1])))
    # def test06(self):
    # def test07(self):
    # def test08(self):
    # def test09(self):
    # def test10(self):
    # def test11(self):
    # def test12(self):
