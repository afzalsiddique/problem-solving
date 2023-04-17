from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
from Problem_Solving_Python.template.binary_tree import deserialize
def get_sol(): return Solution()
class MaxHeap(list):
    def __init__(self):
        super().__init__()
        self.li = []
    def push(self,x):
        heappush(self.li,-x)
    def heappop(self):
        return heappop(self.li)*(-1)
    def top(self):
        return self.li[0]*(-1)
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x:(x[0],x[1]))
        pq = []
        time=0
        res=0
        for i,(duration,deadline) in enumerate(courses):
            while pq and time+duration>deadline:
                prevDeadline,prevDuration = heappop(pq)
                time-=prevDeadline
            if time+duration<=deadline:
                heappush(pq,[deadline,duration])
                time+=duration
                res=max(res,len(pq))
        return res



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
        self.assertEqual(4, get_sol().scheduleCourse([[3,12],[7,17],[4,18],[10,19],[5,20]]))
    def test8(self):
        self.assertEqual(3, get_sol().scheduleCourse([[100,200],[1000,1200],[300,1300],[400,1300]]))
