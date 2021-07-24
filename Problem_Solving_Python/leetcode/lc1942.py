import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, lru_cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        n=len(times)
        pq = [i for i in range(n)]
        heapify(pq)
        arrivals=[(times[i][0],i) for i in range(n)]
        leavings=[(times[i][1],i) for i in range(n)]
        arrivals.sort()
        leavings.sort()
        # print(arrivals)
        # print(leavings)
        i,j=0,0
        chairs_occupied = {}
        while i<n and j<n:
            if arrivals[i][0]<leavings[j][0]:
                friend = arrivals[i][1]
                chair_no = heappop(pq)
                chairs_occupied[friend]= chair_no
                if friend==targetFriend: return chair_no
                i+=1
            else:
                friend = leavings[j][1]
                chair_no=chairs_occupied[friend]
                heappush(pq,chair_no)
                j+=1

class tester(unittest.TestCase):
    def test_1(self):
        times = [[1,4],[2,3],[4,6]]
        targetFriend = 1
        Output= 1
        self.assertEqual(Output, get_sol().smallestChair(times,targetFriend))
    def test_2(self):
        times = [[3,10],[1,5],[2,6]]
        targetFriend = 0
        Output= 2
        self.assertEqual(Output, get_sol().smallestChair(times,targetFriend))
    def test_3(self):
        times = [[4,5],[12,13],[5,6],[1,2],[8,9],[9,10],[6,7],[3,4],[7,8],[13,14],[15,16],[14,15],[10,11],[11,12],[2,3],[16,17]]
        targetFriend = 15
        Output= 0
        self.assertEqual(Output, get_sol().smallestChair(times,targetFriend))
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
