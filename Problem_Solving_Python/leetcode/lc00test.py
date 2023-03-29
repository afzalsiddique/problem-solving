from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        n=len(courses)
        courses.sort(key=lambda x:(x[0],x[1]))
        time=0
        res=0
        for dur,last in courses:
            if time+dur<=last:
                res+=1
                time+=dur
        return res

class Correct:
    # https://www.youtube.com/watch?v=ey8FxYsFAMU
    # For any iteration check if taking the course, total_time will exceed the deadline
    # 1. If no, then just add the course time to the total time
    # 2. If yes, then swap with the course which has the longest duration.
    #    Swapping with longer duration course will reduce total_time.
    #    To get the longest duration we need to have a max_heap.
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
        a=[[7,17],[3,12],[5,20],[4,18]]
        self.assertEqual(Correct().scheduleCourse(a), Solution().scheduleCourse(a))
