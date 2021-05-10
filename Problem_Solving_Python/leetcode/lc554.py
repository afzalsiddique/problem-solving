import itertools
import math
import operator
import random
from bisect import *
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List
def get_sol(): return Solution()



class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        di=defaultdict(int)
        di['empty']=0
        def calculate_prefix_sum(row):
            pre=0
            for i in range(len(row)-1):
                pre+=row[i]
                di[pre]+=1
        for row in wall:
            calculate_prefix_sum(row)

        return len(wall) - max(di.values())



class tester(unittest.TestCase):
    def test01(self):
        wall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
        Output= 2
        self.assertEqual(Output,get_sol().leastBricks(wall))
    def test02(self):
        wall = [[1],[1],[1]]
        Output= 3
        self.assertEqual(Output,get_sol().leastBricks(wall))
