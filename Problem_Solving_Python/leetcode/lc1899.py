import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        cur = [0,0,0]
        for x,y,z in triplets:
            if x<=target[0] and y<=target[1] and z<=target[2]:
                cur = [max(cur[0], x), max(cur[1],y), max(cur[2],z)]
        return True if cur==target else False

class MyTestCase(unittest.TestCase):
    def test1(self):
        triplets,target = [[2,5,3],[1,8,4],[1,7,5]],  [2,7,5]
        Output= True
        self.assertEqual(Output, get_sol().mergeTriplets(triplets, target))
    def test2(self):
        triplets,target = [[1,3,4],[2,5,8]],  [2,5,8]
        Output= True
        self.assertEqual(Output, get_sol().mergeTriplets(triplets, target))
    def test3(self):
        triplets,target = [[2,5,3],[2,3,4],[1,2,5],[5,2,3]],  [5,5,5]
        Output= True
        self.assertEqual(Output, get_sol().mergeTriplets(triplets, target))
    def test4(self):
        triplets,target = [[3,4,5],[4,5,6]],  [3,2,5]
        Output= False
        self.assertEqual(Output, get_sol().mergeTriplets(triplets, target))
    # def test5(self):
    # def test6(self):
    # def test7(self):
