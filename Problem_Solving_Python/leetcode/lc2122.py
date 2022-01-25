from itertools import accumulate; from math import floor,ceil,log2; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import *
def get_sol(): return Solution()
class Solution:
    def recoverArray(self, A: List[int]) -> List[int]:
        def valid(k):
            count=Counter(A) # don't forget to reinitialize
            cnt=0
            res=[]
            for x in A:
                if count[x] and count[x+2*k]:
                    count[x]-=1
                    count[x+2*k]-=1
                    res.append(x+k)
                    cnt+=2
            return cnt==n,res

        n=len(A)
        A.sort()
        sett=set()
        for i in range(1,n):
            diff=A[i]-A[0]
            if diff!=0 and diff%2==0: # k must be positive as per the constraint
                sett.add(diff//2)
        for k in sett:
            tmp,res=valid(k)
            if tmp:
                return res


class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual([3,7,11], get_sol().recoverArray([2,10,6,4,8,12]))
    def test02(self):
        self.assertEqual([2,2], get_sol().recoverArray([1,1,3,3]))
    def test03(self):
        self.assertEqual([220], get_sol().recoverArray([5,435]))
    def test04(self):
        self.assertEqual([51,100,149], get_sol().recoverArray([1,50,99,101,150,199]))
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
    # def test_9(self):

