from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    def maximumTop(self, A: List[int], k: int) -> int:
        n=len(A)
        if n==1:
            if k%(2*n)==0:
                return A[0]
            return -1
        if k==0:
            return A[0]
        if k==1:
            if n==1:
                return -1
            return A[1]
        if k<n:
            option1=max(A[:k-1])
            option2=A[k]
            return max(option1,option2)
        if k==n:
            return max(A[:-1])
        if n<k<=2*n:
            return max(A)
        return max(A)



class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(5, get_sol().maximumTop([5,2,2,4,0,6],4))
    def test02(self):
        self.assertEqual(-1, get_sol().maximumTop([2],1))
    def test03(self):
        self.assertEqual(2, get_sol().maximumTop([1,2,3],3))
    def test04(self):
        self.assertEqual(3, get_sol().maximumTop([1,2,3],4))
    def test05(self):
        self.assertEqual(3, get_sol().maximumTop([1,2,3],5))
    def test06(self):
        self.assertEqual(3, get_sol().maximumTop([1,2,3],6))
    def test07(self):
        self.assertEqual(99, get_sol().maximumTop([1,2,5,99,4],3))
    def test08(self):
        self.assertEqual(99, get_sol().maximumTop([1,99,5,3,4],3))
    def test09(self):
        self.assertEqual(-1, get_sol().maximumTop([18],3))
    def test10(self):
        self.assertEqual(61, get_sol().maximumTop([17,61,5,1,44],100))
