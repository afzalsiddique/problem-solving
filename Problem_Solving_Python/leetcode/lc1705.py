import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # only push to the heap when it already has been produced
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        ans, i, n = 0, 0, len(apples)
        h = []
        while i < n or h:
            # only push to heap when you have a valid i, and the apple has atleast one day to stay fresh.
            if i<n and apples[i] > 0:
                heappush(h, [i + days[i], apples[i]])
            # remove the rotten apples batches and the batches with no apples left (which might have got consumed).
            while h and (h[0][0] <= i or h[0][1] <= 0):
                heappop(h)
            # only if there is batch in heap after removing all the rotten ones, you can eat. else wait for the subsequent days for new apple batch by incrementing i.
            if h:
                h[0][1]-=1
                ans+=1
            i+=1
        return ans
class Solution2:
    # only push to the heap when it already has been produced
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        n=len(apples)
        pq=[]
        i=0
        eaten=0
        while i<n:
            while pq and pq[0][0]<=i:
                heappop(pq)
            if apples[i]!=0:
                heappush(pq,[i+days[i],apples[i]])
            if pq:
                eaten+=1
                pq[0][1]-=1
                if pq[0][1]==0: heappop(pq)
            i+=1
        while pq:
            if pq and pq[0][0]<=i: heappop(pq)
            if not pq: break
            day,apple=pq[0]
            if day-i<=apple: # not enough days
                eaten+=day-i
                i=day
            else: # not enough apples
                eaten+=apple
                i+=apple
                heappop(pq)
        return eaten
class Solution3:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        n=len(apples)
        pq=[]
        i=0
        eaten=0
        while i<n:
            while pq and pq[0][0]<=i:
                heappop(pq)
            if apples[i]!=0:
                heappush(pq,[i+days[i],apples[i]])
            if pq:
                eaten+=1
                pq[0][1]-=1
                if pq[0][1]==0: heappop(pq)
            i+=1
        while pq:
            if pq and pq[0][0]<=i: heappop(pq)
            if not pq: break
            eaten+=1
            pq[0][1]-=1
            if pq[0][1]==0: heappop(pq)
            i+=1
        return eaten
class MyTestCase(unittest.TestCase):
    def test_1(self):
        apples,days = [1,2,3,5,2], [3,2,1,4,2]
        Output= 7
        self.assertEqual(Output, get_sol().eatenApples(apples,days))
    def test_2(self):
        apples,days = [3,0,0,0,0,2], [3,0,0,0,0,2]
        Output= 5
        self.assertEqual(Output, get_sol().eatenApples(apples,days))
    def test_3(self):
        apples,days = [2,1,1,4,5], [10,10,6,4,2]
        Output= 8
        self.assertEqual(Output, get_sol().eatenApples(apples,days))
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
    # def test_9(self):
