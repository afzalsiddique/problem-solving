from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
from Problem_Solving_Python.template.binary_tree import deserialize
def get_sol(): return Solution()
class Solution:
    def sort(self,li) -> List[int]:
        def mergeSort(li):
            n=len(li)
            if n==1:
                return [li[0]]
            mid=n//2
            L=mergeSort(li[:mid])
            R=mergeSort(li[mid:])
            return merge(L,R)

        def merge(L,R):
            i,j=0,0
            tmp=[]
            while i<len(L) and j<len(R):
                if L[i]>R[j]:
                    tmp.append(L[i])
                    i+=1
                else:
                    tmp.append(R[j])
                    j+=1
            tmp.extend(L[i:] or R[j:])
            return tmp

        return mergeSort(li)

class mytestcase(unittest.TestCase):
    def test1(self):
        li = [5,2,3,1]
        self.assertEqual(sorted(li,reverse=True), get_sol().sort(li))
    def test2(self):
        li =  [5,1,1,2,0,0]
        self.assertEqual(sorted(li,reverse=True), get_sol().sort(li))
    # def test3(self):
    # def test4(self):
    # def test5(self):
    # def test6(self):
    # def test7(self):
    # def test8(self):
