import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        cur_time=-1
        total=0
        for arrival,prep in customers:
            if cur_time<=arrival:
                cur_time=arrival+prep
                total+=prep
            else:
                total+=cur_time-arrival
                total+=prep
                cur_time+=prep

        return total/len(customers)

class MyTestCase(unittest.TestCase):
    def test_1(self):
        customers = [[1,2],[2,5],[4,3]]
        Output= 5.00000
        self.assertEqual(Output, get_sol().averageWaitingTime(customers))
    def test_2(self):
        customers = [[5,2],[5,4],[10,3],[20,1]]
        Output= 3.25000
        self.assertEqual(Output, get_sol().averageWaitingTime(customers))
    # def test_3(self):
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
    # def test_9(self):