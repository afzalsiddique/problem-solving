import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        n =len(groupSizes)
        di=defaultdict(list)
        for person in range(n):
            size = groupSizes[person]
            if len(di[size]) == 0: # no group created at all. so create new group
                new_list = []
                new_list.append(person)
                di[size].append(new_list)
            elif len(di[size][-1])==size: # last group already filled. so create new group
                new_list = []
                new_list.append(person)
                di[size].append(new_list)
            else:
                di[size][-1].append(person)
        res=[]
        for key in di:
            for group in di[key]:
                res.append(group)
        return res
class tester(unittest.TestCase):
    def test1(self):
        groupSizes = [3,3,3,3,3,1,3]
        Output= [[5],[0,1,2],[3,4,6]]
        Output.sort()
        self.assertEqual(Output,sorted(get_sol().groupThePeople(groupSizes)))
    def test2(self):
        groupSizes = [2,1,3,3,3,2]
        Output= [[1],[0,5],[2,3,4]]
        Output.sort()
        self.assertEqual(Output,sorted(get_sol().groupThePeople(groupSizes)))
