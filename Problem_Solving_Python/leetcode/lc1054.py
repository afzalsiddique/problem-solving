import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        n=len(barcodes)
        res=[0]*n
        count = Counter(barcodes)
        pq=[]
        for k,freq in count.items():
            pq.append([-freq,k])
        heapify(pq)
        i=0 # fill up the even positions
        while i<n and pq:
            while i<n and pq and pq[0][0]:
                res[i]=pq[0][1]
                pq[0][0]+=1 # because max_heap
                i+=2
            if not pq[0][0]: heappop(pq)

        i=1 # fill up the odd positions
        while i<n and pq:
            while i<n and pq and pq[0][0]:
                res[i]=pq[0][1]
                pq[0][0]+=1 # because max_heap
                i+=2
            if not pq[0][0]: heappop(pq)
        return res

class tester(unittest.TestCase):
    def test1(self):
        barcodes = [1,1,1,2,2,2]
        Output= [2,1,2,1,2,1]
        self.assertEqual(Output,get_sol().rearrangeBarcodes(barcodes))
    def test2(self):
        barcodes = [1,1,1,1,2,2,3,3]
        Output= [1,3,1,3,1,2,1,2]
        self.assertEqual(Output,get_sol().rearrangeBarcodes(barcodes))
    def test3(self):
        barcodes = [1,1,2]
        Output= [1,2,1]
        self.assertEqual(Output,get_sol().rearrangeBarcodes(barcodes))
    def test4(self):
        barcodes = [1,1,1,1,2,2,3,3]
        Output= 'many answers'
        self.assertEqual(Output,get_sol().rearrangeBarcodes(barcodes))

    # def test5(self):
    # def test6(self):
    # def test7(self):
