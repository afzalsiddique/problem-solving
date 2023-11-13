from itertools import accumulate,permutations; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import heappop,heappush,heapify; import unittest; from typing import List, Optional, Union, Dict; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list, ListNode
from Problem_Solving_Python.template.binary_tree import deserialize,serialize

def get_sol(): return Solution()
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        hp=[[lList.val,lList] for lList in lists if lList]
        heapify(hp)
        dummy=ListNode(-99)
        head=dummy
        while hp:
            top,ll=heappop(hp)
            if ll.next:
                ll=ll.next
                heappush(hp,[ll.val,ll])
            head.next(top)
            head=head.next
        return dummy.next


class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(make_linked_list([1,1,2,3,4,4,5,6]), get_sol().mergeKLists(list(map(make_linked_list,[[1,4,5],[1,3,4],[2,6]]))))
    def test02(self):
        self.assertEqual([[4],[9],[3,0,1],[8],[7]], get_sol().verticalOrder(des([3,9,8,4,0,1,7])))
    def test03(self):
        self.assertEqual([[4],[9,5],[3,0,1],[8,2],[7]], get_sol().verticalOrder(des([3,9,8,4,0,1,7,None,None,None,2,5])))
    def test04(self):
        self.assertEqual([[4],[2,7,8],[1,5,6,10,11,10],[3,9]], get_sol().verticalOrder(des([1,2,3,4,5,6,None,None,7,8,None,None,9,None,10,None,11,10])))
    def test05(self):
        self.assertEqual([[26],[5,11,53],[3,9,10,64,27],[6,18,15],[21]], get_sol().verticalOrder(des([3,5,6,None,9,10,None,11,18,53,15,26,64,27,21])))
    def test06(self):
        self.assertEqual([[26,9],[5,11,53],[3,9,10,64,27],[2,6,39,18,15,12,48],[1,34,14,66,7,55,89,42,86,21],[0,8,37,69,17,32,80,75],[4,29,45,22,51,57],[13,35,84,65],[19],[58]], get_sol().verticalOrder(des([0,1,4,2,8,37,13,3,34,14,29,66,45,22,19,5,6,39,69,None,17,None,35,None,None,None,None,32,None,None,58,None,9,10,7,None,55,89,None,42,51,57,None,86,None,None,None,11,18,53,15,12,None,None,None,None,None,48,None,80,84,75,65,None,None,26,64,27,21,9])))
