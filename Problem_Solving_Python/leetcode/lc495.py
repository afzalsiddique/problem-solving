from itertools import accumulate; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        last=-1
        total=0
        for t in timeSeries:
            if t<last:
                total-=last-t
            total+=duration
            last=t+duration
        return total
class Solution3:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        last=-1
        total=0
        for t in timeSeries:
            if t<=last:
                total-=last-t+1
            total+=duration
            last=t+duration-1
        return total
class Solution4:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries: return 0
        ans=0
        for i in range(len(timeSeries)-1):
            if timeSeries[i]+duration<timeSeries[i+1]:
                ans+=duration
            else:
                ans += timeSeries[i+1]-timeSeries[i]
        ans+=duration
        return ans

class Solution2:
    # based on merge interval lc56
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        n=len(timeSeries)
        intervals=[]
        for time in timeSeries:
            intervals.append([time,time+duration-1])
        # print(intervals)
        res = []
        intervals.sort()
        res.append([intervals[0][0],intervals[0][1]])
        for i in range(1,n):
            new_start,new_end=intervals[i][0],intervals[i][1]
            last_start,last_end=res[-1][0],res[-1][1]
            if last_start<=new_start<=last_end or last_start<=new_end<=last_end:
                res[-1][0]=min(new_start,last_start)
                res[-1][1]=max(new_end,last_end)
            else:
                res.append([new_start,new_end])
        ans = 0
        for start,end in res:
            ans+=end-start+1
        return ans


class tester(unittest.TestCase):
    def test01(self):
        timeSeries = [1,4]
        duration = 2
        Output= 4
        self.assertEqual(Output,get_sol().findPoisonedDuration(timeSeries, duration))
    def test02(self):
        timeSeries = [1,2]
        duration = 2
        Output= 3
        self.assertEqual(Output,get_sol().findPoisonedDuration(timeSeries, duration))
    def test03(self):
        timeSeries = [1,4]
        duration = 3
        Output= 6
        self.assertEqual(Output,get_sol().findPoisonedDuration(timeSeries, duration))
    def test04(self):
        timeSeries = [1,3]
        duration = 3
        Output= 5
        self.assertEqual(Output,get_sol().findPoisonedDuration(timeSeries, duration))
    def test05(self):
        timeSeries = []
        duration = 100000
        Output= 0
        self.assertEqual(Output,get_sol().findPoisonedDuration(timeSeries, duration))
