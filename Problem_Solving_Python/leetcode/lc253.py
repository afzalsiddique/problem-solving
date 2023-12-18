from itertools import accumulate,permutations; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import heappop,heappush,heapify; import unittest; from typing import List, Optional, Union; from functools import cache; from operator import lt, gt; import sortedcontainers
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
from Problem_Solving_Python.template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
# similar to 2251
class Solution:
    # SortedDict
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        di = sortedcontainers.SortedDict()
        for a,b in intervals:
            di[a]=di.get(a,0)+1
            di[b]=di.get(b,0)-1
        count = list(accumulate(di.values())) # prefix sum
        return max(count)
class Solution2:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        di=defaultdict(int)
        for a,b in intervals:
            di[a]+=1
            di[b]-=1

        count=[]
        for k in sorted(di.keys()):
            count.append(di[k])
        pre_sum=accumulate(count)
        return max(pre_sum)



class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual(2, get_sol().minMeetingRooms([[0,30],[5,10],[15,20]]))
    def test2(self):
        self.assertEqual(1, get_sol().minMeetingRooms([[7,10],[2,4]]))
    def test3(self):
        self.assertEqual(1, get_sol().minMeetingRooms([[13,15],[1,13]]))
    # def test4(self):
    # def test5(self):
    # def test6(self):
    # def test7(self):
    # def test8(self):
    # def test9(self):
