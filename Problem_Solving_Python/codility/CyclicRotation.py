from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
def get_sol(a,b): return solution(a,b)
def solution(nums, k):
    n=len(nums)
    if n==0 or k<=0: return nums
    curIdx=0
    startIdx=0
    numToBeRotated=nums[startIdx]
    for i in range(n):
        nxtIdx=(curIdx+k)%n
        nxt = nums[nxtIdx]
        nums[nxtIdx]=numToBeRotated
        numToBeRotated = nxt
        curIdx = nxtIdx


        if curIdx==startIdx: # start a new cycle
            curIdx=(curIdx+1)%n
            numToBeRotated = nums[curIdx]
            startIdx+=1
    return nums

class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual( [5,6,7,1,2,3,4],get_sol([1,2,3,4,5,6,7], 3))
    def test02(self):
        self.assertEqual( [3,4,1,2],get_sol([1,2,3,4],2))
    def test03(self):
        self.assertEqual( [1],get_sol([1], 1))
    def test04(self):
        self.assertEqual([1,2],get_sol([1,2], 2))
    def test05(self):
        self.assertEqual([-1],get_sol([-1], 2))
    def test06(self):
        self.assertEqual([2,3,1],get_sol([1,2,3], 2))
    def test07(self):
        self.assertEqual([4,5,6,1,2,3],get_sol([1,2,3,4,5,6], 3))
    def test08(self):
        self.assertEqual([7,8,9,1,2,3,4,5,6],get_sol([1,2,3,4,5,6,7,8,9], 3))
    def test09(self):
        self.assertEqual([],get_sol([], 3))
    def test10(self):
        self.assertEqual([9, 7, 6, 3, 8],get_sol([3, 8, 9, 7, 6], 3))