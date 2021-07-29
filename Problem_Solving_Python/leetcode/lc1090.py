import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List
def get_sol(): return Solution()
class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
        n=len(values)
        pq = [[-values[i],labels[i]] for i in range(n)]
        heapify(pq)
        res=0
        usage=Counter()
        left=Counter(labels)
        while num_wanted and pq:
            while True:
                if not num_wanted: break
                if not pq: break
                lab=pq[0][1]
                if left[lab]>0 and usage[lab]<use_limit: break
                heappop(pq)
            if not pq: break
            tmp,lab= heappop(pq)
            tmp*=(-1) # max_heap
            usage[lab]+=1
            left[lab]-=1
            res+=tmp
            num_wanted-=1
        return res


class tester(unittest.TestCase):
    def test_1(self):
        values,labels,num_wanted,use_limit = [5,4,3,2,1],[1,1,2,2,3],3,1
        Output= 9
        self.assertEqual(Output,get_sol().largestValsFromLabels(values,labels,num_wanted,use_limit))
    def test_2(self):
        values,labels,num_wanted,use_limit = [5,4,3,2,1],[1,3,3,3,2],3,2
        Output= 12
        self.assertEqual(Output,get_sol().largestValsFromLabels(values,labels,num_wanted,use_limit))
    def test_3(self):
        values,labels,num_wanted,use_limit = [9,8,8,7,6],[0,0,0,1,1],3,1
        Output= 16
        self.assertEqual(Output,get_sol().largestValsFromLabels(values,labels,num_wanted,use_limit))
    def test_4(self):
        values,labels,num_wanted,use_limit = [9,8,8,7,6],[0,0,0,1,1],3,2
        Output= 24
        self.assertEqual(Output,get_sol().largestValsFromLabels(values,labels,num_wanted,use_limit))
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
