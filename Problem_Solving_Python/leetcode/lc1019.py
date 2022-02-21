from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self): return str(self.val) + "->" + str(self.next)
# class Solution2:
#     def nextLargerNodes(self, head: ListNode) -> List[int]:
        # maybe it is possible to do it in one pass
class Solution:
    def getLen(self,head): return 1+self.getLen(head.next) if head else 0
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        n=self.getLen(head)
        res=[0]*n
        st=[]
        cur=head
        for i in range(n):
            while st and st[-1][0]<cur.val:
                val,idx=st.pop()
                res[idx]=cur.val
            st.append([cur.val,i])
            cur=cur.next
        return res

class tester(unittest.TestCase):
    def test01(self):
        Input= [2,1,5]
        Output= [5,5,0]
        Input = make_linked_list(Input)
        self.assertEqual(Output, get_sol().nextLargerNodes(Input))
    def test02(self):
        Input= [2,7,4,3,5]
        Output= [7,0,5,5,0]
        Input = make_linked_list(Input)
        self.assertEqual(Output, get_sol().nextLargerNodes(Input))
    def test03(self):
        Input= [1,7,5,1,9,2,5,1]
        Output= [7,9,9,9,0,5,0,0]
        Input = make_linked_list(Input)
        self.assertEqual(Output, get_sol().nextLargerNodes(Input))
