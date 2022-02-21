from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    def func(self, count1, count2):
        maxx1=max(count1.keys(), key=lambda x:count1[x])
        maxx2=max(count2.keys(), key=lambda x:count2[x])
        n1=sum(count1.values())
        n2=sum(count2.values())
        if count1[maxx1]<count2[maxx2]: return self.func(count2,count1)
        if maxx1==maxx2:
            cnt2=count2[maxx2]
            count2.pop(maxx2)
            maxx4=max(count2.keys(), key=lambda x:count2[x])
            res=n1-count1[maxx1]+n2-count2[maxx4]
            count2[maxx2]=cnt2

            cnt1=count1[maxx1]
            count1.pop(maxx1)
            maxx3=max(count1.keys(), key=lambda x:count1[x])
            res=min(res,n2-count2[maxx2]+n1-count1[maxx3])
            count1[maxx1]=cnt1
        else:
            res=n1-count1[maxx1]+n2-count2[maxx2]
        return res

    def minimumOperations(self, A: List[int]) -> int:
        n=len(A)
        even=Counter()
        odd=Counter()
        even[-1]=0
        odd[-1]=0
        for i in range(0,n,2):
            even[A[i]]+=1
        for i in range(1,n,2):
            odd[A[i]]+=1
        return self.func(even,odd)


class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(3, get_sol().minimumOperations([3,1,3,2,4,3]))
    def test2(self):
        self.assertEqual(2, get_sol().minimumOperations([1,2,2,2,2]))
    # def test3(self):
    # def test4(self):
    # def test5(self):
    # def test6(self):
