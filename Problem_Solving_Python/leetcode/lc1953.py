import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/maximum-number-of-weeks-for-which-you-can-work/discuss/1375381/C%2B%2B-max-element-solution.-Greedy
    def numberOfWeeks(self, milestones: List[int]) -> int:
        summ=sum(milestones)
        maxx=max(milestones)
        rest=summ-maxx
        if maxx*2<=summ:
            return summ
        return rest*2+1

class tester(unittest.TestCase):
    def test0(self):
        milestones = [5,5,1]
        Output= 23
        self.assertEqual(Output,get_sol().numberOfWeeks(milestones))
    def test1(self):
        milestones = [1,2,3]
        Output= 6
        self.assertEqual(Output,get_sol().numberOfWeeks(milestones))
    def test2(self):
        milestones = [5,2,1]
        Output= 7
        self.assertEqual(Output,get_sol().numberOfWeeks(milestones))
    def test3(self):
        milestones = [1,10,7,1,7,2,10,10,355359359]
        Output= 97
        self.assertEqual(Output,get_sol().numberOfWeeks(milestones))
    def test5(self):
        milestones = [9,3,6,8,2,1]
        Output= 29
        self.assertEqual(Output,get_sol().numberOfWeeks(milestones))
    # def test6(self):
    # def test7(self):