from itertools import accumulate,permutations; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import heappop,heappush,heapify; import unittest; from typing import List, Optional, Union; from functools import cache; from operator import lt, gt; import sortedcontainers
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list,ListNode
from Problem_Solving_Python.template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(-1)
        head=dummy
        carry=0
        while l1 or l2:
            a=l1.val if l1 else 0
            b=l2.val if l2 else 0
            val=a+b+carry
            head.next=ListNode(val%10)
            carry=val//10
            head=head.next
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None
        if carry:
            head.next=ListNode(carry)


        return dummy.next


class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual([0,3,1,2,4], get_sol().timeTaken([0,1,1,2,4], [0,1,0,0,1]))
    def test2(self):
        self.assertEqual([0,2,1], get_sol().timeTaken([0,0,0], [1,0,1]))
    # def test3(self):
    # def test4(self):
    # def test5(self):
    # def test6(self):
    # def test7(self):
    # def test8(self):
    # def test9(self):
