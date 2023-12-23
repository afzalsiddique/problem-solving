from itertools import accumulate,permutations; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import heappop,heappush,heapify; import unittest; from typing import List, Optional, Union; from functools import cache; from operator import lt, gt; import sortedcontainers
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list,ListNode
from Problem_Solving_Python.template.binary_tree import deserialize,serialize
# def get_sol(*args): return Solution().peakIndexInMountainArray(*args)
def get_sol(): return Solution()

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n<0: return 1/self.myPow(x,-n)
        if n==0: return 1
        ans=self.myPow(x,n//2)
        return ans*ans*(x if n%2 else 1)


class MyTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual( 4.00000, get_sol().myPow(2,2))
    def test_2(self):
        self.assertEqual( 16.00000, get_sol().myPow(2,4))
    def test_3(self):
        self.assertEqual( 128, get_sol().myPow(2,7))
    def test_4(self):
        self.assertEqual( 9.26100, get_sol().myPow(2.1, 3))
    def test_5(self):
        self.assertEqual( 0.25000, get_sol().myPow(2,-2))
    def test_6(self):
        self.assertEqual(54.83508, get_sol().myPow(0.44894, -5))
    def test_7(self):
        self.assertEqual(4.00, get_sol().myPow(-2.00000, 2))


# Cases=[
#     [0, 1, 0],
#     [0, 2, 1, 0],
#     [0, 10, 5, 2],
#     [3, 4, 5, 1]
# ]
# PARAMETERS=1
# Expected=[1,1,1,2]
#
#
# class MyTestCase(unittest.TestCase):
#     def test00(self):
#         testNo=0
#         self.assertEqual(Expected[testNo], get_sol(*Cases[testNo*PARAMETERS:(testNo+1)*PARAMETERS]))
#     def test01(self):
#         testNo=1
#         self.assertEqual(Expected[testNo], get_sol(*Cases[testNo*PARAMETERS:(testNo+1)*PARAMETERS]))
#     def test02(self):
#         testNo=2
#         self.assertEqual(Expected[testNo], get_sol(*Cases[testNo*PARAMETERS:(testNo+1)*PARAMETERS]))
#     def test03(self):
#         testNo=3
#         self.assertEqual(Expected[testNo], get_sol(*Cases[testNo*PARAMETERS:(testNo+1)*PARAMETERS]))
    # def test04(self):
    #     testNo=4
    #     self.assertEqual(Expected[testNo], get_sol(*Cases[testNo*PARAMETERS:(testNo+1)*PARAMETERS]))
    # def test05(self):
    #     testNo=5
    #     self.assertEqual(Expected[testNo], get_sol(*Cases[testNo*PARAMETERS:(testNo+1)*PARAMETERS]))


