from itertools import accumulate,permutations; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import heappop,heappush,heapify; import unittest; from typing import List, Optional, Union; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
from Problem_Solving_Python.template.binary_tree import deserialize
def get_sol(): return Solution()
class MaxHeap(list):
    def __init__(self): super().__init__()
    def top(self): return -self[0]
    def push(self, val): heappush(self, -val)
    def heappop(self): return -heappop(self)
class Solution:
    # https://www.youtube.com/watch?v=ey8FxYsFAMU
    # For any iteration check if taking the course, total_time will exceed the deadline
    # 1. If no, then just add the course time to the total time
    # 2. If yes, then swap with the course which has the longest duration.
    #    Swapping with longer duration course will reduce total_time.
    #    To get the longest duration we need to have a max_heap.
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x:(x[1],x[0]))
        time=0
        pq = MaxHeap()
        for dur,deadline in courses:
            pq.push(dur) # push it to the heap first
            time+=dur
            if time>deadline: # then check the elapsed time
                time-=pq.heappop()
        return len(pq)
class Solution2:
    # incorrect. run test case [[7,17],[3,12],[5,20],[10,19],[4,18]] to understand
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x:(x[1],x[0]))
        time=0
        pq = MaxHeap()
        res=0
        for i,(dur,lastDay) in enumerate(courses):
            while pq and time+dur>lastDay:
                time-=pq.pop()
            if time+dur<=lastDay:
                time+=dur
                pq.push(dur)
                res=max(res,len(pq))
        return res
class Solution3:
    # dp. tle
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        @cache
        def func(i,cur_time):
            if i==n: return 0
            this_time,deadline=courses[i]
            maxx=float('-inf')
            if cur_time+this_time<=deadline: # take this course
                maxx=max(maxx,func(i+1,cur_time+this_time)+1)
            maxx=max(maxx,func(i+1,cur_time)) # do not take this course
            return maxx

        n=len(courses)
        courses.sort(key=lambda x:x[1])
        return func(0,0)

class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(3, get_sol().scheduleCourse(courses = [[100,200],[200,1300],[1000,1250],[2000,3200]]))
    def test2(self):
        self.assertEqual(1, get_sol().scheduleCourse(courses = [[1,2]]))
    def test3(self):
        self.assertEqual(0, get_sol().scheduleCourse(courses = [[3,2],[4,3]]))
    def test4(self):
        self.assertEqual(3, get_sol().scheduleCourse([[7,17],[9,10],[5,20],[4,18]]))
    def test5(self):
        self.assertEqual(4, get_sol().scheduleCourse([[7,17],[3,12],[5,20],[4,18]]))
    def test6(self):
        self.assertEqual(4, get_sol().scheduleCourse([[7,17],[3,12],[10,20],[9,10],[5,20],[10,19],[4,18]]))
    def test7(self):
        self.assertEqual(4, get_sol().scheduleCourse([[7,17],[3,12],[5,20],[10,19],[4,18]]))
    def test8(self):
        self.assertEqual(4, get_sol().scheduleCourse([[3,12],[7,17],[4,18],[10,19],[5,20]]))
    def test9(self):
        self.assertEqual(3, get_sol().scheduleCourse([[100,200],[1000,1200],[300,1300],[400,1300]]))
