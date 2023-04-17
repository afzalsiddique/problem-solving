from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional,Union; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
from Problem_Solving_Python.template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
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



class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual(2,get_sol().nextGreaterElement([7,5,4,3,6],[]))
    # def test02(self):
    # def test03(self):
    # def test04(self):
