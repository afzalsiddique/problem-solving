from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
from Problem_Solving_Python.template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    # https://www.youtube.com/watch?v=_sA1xI4XK0c
    def countSmaller(self, nums: List[int]) -> List[int]:
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
                    res[li[i][1]]+=(hi-j+1)
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

        li = [[x,i] for i,x in enumerate(nums)]
        res = [0]*len(nums)
        mergeSort(0,len(li)-1)
        return res
        return [x[0] for x in li]


class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual([3,3,5,5,5,0,0,0,0,0], get_sol().countSmaller([7,8,11,12,13,4,5,6,9,10]))
    def test2(self):
        self.assertEqual([2,1,1,0], get_sol().countSmaller([5,2,6,1]))
