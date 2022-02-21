from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self): return str(self.val)+'->'+str(self.next)
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(-1)
        cur = dummy


        right=head
        right=right.next
        while right:
            summ=0
            while right.val!=0:
                summ+=right.val
                right=right.next
            right=right.next
            if summ!=0:
                cur.next=ListNode(summ)
                cur=cur.next

        return dummy.next



class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(make_linked_list([4,11]), get_sol().mergeNodes(make_linked_list([0,3,1,0,4,5,2,0])))
    def test02(self):
        self.assertEqual(make_linked_list([1,3,4]), get_sol().mergeNodes(make_linked_list([0,1,0,3,0,2,2,0])))
