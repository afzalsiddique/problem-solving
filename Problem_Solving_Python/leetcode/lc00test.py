from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional,Union; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
from Problem_Solving_Python.template.binary_tree import deserialize,serialize
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x:(x[1],x[0]))
        pq = []
        time=0
        res=0
        for i,(duration,deadline) in enumerate(courses):
            while pq and time+duration>deadline:
                time-=pq[0]*(-1)
                heappop(pq)
            if time+duration<=deadline:
                heappush(pq,-duration)
                time+=duration
                res=max(res,len(pq))
        return res

class Correct:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x:x[1])
        pq=[]
        total_time=0
        for time,deadline in courses:
            total_time+=time
            heappush(pq,-time)
            if total_time>deadline:
                tmp=heappop(pq)*(-1)
                total_time-=tmp
        return len(pq)

class Tester(unittest.TestCase):
    def test01(self):
        # a=[7, 1, 7, 1, 7, 1], 3
        a=[[7,17],[3,12],[5,20],[10,19],[4,18]]
        self.assertEqual(Correct().scheduleCourse(a), Solution().scheduleCourse(a))
