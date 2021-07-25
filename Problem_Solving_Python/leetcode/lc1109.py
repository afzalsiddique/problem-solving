import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # line sweep
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ENOUGH = 2*10**4+2
        li=[0]*ENOUGH
        for start,end,seat in bookings:
            li[start]+=seat
            li[end+1]-=seat

        cnt=0
        res=[]
        for i in range(1,n+1):
            cnt+=li[i]
            res.append(cnt)
        return res
class tester(unittest.TestCase):
    def test_1(self):
        bookings = [[1,2,10],[2,3,20],[2,5,25]]
        n = 5
        Output= [10,55,45,25,25]
        self.assertEqual(Output, get_sol().corpFlightBookings(bookings,n))
    def test_2(self):
        bookings = [[1,2,10],[2,2,15]]
        n = 2
        Output= [10,25]
        self.assertEqual(Output, get_sol().corpFlightBookings(bookings,n))
    # def test_3(self):
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):