from itertools import accumulate,permutations; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import heappop,heappush,heapify; import unittest; from typing import List, Optional, Union, Dict; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list, ListNode
from Problem_Solving_Python.template.binary_tree import deserialize,serialize

def get_sol(): return Solution()
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        class Wrapper(ListNode):
            def __lt__(self, other): return self.val<other.val
        hp=[[lList.val,random.random(),lList] for lList in lists if lList]
        heapify(hp)
        dummy=ListNode(-99)
        head=dummy
        while hp:
            top,_,ll=heappop(hp)
            if ll.next:
                ll=ll.next
                heappush(hp,[ll.val,random.random(),ll])
            head.next=ListNode(top)
            head=head.next
        return dummy.next


class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(make_linked_list([1,1,2,3,4,4,5,6]),get_sol().mergeKLists(list(map(make_linked_list,[[1,4,5],[1,3,4],[2,6]]))))
    def test02(self):
        self.assertEqual(make_linked_list([]),get_sol().mergeKLists(list(map(make_linked_list,[[]]))))
    def test03(self):
        self.assertEqual(make_linked_list([]),get_sol().mergeKLists(list(map(make_linked_list,[]))))
    # def test04(self):
    # def test05(self):
    # def test06(self):
    # def test07(self):
    # def test08(self):
    # def test09(self):
    # def test10(self):
    # def test11(self):
    # def test12(self):
