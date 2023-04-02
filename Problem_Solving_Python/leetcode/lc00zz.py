from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
from Problem_Solving_Python.template.binary_tree import deserialize
def get_sol(): return Solution()
class Solution:
    def sortArray(self, li) -> List[List[int]]: # sort array with initial index before sorting of each element
        def mergeSort(lo,hi):
            if lo==hi:
                return
            mid=(lo+hi)//2
            mergeSort(lo,mid)
            mergeSort(mid+1,hi)
            merge(lo, mid, hi)

        def merge(lo, mid, hi):
            i,j=lo,mid+1
            tmp=[]
            while i<=mid and j<=hi:
                if li[i][0]>li[j][0]:
                    tmp.append(li[i])
                    i+=1
                else:
                    tmp.append(li[j])
                    j+=1
            while i<=mid:
                tmp.append(li[i])
                i+=1
            while j<=hi:
                tmp.append(li[j])
                j+=1
            for k in range(len(tmp)):
                li[lo+k]=tmp[k]

        li = [[x,i] for i,x in enumerate(li)]
        mergeSort(0,len(li)-1)
        return li

class Tester(unittest.TestCase):
    def test1(self):
        li = [7,5,6,4]
        # 7 was at index 0 before sorting
        # 6 was at index 2 before sorting
        # 5 was at index 1 before sorting
        # 4 was at index 3 before sorting
        expected = [[7, 0], [6, 2], [5, 1], [4, 3]]
        self.assertEqual(expected, get_sol().sortArray(li))
    def test2(self):
        li = [2,5,1]
        self.assertEqual([[5, 1], [2, 0], [1, 2]], get_sol().sortArray(li))
    # def test4(self):
    # def test5(self):
    # def test6(self):
    # def test7(self):
    # def test8(self):
